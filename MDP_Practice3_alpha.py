'''
w, w(c), w(w) = 0.4, 1.5, 1
람다u, 뮤c, 뮤w = 0.1, 0.1, 0.5
Ls, Ld = 1, 0.59
타우 = 1
'''


# 셀룰러, 와이파이의 상태에 따른 데이터 갯수?
STATES = [[0 for _ in range(5)] for _ in range(2)]
# SAS의 행동
acations = ['push', 'egg']
# 모드
t = ['celluar', 'wifi']

def P1(n, n2, a) : # SAS가 집약할지, 전송할지의 확률 반환
    if n < limit and a == 'agg ':
        if n2 == n + 1 :
            return 0.1 * 1
        elif n2 == n :
            return 1 - 0.1 * 1
            
    elif n != 0 and n2 == 0 and a == 'push' :
        return 1
    
def P2(t, t2) : # 데이터 모드 바뀌는 확률 반환
    if t == 'celluar' :
        if t2 == 'wifi' :
            return 0.1 * 1
        elif t2 == 'celluar' :
            return 1 - 0.1 * 1

    elif t == 'wifi' :
        if t2 == 'celluar' :
            return 0.5 * 1
        elif t2 == 'wifi' :
            return 1 - 0.5 * 1
        
# P = p1() * p2()

# 보상 함수
def reword(s, a, m, n) : # 현재상태?, 액션(푸쉬 에그), 모드(와이파이, 셀룰러), 데이터 갯수
    return 0.4 * f(s, a, m, n) - (1 - 0.4) * g(a, n)

def f(s, a, m, n) :
    if a == 'agg' :
        if m == 'wifi' :
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









def iteration(states, actions, r, gamma = 0.9, limit = 0.001) :
    v = np.zeros(size * size) # 각 상태들의 가치
    policy = np.zeros(size * size) # 각 상태들의 최적 정책

    while True :
        delta = 0 # 상태의 가치가 얼마나 변하는가를 담음
        for s in states :
            temp_v = v[s] # 현재 상태의 밸류를 임시 저장

            check = []
            for a in actions :
                tmp1 = r[move(s, a)]
                tmp2 = gamma * move(s,a) * propagate_ratio
                check.append(tmp1 + tmp2)
            v[s] = max(check)


            # v[s] = max([r[move(s, a)] + gamma * move(s, a) * propagate_ratio] for a in actions)


            delta = max(delta, abs(temp_v - v[s]))
            # 기존의 가치 - 새로 갱신한 가치의값과 기존의 델타 값 중 뭐가 더 큰지를 비교
        if delta < limit :
            break
         # 정의한 임계값보다 낮으면 더이상 변해도 의미가 없는 수렴 상태라고 판단 후 종료
    
        for s in states:  # 모든 상태에 대해 반복
        # 최적의 행동을 선택하는 정책 계산
            policy[s] = np.argmax([r[move(s, a)] + gamma * v[move(s, a)] for a in actions])
    
    return policy, v  # 최적 정책과 가치 함수 반환