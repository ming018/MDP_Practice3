'''
w, w(c), w(w) = 0.4, 1.5, 1
람다u, 뮤c, 뮤w = 0.1, 0.1, 0.5
Ls, Ld = 1, 0.59
타우 = 1
'''

w = 0.4
wc = 1.5
ww = 1
lamu = 0.1
mc = 0.1
mw = 0.5
ls = 1
ld = 0.59
tau = 1

import numpy as np

# SAS의 행동
action = [0, 1] # 0 : egg, 1 : push
# 모드
t = [0, 1] # 0 : cellular, 1 : wifi


n = 5 # 최대 담을 수 있는 데이터의 갯수
# 셀룰러, 와이파이의 상태에 따른 데이터 갯수?
states = [[0 for _ in range(n)] for _ in range(len(t))]

# 전이 확률 행렬
p = [[[0 for _ in range(len(states[0]) + 1)] for _ in range(len(states[0]))] for _ in range(len(t))]

def P(s_, s, a, t_ ,t) : # 전이 확률 계산
    return P1(s_, s, a) * P2(t_, t)

def P1(n_, n, a) :
    if not(n_ == len(states[0])) :
        if a == 0 : # 액션이 에그 인 경우
            if n_ == n + 1 :
                return lamu * tau
            elif n_ == n :
                return 1 - (lamu * tau)
            else :
                return 0
            
        elif a == 1 :
            if n_ == 0 :
                return 1
            else :
                return 0
        
        else :
            return 0
    else :
        return 0
    
def P2(t_, t) :
    if t == 0 : # 셀룰러인 경우
        if t_ == 1 : # 와이파이로 변경될 확률
            return mc * tau
        elif t_ == 0 : # 셀룰러로 지속될 확률
            return 1 - (mc * tau)
        else :
            return 0
    elif t == 1 : # 와이파이인 경우
        if t_ == 0 : # 셀룰러로 변경될 확률
            return mw * tau
        elif t_ == 1 : # 와이파이로 계속될 확률
            return 1 - (mw * tau)
        else :
            return 0
        

def pas() : # 가릴려고 만듦
    print()
    # # 0에서 에그를 했는데 0이 되고 셀룰러에서 셀룰러가 될 확률
    # p[0][0][0] = P(0, 0, 0, 0, 0)
    # # 0에서 에그를 했는데 0이 되고 셀룰러에서 와이파이가 될 확률
    # p[0][0][1] = P(0, 0, 0, 1, 0)
    # # 0에서 에그를 했는데 1이 되고 셀룰러에서 셀룰러가 될 확률
    # p[0][0][2] = P(1, 0, 0, 0, 0)
    # # 0에서 에그를 했는데 1이 되고 셀룰러에서 와이파이가 될 확률
    # p[0][0][3] = P(1, 0, 0, 1, 0)

    # # 1에서 에그를 했는데 1이 되고 셀룰러에서 셀룰러가 될 확률
    # p[0][1][0] = P(1, 1, 0, 0, 0)
    # # 1에서 에그를 했는데 1이 되고 셀룰러에서 와이파이가 될 확률
    # p[0][1][1] = P(1, 1, 0, 1, 0)
    # # 1에서 에그를 했는데 2이 되고 셀룰러에서 셀룰러가 될 확률
    # p[0][1][2] = P(2, 1, 0, 0, 0)
    # # 1에서 에그를 했는데 2이 되고 셀룰러에서 와이파이가 될 확률
    # p[0][1][3] = P(2, 1, 0, 1, 0)

    # # 2에서 에그를 했는데 2이 되고 셀룰러에서 셀룰러가 될 확률
    # p[0][2][0] = P(2, 2, 0, 0, 0)
    # # 2에서 에그를 했는데 2이 되고 셀룰러에서 와이파이가 될 확률
    # p[0][2][1] = P(2, 2, 0, 1, 0)
    # # 2에서 에그를 했는데 3이 되고 셀룰러에서 셀룰러가 될 확률
    # p[0][2][2] = P(3, 2, 0, 0, 0)
    # # 2에서 에그를 했는데 3이 되고 셀룰러에서 와이파이가 될 확률
    # p[0][2][3] = P(3, 2, 0, 1, 0)

    # # 0에서 푸쉬를 했는데 0이 되고 셀룰러에서 셀룰러가 될 확률
    # p[1][0][0] = P(0, 0, 1, 0, 0)
    # # 0에서 푸쉬를 했는데 0이 되고 셀룰러에서 와이파이가 될 확률
    # p[1][0][1] = P(0, 0, 1, 1, 0)

    # # 1에서 푸쉬를 했는데 0이 되고 셀룰러에서 셀룰러가 될 확률
    # p[1][1][0] = P(0, 1, 1, 0, 0)
    # # 1에서 푸쉬를 했는데 0이 되고 셀룰러에서 와이파이가 될 확률
    # p[1][1][1] = P(0, 1, 1, 1, 0)

    # # 2에서 푸쉬를 했는데 0이 되고 셀룰러에서 셀룰러가 될 확률
    # p[1][2][0] = P(0, 2, 1, 0, 0)
    # # 2에서 푸쉬를 했는데 0이 되고 셀룰러에서 와이파이가 될 확률
    # p[1][2][1] = P(0, 2, 1, 1, 0)

