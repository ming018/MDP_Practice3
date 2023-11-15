'''
w, w(c), w(w) = 0.4, 1.5, 1
람다u, 뮤c, 뮤w = 0.1, 0.1, 0.5
Ls, Ld = 1, 0.59
타우 = 1
'''


import numpy as np

# 셀룰러, 와이파이의 상태에 따른 데이터 갯수?
states = [[0 for _ in range(3)] for _ in range(2)] # 원래 3 * 2 되있던거 일단 3만 해봄
# SAS의 행동
action = [0, 1] # 0 : egg, 1 : push
field = np.empty((len(states), len(states[0])))
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

def setreword() :
    for i in range(len(field)) :
        for k in range(len(field[0])) :
            array = []
            for a in action :
                array.append(reword(k, a, i))
            field[i][k] = max(array)

# 보상 함수
def reword(s, a, t) : # 현재상태?, 액션(에그, 푸쉬), 모드(셀룰러, 와이파이)
    tem1 = f(s, a, t)
    tem2 = g(s, a)
    return 0.4 * tem1 - (1 - 0.4) * tem2

def f(s, a, t) :
    if a == 0 :
        if t == 1 :
            return 1 * (1 + s * 0.59)
        elif t == 0 :
            return 1.5 * (1 + s * 0.59)
    else :
        return 0

def g(s, a) :
    if a == 0 :
        return s
    else :
        return 0
    
# def P(n, a, n2, t, t2)
print(P(0, 1, 0, 0, 0))
print(P(0, 1, 1, 0, 0))
print(P(0, 1, 0, 0, 1))
print(P(0, 1, 1, 0, 1))

