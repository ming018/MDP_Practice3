'''
w, w(c), w(w) = 0.4, 1.5, 1
람다u, 뮤c, 뮤w = 0.1, 0.1, 0.5
Ls, Ld = 1, 0.59
타우 = 1
'''

w = 0.4 # 비중변수(전송비용, 사용자qoe 비중 계산)
wc = 1.5 # 네트워크 유형, 셀룰러일때
ww = 1 # 네트워크 유형, 와이파이 일때
lamu = 0.1
lama = 0.1
mc = 0.1
mw = 0.5
ls = 1
ld = 0.59
tau = 1

import numpy as np
from matplotlib import pyplot as plt
import random

# SAS의 행동
action = [0, 1] # 0 : egg, 1 : push
# 모드
t = [0, 1] # 0 : cellular, 1 : wifi


full_n = 5 # 최대 담을 수 있는 데이터의 갯수
# 셀룰러, 와이파이의 상태에 따른 데이터 갯수?
states = [[0 for _ in range(full_n)] for _ in range(len(t))]

record = 10 # 그래프에서 저장할 단위

# 전이 확률 행렬
p = [[[0 for _ in range(len(states[0]) + 1)] for _ in range(len(states[0]))] for _ in range(len(t))]

def P(s_, s, a, t_ ,t) : # 전이 확률 계산
    return P1(s_, s, a) * P2(t_, t)

def P1(n_, n, a) :
    
    n = n - full_n if n >= full_n else n
    n_ = n_ - full_n if n_ >= full_n else n_
         
    if  a == 0 :
        if n < full_n : # 액션이 에그 인 경우
            if n_ == n + 1 :
                return lamu * tau
            elif n_ == n :
                return 1 - (lamu * tau)
            else :
                return 0
        else :
            return 0
    elif a == 1 :        
        if  n != 0 :
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


def reward(s, a, t) : # 보상 함수
    s = s - full_n if t == 1 else s
    return (w * f(s, a, t) - (1 - w) * g(s, a))

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
    
def iteration():
    num_states = full_n * len(t)  # 상태 갯수를 계산합니다. 'n'은 상태의 수, 't'는 통신 타입의 수입니다.
    v = np.zeros(num_states)  # 각 상태의 가치를 저장할 배열을 초기화합니다.
    policy = np.zeros(num_states)  # 각 상태에 대한 최적 정책을 저장할 배열을 초기화합니다.
    
    for s in range(len(v)) :

        i = 0
        temp = 0
        
        while True :
            temp = v[s]
            
            egging = []
            pushing = []

            if s <= full_n - 1 : # 셀룰러 상태 처리 
                if  s == full_n - 1 : # 데이터 갯수 == n
                    egging.append(0)

                    pushing.append(0)
                else :
                    egging.append(reward(s, 0, 0) + (1 - lama) * P(s, s, 0, 0, 0) * v[s]) # egg, c, n` = n
                    egging.append(reward(s, 0, 0) + (1 - lama) * P(s + full_n, s, 0, 1, 0) * v[s + full_n]) # egg, w, n` = n
                    egging.append(reward(s, 0, 0) + (1 - lama) * P(s + 1, s, 0, 0, 0) * v[s + 1]) # egg, c, n` = n + 1
                    egging.append(reward(s, 0, 0) + (1 - lama) * P(s + full_n + 1, s, 0, 1, 0) * v[s + full_n + 1]) # egg, w, n` = n + 1

                    pushing.append(reward(s, 1, 0) + (1 - lama) * P(0, s, 1, 0, 0) * v[0]) # push, c, n` = n = 0
                    pushing.append(reward(s, 1, 0) + (1 - lama) * P(full_n, s, 1, 1, 0) * v[full_n]) # push, w, n` = n = 0

            else : # 와이파이 상태 처리
                if  s == len(v) - 1 : # 데이터 갯수 == n
                    egging.append(0)

                    pushing.append(0)
                else :
                    egging.append(reward(s, 0, 1) + (1 - lama) * P(s - full_n, s, 0, 0, 1) * v[s - full_n]) # egg, c, n` = n
                    egging.append(reward(s, 0, 1) + (1 - lama) * P(s - full_n + 1, s, 0, 0, 1) * v[s - full_n + 1]) # egg, c, n` = n + 1

                    egging.append(reward(s, 0, 1) + (1 - lama) * P(s, s, 0, 1, 1) * v[s]) # egg, w, n` = n
                    egging.append(reward(s, 0, 1) + (1 - lama) * P(s + 1, s, 0, 1, 1) * v[s + 1]) # egg, w, n` = n + 1

                    pushing.append(reward(s, 1, 1) + (1 - lama) * P(0, s, 1, 0, 1) * v[0]) # push, c, n` = n = 0
                    pushing.append(reward(s, 1, 1) + (1 - lama) * P(full_n, s, 1, 1, 1) * v[full_n]) # push, w, n` = n = 0
        
            check = []
            check.append(sum(egging) / len(egging))
            check.append(sum(pushing) / len(pushing))

            policy[s] = 0 if check[0] > check[1] else 1

            v[s] = sum(egging) + sum(pushing)
            
            if 1 * lama / 2 * (1 - lama) >= abs(v[s] - temp) :
                break

            i += 1


    return policy  # 최종 정책 배열을 반환합니다.

