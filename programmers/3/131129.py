# 131129 카운트 다운
# https://school.programmers.co.kr/learn/courses/30/lessons/131129
# level 3
# solved

def solution(target):
    answer = []
    
    cases = [[0,0] for _ in range(61)]
    for i in range(1, 21):
        cases[i] = [1, 1]
        for mul in range(2, 4):
            cases[i*mul] = [1, 0]
    for i in range(21, 41):
        if sum(cases[i]) != 0:
            continue
        cases[i] = [2, 2]
    for i in range(41, 50):
        if sum(cases[i]) != 0:
            continue
        cases[i] = [2, 1]
    cases[50] = [1, 1]
    for i in range(51, 61):
        if sum(cases[i]) != 0:
            continue
        cases[i] = [2, 2]
                            
    if target < 61:
        return cases[target]
    
    dp = cases + [[1e9, 1e9] for _ in range(61, target+1)]
    
    for i in range(60, 0, -1):
        for v in range(61, target+1):
            tmp = [dp[v-i][0]+dp[i][0], dp[v-i][1]+dp[i][1]]
            if tmp[0] < dp[v][0]:
                dp[v] = tmp
                continue
            elif tmp[0] == dp[v][0] and tmp[1] > dp[v][1]:
                dp[v] = tmp
                continue
    
    return dp[target]