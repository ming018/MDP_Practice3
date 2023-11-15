import numpy as np

# 전역 변수 설정
w = 0.4
wc = 1.5
ww = 1
lamu = 0.1
mc = 0.1
mw = 0.5
ls = 1
ld = 0.59
tau = 1
n = 5

# SAS의 행동
action = [0, 1]  # 0 : egg, 1 : push
# 모드
t = [0, 1]  # 0 : cellular, 1 : wifi

# 상태와 모드에 대한 인덱스 배열 생성
state_indices = np.arange(n)  # [0, 1, 2, 3, 4]
mode_indices = np.array(t)  # [0, 1]

# 전이 확률 함수
def P(s_, s, a, t_ ,t):
    return P1(s_, s, a) * P2(t_, t)

def P1(n_, n, a):
    if n_ >= len(state_indices):
        n_ = len(state_indices) - 1
    if a == 0:
        if n_ == n + 1:
            return lamu * tau
        elif n_ == n:
            return 1 - lamu * tau
        else:
            return 0
    elif a == 1:
        if n_ == 0:
            return 1
        else:
            return 0
    else:
        return 0

def P2(t_, t):
    if t == 0:
        if t_ == 1:
            return mc * tau
        elif t_ == 0:
            return 1 - mc * tau
        else:
            return 0
    elif t == 1:
        if t_ == 0:
            return mw * tau
        elif t_ == 1:
            return 1 - mw * tau
        else:
            return 0
    else:
        return 0

# 보상 함수
def s(s, a, t):
    return w * f(s, a, t) - (1 - w) * g(s, a)

def f(n, a, t):
    if a == 0:
        if t == 0:
            return wc * (ls + n * ld)
        elif t == 1:
            return ww * (ls + n * ld)
        else:
            return 0
    else:
        return 0
    
def g(s, a):
    if a == 0:
        return s
    else:
        return 0

# 가치 반복 알고리즘
def value_iteration(states, actions, reward, p, gamma, theta=0.001):
    V = np.zeros(len(states))
    policy = np.zeros(len(states), dtype=int)

    while True:
        delta = 0
        for s in range(len(states)):
            v = V[s]
            max_value = float('-inf')
            for a in range(len(actions)):
                value_sum = 0
                for i in range(len(states)):
                    value_sum += p[s][i][a] * (reward[s][a] + gamma * V[i])
                max_value = max(max_value, value_sum)
            V[s] = max_value
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break

    for s in range(len(states)):
        max_action_value = float('-inf')
        best_action = 0
        for a in range(len(actions)):
            value_sum = 0
            for i in range(len(states)):
                value_sum += p[s][i][a] * (reward[s][a] + gamma * V[i])
            if value_sum > max_action_value:
                max_action_value = value_sum
                best_action = a
        policy[s] = best_action

    return policy, V

# 상태와 행동 리스트 생성
states_list = [i * len(mode_indices) + j for i in range(len(state_indices)) for j in range(len(mode_indices))]

# 보상 함수 생성
reward = np.zeros((len(states_list), len(action)))
for i in range(len(states_list)):
    state = state_indices[states_list[i] % len(state_indices)]
    mode = mode_indices[states_list[i] // len(state_indices)]
    reward[i][action[0]] = s(state, action[0], mode)
    reward[i][action[1]] = s(state, action[1], mode)

# 전이 확률 행렬 계산
p = np.zeros((len(states_list), len(states_list), len(action)))
for i in range(len(states_list)):
    current_state = state_indices[states_list[i] % len(state_indices)]
    current_mode = mode_indices[states_list[i] // len(state_indices)]
    for a in action:
        for j in range(len(states_list)):
            next_state = state_indices[states_list[j] % len(state_indices)]
            next_mode = mode_indices[states_list[j] // len(state_indices)]
            p[i][j][a] = P(next_state, current_state, a, next_mode, current_mode)

# 가치 반복 알고리즘 실행
policy, V = value_iteration(states_list, action, reward, p, gamma=0.9)

# 결과 출력
print("Optimal policy:", policy)
for i in range(len(policy)):
    if i == len(policy) // 2:
        print()
    print(policy[i], end=' ') 
    
print("\nValue function:", V)