def ops_testing(policy) :
    state = 0

    type = 0

    re = 0

    array = []
    array.append(P(state, state, 0, 0, type))
    array.append(P(state + 1, state, 0, 0, type))
    array.append(P(state, state, 0, 1, type))
    array.append(P(state + 1, state, 0, 1, type))

    i = 0

    result = []

    while True :
        rand = random.random()
        ac = policy[state]
        
        re += reward(state, ac, type)

        # 최적 정책이 egg인 경우
        if policy[state] == 0 :

            array = []
            array.append(P(state, state, 0, 0, type))
            array.append(P(state + 1, state, 0, 0, type))
            array.append(P(state, state, 0, 1, type))
            array.append(P(state + 1, state, 0, 1, type))

            # 0 -> 0
            if rand < array[0] :
                state = state if state < full_n else state - full_n
                type = type if state < full_n else 0

            # 0 -> 1
            elif rand < sum(array[0 : 2]) :
                state = state + 1 if state < full_n else state - full_n + 1
                type = type if state < full_n else 0

            # 0 -> len(policy) // 2
            elif rand < sum(array[0 : 3]) :
                state = state + len(policy) // 2 if state < full_n else state
                type = 1

            # 0 -> len(policy) // 2 + 1
            elif rand < sum(array) :
                state = state + len(policy) // 2 + 1 if state < full_n else state
                type = 1
            
            else :
                print('흠..')

        # 현재 상태의 최적 정책이 push인 경우
        elif policy[state] == 1 :
            array = []
            array.append(P(0, state, 1, 0, type))
            array.append(P(full_n, state, 1, 1, type))

            if rand > array[0] :
                state = 0
                type = 0

            else :
                state = full_n
                type = 1

        if i % record == 0:
            result.append(round(re, 1))
            
        i += 1
        if i == 100 :
            return result
        