def setP() : # 전이확률 행렬 생성
    for k in range(3):  # 두 번째 인덱스가 0, 1, 2로 반복
        for j in range(4):  # 세 번째 인덱스가 0, 1, 2, 3으로 반복
            p[0][k][j] = P(k + j//2, k,  0, j % 2, 0)

    for i in range(3):  # 두 번째 인덱스 (0, 1, 2)
        for j in range(2):  # 세 번째 인덱스 (0, 1)
            p[1][i][j] = P(0, i, 1, j, 0)

def showP() : # 출력용 함수
    for i in range(len(p)) :
        for k in range(len(p[0])) :
            print(p[i][k])
            print('sum :', sum(p[i][k]))
            print()
        print('---')


def s(s, a, t) : # 보상 함수
    return w * f(s, a, t) - (1 - w) * g(s, a)

def f(n, a, t) :
    if a == 0 :
        if t == 0 :
            return wc * (ls + n * ld)
        elif t == 1 :
            return ww * (ls + n * ld)
        else :
            return 0
    else :
        return 0
    
def g(s, a) :
    if a == 0 :
        return s
    else :
        return 0
    
def iteration(gamma=0.9, limit=0.001):
    num_states = n * len(t)  # 상태 갯수를 계산합니다. 'n'은 상태의 수, 't'는 통신 타입의 수입니다.
    v = np.zeros(num_states)  # 각 상태의 가치를 저장할 배열을 초기화합니다.
    policy = np.zeros(num_states)  # 각 상태에 대한 최적 정책을 저장할 배열을 초기화합니다.

    def get_index(state, t_state):  # 2차원 상태를 1차원 인덱스로 변환하는 함수입니다.
        return state * len(t) + t_state

    delta = limit  # 변화량을 초기화합니다. 이 값은 가치의 변화가 얼마나 되었는지 추적합니다.
    while delta >= limit:
        delta = 0
        for state in range(n):  # 모든 상태에 대해 반복합니다.

            for t_state in range(len(t)):  # 모든 통신 타입에 대해 반복합니다.
                idx = get_index(state, t_state)  # 현재 상태와 통신 타입을 1차원 인덱스로 변환합니다.

                v_old = v[idx]  # 현재 상태의 이전 가치를 저장합니다.
                v_new = 0

                for a in action:  # 가능한 모든 행동에 대해 반복합니다.
                    expected_value = 0  # 행동의 기대 가치를 계산하기 위해 초기화합니다.
                    
                    for s_prime in range(n):  # 가능한 모든 다음 상태에 대해 반복합니다.
                        for t_prime in range(len(t)):  # 가능한 모든 다음 통신 타입에 대해 반복합니다.
                            idx_prime = get_index(s_prime, t_prime)
                            transition_prob = P(s_prime, state, a, t_prime, t_state)  # 상태 전이 확률을 계산합니다.
                            reward = s(state, a, t_state)  # 보상을 계산합니다.
                            expected_value += transition_prob * (reward + gamma * v[idx_prime])  # 기대 가치를 갱신합니다.

                            if expected_value > v_new:
                                v_new = expected_value  # 새로운 가치를 갱신합니다.
                                policy[idx] = a  # 최적 정책을 갱신합니다.
                
                v[idx] = v_new  # 가치 배열을 새로운 가치로 갱신합니다.
                delta = max(delta, abs(v_old - v[idx]))  # 변화량을 계산하여 갱신합니다.

    return v, policy  # 최종 가치 배열과 정책 배열을 반환합니다.


def main() :
    V, policy = iteration()

    for i in range(len(policy)) :
        if i == len(policy) // 2 :
            print()
        print(policy[i], end = ' ')

    print()
    print()

    for i in range(len(V)) :
        if i == len(V) // 2 :
            print()
        print(round(V[i], 1), end = ' ')
    
if __name__ == '__main__'  :
    main()

