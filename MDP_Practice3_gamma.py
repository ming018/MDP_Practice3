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

# SAS의 행동
action = [0, 1] # 0 : egg, 1 : push
# 모드
t = [0, 1] # 0 : cellular, 1 : wifi


full_n = 3 # 최대 담을 수 있는 데이터의 갯수
# 셀룰러, 와이파이의 상태에 따른 데이터 갯수?
states = [[0 for _ in range(full_n)] for _ in range(len(t))]

# 전이 확률 행렬
p = [[[0 for _ in range(len(states[0]) + 1)] for _ in range(len(states[0]))] for _ in range(len(t))]

def P(s_, s, a, t_ ,t) : # 전이 확률 계산
    return P1(s_, s, a) * P2(t_, t)

def P1(n_, n, a) :
    
    n = n - full_n if n >= full_n else n
    n_ = n_ - full_n if n_ >= full_n else n_
    
        
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
                return 0
            else :
                return 1
        
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


def reward(s, a, t) : # 보상 함수
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
    num_states = full_n * len(t)  # 상태 갯수를 계산합니다. 'n'은 상태의 수, 't'는 통신 타입의 수입니다.
    v = np.zeros(num_states)  # 각 상태의 가치를 저장할 배열을 초기화합니다.
    policy = np.zeros(num_states)  # 각 상태에 대한 최적 정책을 저장할 배열을 초기화합니다.

    i = 0

    
    while True :
        print('v[0]진행중')
        print(i, '번째 반복')
  
        temp = v[0]
        
        egging = []

        egging.append(reward(0, 0, 0) + (1 - lama) * P(0, 0, 0, 0, 0) * v[0]) # egg, c, n` = n
        egging.append(reward(0, 0, 0) + (1 - lama) * P(1, 0, 0, 0, 0) * v[1]) # egg, c, n` = n + 1
        egging.append(reward(0, 0, 0) + (1 - lama) * P(0, 0, 0, 1, 0) * v[0 + full_n]) # egg, w, n` = n
        egging.append(reward(0, 0, 0) + (1 - lama) * P(1, 0, 0, 1, 0) * v[0 + full_n]) # egg, w, n` = n + 1

        pushing = []
        pushing.append(reward(0, 1, 0) + (1 - lama) * P(0, 0, 1, 0, 0) * v[0]) # push, c, n` = n = 0
        pushing.append(reward(0, 1, 0) + (1 - lama) * P(0, 0, 1, 1, 0) * v[0 + full_n]) # push, w, n` = n = 0
        
        check = []
        check.append(sum(egging)/len(egging))
        check.append(sum(pushing) / len(pushing))

        print('egging :', egging)
        print('pushing :', pushing)
        print('check :', check)

        if check[0] >= check[1] :
            
            policy[0] = 3
        else :
            policy[0] = 1

        print('이하 policy')
        print(policy[:len(policy) // 2])
        print(policy[len(policy) // 2 :])

        v[0] = sum(egging) + sum(pushing)

        
        if limit >= v[0] - temp :
            break
        
        i += 1
        print()
        print('------------------------------')
        print()

    i = 0

    
    while True :
        print('v[1]진행중')
        print(i, '번째 반복')

        temp = v[1]
        
        egging = []
        
        egging.append(reward(1, 0, 0) + (1 - lama) * P(1, 1, 0, 0, 0) * v[1]) # egg, c, n` = n
        egging.append(reward(1, 0, 0) + (1 - lama) * P(2, 1, 0, 0, 0) * v[1 + 1]) # egg, c, n` = n + 1
        egging.append(reward(1, 0, 0) + (1 - lama) * P(1, 1, 0, 1, 0) * v[1 + full_n]) # egg, w, n` = n
        egging.append(reward(1, 0, 0) + (1 - lama) * P(2, 1, 0, 1, 0) * v[1 + full_n + 1]) # egg, w, n` = n + 1

        pushing = []
        pushing.append(reward(1, 1, 0) + (1 - lama) * P(0, 1, 1, 0, 0) * v[0]) # push, c, n` = n = 0
        pushing.append(reward(1, 1, 0) + (1 - lama) * P(0, 1, 1, 1, 0) * v[0 + full_n]) # push, w, n` = n = 0
        
        check = []
        check.append(sum(egging)/len(egging))
        check.append(sum(pushing) / len(pushing))

        print('egging :', egging)
        print('pushing :', pushing)
        print('check :', check)

        policy[1] = 3 if check[0] > check[1] else 1

        print('이하 policy')
        print(policy[:len(policy) // 2])
        print(policy[len(policy) // 2 :])

        v[1] = sum(egging) + sum(pushing)

        if limit >= v[1] - temp :
            break
        i += 1
        print()
        print('------------------------------')
        print()


    i = 0

    while True :
        print('v[2]진행중')
        print(i, '번째 반복')
        temp = v[2]
        
        idx = 2

        egging = []

        if not(idx == full_n - 1) :  
            egging.append(reward(idx, 0, 0) + (1 - lama) * P(idx, idx, 0, 0, 0) * v[idx]) # egg, c, n` = n
            egging.append(reward(idx, 0, 0) + (1 - lama) * P(idx + 1, idx, 0, 0, 0) * v[idx]) # egg, c, n` = n + 1
            
            egging.append(reward(idx, 0, 0) + (1 - lama) * P(idx, idx, 0, 1, 0) * v[idx + full_n]) # egg, w, n` = n
            egging.append(reward(idx, 0, 0) + (1 - lama) * P(idx + 1, idx, 0, 1, 0) * v[idx + full_n + 1]) # egg, w, n` = n + 1
        else :
            egging.append(0)

        pushing = []
        pushing.append(reward(idx, 1, 0) + (1 - lama) * P(0, idx, 1, 0, 0) * v[0]) # push, c, n` = n = 0
        pushing.append(reward(idx, 1, 0) + (1 - lama) * P(3, idx, 1, 1, 0) * v[full_n]) # push, w, n` = n = 0
        
        check = []
        check.append(sum(egging) /len(egging))
        check.append(sum(pushing) / len(pushing))

        print('egging :', egging)
        print('pushing :', pushing)
        print('check :', check)

        policy[idx] = 3 if check[0] > check[1] else 1

        print('이하 policy')
        print(policy[:len(policy) // 2])
        print(policy[len(policy) // 2 :])

        v[idx] = sum(egging) + sum(pushing)

        if limit >= v[idx] - temp :
            break
        i += 1

        print()
        print('------------------------------')
        print()
    
    i = 0

    while True :
        print('v[3]진행중')
        print(i, '번째 반복')
        temp = v[3]
        
        egging = []

        egging.append(reward(3, 0, 1) + (1 - lama) * P(0, 3, 0, 0, 1) * v[3]) # egg, c, n` = n
        egging.append(reward(3, 0, 1) + (1 - lama) * P(1, 3, 0, 0, 1) * v[3 + 1]) # egg, c, n` = n + 1
        egging.append(reward(3, 0, 1) + (1 - lama) * P(3, 3, 0, 1, 1) * v[3 - full_n]) # egg, w, n` = n
        egging.append(reward(3, 0, 1) + (1 - lama) * P(4, 3, 0, 1, 1) * v[3 - full_n + 1]) # egg, w, n` = n + 1

        pushing = []
        pushing.append(reward(3, 1, 1) + (1 - lama) * P(0, 3, 1, 0, 1) * v[0]) # push, c, n` = n = 0
        pushing.append(reward(3, 1, 1) + (1 - lama) * P(3, 3, 1, 1, 1) * v[0 + full_n]) # push, w, n` = n = 0
        
        check = []
        check.append(sum(egging)/len(egging))
        check.append(sum(pushing) / len(pushing))

        print('egging :', egging)
        print('pushing :', pushing)
        print('check :', check)

        policy[3] = 3 if check[0] > check[1] else 1

        print('이하 policy')
        print(policy[:len(policy) // 2])
        print(policy[len(policy) // 2 :])

        v[3] = sum(egging) + sum(pushing)

        print()
        print('------------------------------')
        print()

        if limit >= v[3] - temp :
            break
        i += 1
 

    i = 0

    while True :
        print('v[4]진행중')
        print(i, '번째 반복')
        temp = v[4]
        
        egging = []

        egging.append(reward(3, 0, 1) + (1 - lama) * P(1, 4, 0, 0, 1) * v[4 - full_n]) # egg, c, n` = n
        egging.append(reward(3, 0, 1) + (1 - lama) * P(2, 4, 0, 0, 1) * v[4 - full_n + 1]) # egg, c, n` = n + 1
        egging.append(reward(3, 0, 1) + (1 - lama) * P(4, 4, 0, 1, 1) * v[4]) # egg, w, n` = n
        egging.append(reward(3, 0, 1) + (1 - lama) * P(5, 4, 0, 1, 1) * v[4 + 1]) # egg, w, n` = n + 1

        pushing = []
        pushing.append(reward(3, 1, 1) + (1 - lama) * P(0, 4, 1, 0, 1) * v[4 - full_n]) # push, c, n` = n = 0
        pushing.append(reward(3, 1, 1) + (1 - lama) * P(3, 4, 1, 1, 1) * v[4]) # push, w, n` = n = 0
        
        check = []
        check.append(sum(egging)/len(egging))
        check.append(sum(pushing) / len(pushing))

        print('egging :', egging)
        print('pushing :', pushing)
        print('check :', check)

        policy[4] = 3 if check[0] > check[1] else 1

        print('이하 policy')
        print(policy[:len(policy) // 2])
        print(policy[len(policy) // 2 :])

        v[4] = sum(egging) + sum(pushing)

        print()
        print('------------------------------')
        print()

        if limit >= v[4] - temp :
            break
        i += 1

    
    i = 0

    while True :
        print('v[5]진행중')
        print(i, '번째 반복')
        temp = v[5]
        
        egging = []
        idx = 5

        if idx == 5 :
            egging.append(0)
        else :
            egging.append(reward(idx, 0, 0) + (1 - lama) * P(idx, idx, 0, 0, 0) * v[idx]) # egg, c, n` = n
            egging.append(reward(idx, 0, 0) + (1 - lama) * P(idx + 1, idx, 0, 0, 0) * v[idx]) # egg, c, n` = n + 1
            
            egging.append(reward(idx, 0, 0) + (1 - lama) * P(idx, idx, 0, 1, 0) * v[idx + full_n]) # egg, w, n` = n
            egging.append(reward(idx, 0, 0) + (1 - lama) * P(idx + 1, idx, 0, 1, 0) * v[idx + full_n + 1]) # egg, w, n` = n + 1

        pushing = []
        pushing.append(reward(5, 1, 1) + (1 - lama) * P(0, 5, 1, 0, 1) * v[0]) # push, c, n` = n = 0
        pushing.append(reward(5, 1, 1) + (1 - lama) * P(3, 5, 1, 1, 1) * v[0 + full_n]) # push, w, n` = n = 0
        
        check = []
        check.append(sum(egging)/len(egging))
        check.append(sum(pushing) / len(pushing))

        print('egging :', egging)
        print('pushing :', pushing)
        print('check :', check)

        policy[5] = 3 if check[0] > check[1] else 1

        print('이하 policy')
        print(policy[:len(policy) // 2])
        print(policy[len(policy) // 2 :])

        v[5] = sum(egging) + sum(pushing)
        print()
        print('------------------------------')
        print()
        if limit >= v[5] - temp :
            break
        i += 1



    return v, policy  # 최종 가치 배열과 정책 배열을 반환합니다.

def main() :
    V, policy = iteration()

    # for i in range(len(policy)) :
    #     if i == len(policy) // 2 :
    #         print()
    #     print(policy[i], end = ' ')

    # print()
    # print()

    # for i in range(len(V)) :
    #     if i == len(V) // 2 :
    #         print()
    #     print(round(V[i], 1), end = ' ')
    
if __name__ == '__main__'  :
    main()
