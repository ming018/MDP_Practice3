'''
w, w(c), w(w) = 0.4, 1.5, 1
람다u, 뮤c, 뮤w = 0.1, 0.1, 0.5
Ls, Ld = 1, 0.59
타우 = 1
'''


# 셀룰러, 와이파이의 상태에 따른 데이터 갯수?
states = [0 for _ in range(3)] # 원래 3 * 2 되있던거 일단 3만 해봄
# SAS의 행동
acations = [0, 1] # 0 : egg, 1 : push
# 모드
t = [0, 1] # 0 : cellular, 1 : wifi

def P(n, a, n2, t, t2) : # 전이확률 계산한거
    return P1(n, a, n2) * P2(t, t2)

def P1(n, a, n2) : # SAS가 집약할지, 전송할지의 확률 반환
    if n < len(states) and a == 0 :
        if n2 == n + 1 :
            return 0.1 * 1
        elif n2 == n :
            return 1 - 0.1 * 1
            
    elif n != 0 and n2 == 0 and a == 1 :
        return 1
    
    else :
        return 0
    
def P2(t, t2) : # 데이터 모드 바뀌는 확률 반환
    if t == 0 : #  셀룰러 일 경우
        if t2 == 1 : # 변환할 모드가 와이파이 일 경우
            return 0.1 * 1
        elif t2 == 0 : # 변환할 모드가 셀룰러 일 경우
            return 1 - 0.1 * 1

    elif t == 1 : # 와이파이의 경우
        if t2 == 0 : # 변환할 모드가 셀룰러일 경우
            return 0.5 * 1
        elif t2 == 1 : # 변환할 모드가 와이파이인 경우
            return 1 - 0.5 * 1
        
# P = p1() * p2()

# 보상 함수
def reword(s, a, m, n) : # 현재상태?, 액션(푸쉬 에그), 모드(와이파이, 셀룰러), 데이터 갯수
    return 0.4 * f(s, a, m, n) - (1 - 0.4) * g(a, n)

def f(s, a, m, n) :
    if a == 'agg' :
        if m == 1 :
            return 1 * (1 + n * 0.59)
        elif m == 'cellualr' :
            return 1.5 * (1 + n * 0.59)
    else :
        return 0

def g(a, n) :
    if a == 'agg' :
        return n
    else :
        return 0


# 이게 상태 0부터 에이전트가 얻을 수 있는 모든 expected total reward라는거 같은데?
import numpy as np

# # 상태 전이 확률 행렬을 정의, 크기는 모든 상태 * 모드 * 액션
# P = np.zeros(len(states) * len(t) * len(acations))

# # 24개가 나왔음
# print(P)
'''
에그
0 0 0 0
0 0 0 0

푸쉬
0 0 0 0
0 0 0 0

?
0 0 0 0
0 0 0 0
'''



# 보상 행렬을 정의합니다. shape: [현재 상태][행동]
rewards = np.zeros(len(states) * len(acations))

# 감가율(discount factor)을 정의합니다.
gamma = 0.9

# 예시를 위한 상태 전이 확률과 보상을 설정합니다.

print('-----------------------------')
print('상태 1에서 push해서 상태0으로 되며, 셀룰러에서 셀룰러로 변경될 확률')
print(P(1, 1, 0, 0, 0))
print('상태 1에서 push를 해서 상태0이 되며, 셀룰러에서 와이파이로 변경될 확률')
print(P(1, 1, 0, 0, 1))
print('총합')
print(P(1, 1, 0, 0, 0) + P(1, 1, 0, 0, 1))
print('-----------------------------')


# 상태 0에서 행동 1을 선택했을 때
# P[0][1][1] = 1.0
# rewards[0][1] = 0


'''
# 나머지 전이 확률과 보상을 설정합니다.
# ...

# 가치 함수를 0으로 초기화합니다.
V = np.zeros(len(states))

# 가치 반복 알고리즘을 구현합니다.
def value_iteration(V, P, rewards, gamma, threshold=0.001):
    while True:
        delta = 0
        for s in range(len(states)):
            V_old = V[s]
            # 각 행동에 대한 기대 가치를 계산하고 최대값을 선택합니다.
            V[s] = max(
                sum(P[s][a][s_next] * (rewards[s][a] + gamma * V[s_next])
                    for s_next in range(len(states)))
                for a in range(len(acations))
            )
            delta = max(delta, abs(V_old - V[s]))
        if delta < threshold:
            break
    return V

# 가치 반복 알고리즘을 실행합니다.
V = value_iteration(V, P, rewards, gamma)

# 초기 상태에서의 기대 총 보상을 출력합니다.
initial_state = 0
expected_total_reward = V[initial_state]
print(f"Initial state {initial_state}의 기대 총 보상: {expected_total_reward}")

print(states)
print(rewards) '''



# def iteration(len(states), actions, r, gamma = 0.9, limit = 0.001) :
#     v = np.zeros(size * size) # 각 상태들의 가치
#     policy = np.zeros(size * size) # 각 상태들의 최적 정책

#     while True :
#         delta = 0 # 상태의 가치가 얼마나 변하는가를 담음
#         for s in len(states) :
#             temp_v = v[s] # 현재 상태의 밸류를 임시 저장

#             check = []
#             for a in actions :
#                 tmp1 = r[move(s, a)]
#                 tmp2 = gamma * move(s,a) * propagate_ratio
#                 check.append(tmp1 + tmp2)
#             v[s] = max(check)


#             # v[s] = max([r[move(s, a)] + gamma * move(s, a) * propagate_ratio] for a in actions)


#             delta = max(delta, abs(temp_v - v[s]))
#             # 기존의 가치 - 새로 갱신한 가치의값과 기존의 델타 값 중 뭐가 더 큰지를 비교
#         if delta < limit :
#             break
#          # 정의한 임계값보다 낮으면 더이상 변해도 의미가 없는 수렴 상태라고 판단 후 종료
    
#         for s in len(states):  # 모든 상태에 대해 반복
#         # 최적의 행동을 선택하는 정책 계산
#             policy[s] = np.argmax([r[move(s, a)] + gamma * v[move(s, a)] for a in actions])
    
#     return policy, v  # 최적 정책과 가치 함수 반환