def push_testing(policy) :
    state = 0

    type = 0

    re = 0

    array = []
    array.append(P(state, state, 0, 0, type))
    array.append(P(state + 1, state, 0, 0, type))
    array.append(P(state, state, 0, 1, type))
    array.append(P(state + 1, state, 0, 1, type))

    i = 0

    result = []

    pushing_policy = []

    for i in range(len(policy)) :
        if i == 0 or i == full_n :
            pushing_policy.append(0)
            continue
        pushing_policy.append(1)

    i = 0

    while True :
        rand = random.random()
        ac = pushing_policy[state]
        
        re += reward(state, ac, type)

        # 최적 정책이 egg인 경우
        if pushing_policy[state] == 0 :

            array = []
            array.append(P(state, state, 0, 0, type))
            array.append(P(state + 1, state, 0, 0, type))
            array.append(P(state, state, 0, 1, type))
            array.append(P(state + 1, state, 0, 1, type))

            # 0 -> 0
            if rand < array[0] :
                state = state if state < full_n else state - full_n
                type = type if state < full_n else 0

            # 0 -> 1
            elif rand < sum(array[0 : 2]) :
                state = state + 1 if state < full_n else state - full_n + 1
                type = type if state < full_n else 0

            # 0 -> len(policy) // 2
            elif rand < sum(array[0 : 3]) :
                state = state + len(policy) // 2 if state < full_n else state
                type = 1

            # 0 -> len(policy) // 2 + 1
            elif rand < sum(array) :
                state = state + len(policy) // 2 + 1 if state < full_n else state
                type = 1
            
            else :
                print('흠..')

        # 현재 상태의 최적 정책이 push인 경우
        elif policy[state] == 1 :
            array = []
            array.append(P(0, state, 1, 0, type))
            array.append(P(full_n, state, 1, 1, type))

            if rand > array[0] :
                state = 0
                type = 0

            else :
                state = full_n
                type = 1

        if i % record == 0 :
            result.append(round(re, 1))

        i += 1
        if i == 100 :
            return result

def egg_testing(policy) :
    state = 0

    type = 0

    re = 0

    array = []
    
    i = 0

    result = []

    egging_policy = []

    for i in range(len(policy)) :
        if i == full_n - 1 or i == len(policy) - 1 :
            egging_policy.append(1)
            continue
        egging_policy.append(0)
    
    print(egging_policy)

    i = 0

    while True :
        rand = random.random()
        ac = egging_policy[state]
        
        re += reward(state, ac, type)

        # 최적 정책이 egg인 경우
        if egging_policy[state] == 0 :

            array = []
            array.append(P(state, state, 0, 0, type))
            array.append(P(state + 1, state, 0, 0, type))
            array.append(P(state, state, 0, 1, type))
            array.append(P(state + 1, state, 0, 1, type))

            # 0 -> 0
            if rand < array[0] :
                state = state if state < full_n else state - full_n
                type = type if state < full_n else 0

            # 0 -> 1
            elif rand < sum(array[0 : 2]) :
                state = state + 1 if state < full_n else state - full_n + 1
                type = type if state < full_n else 0

            # 0 -> len(policy) // 2
            elif rand < sum(array[0 : 3]) :
                state = state + len(policy) // 2 if state < full_n else state
                type = 1

            # 0 -> len(policy) // 2 + 1
            elif rand < sum(array) :
                state = state + len(policy) // 2 + 1 if state < full_n else state
                type = 1
            
            else :
                print('흠..')

        # 현재 상태의 최적 정책이 push인 경우
        elif policy[state] == 1 :
            array = []
            array.append(P(0, state, 1, 0, type))
            array.append(P(full_n, state, 1, 1, type))

            if rand > array[0] :
                state = 0
                type = 0

            else :
                state = full_n
                type = 1

        if i % record == 0 :
            result.append(round(re, 1))

        i += 1
        if i == 100 :
            return result



def main() :
    policy = iteration()
    
    ops_result = ops_testing(policy)

    push_result = push_testing(policy)

    egg_result = egg_testing(policy)

    x = ops_result  # X-axis from -10 to 10
    time = range(1, len(x) + 1)  # Y-axis from -10 to 10
    x2 = push_result
    x3 = egg_result

    plt.figure(figsize=(8, 6))
    plt.plot(time, x, marker='o', color = 'blue', label = 'ops')
    plt.plot(time, x2, marker='x', color='red', label='push')
    plt.plot(time, x3, marker='*', color='green', label='egg')
    plt.xlim(0, 10)
    
    plt.xlabel('Simulation time')
    plt.ylabel('Exptected total reward')
    # plt.title('Graph with X and Y axis from -10 to 10')

    plt.grid(True)
    plt.legend()
    plt.show()
    
if __name__ == '__main__'  :
    main()