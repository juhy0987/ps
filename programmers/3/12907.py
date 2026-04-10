# 12907 거스름돈
# https://school.programmers.co.kr/learn/courses/30/lessons/12907
# level 3
# dp

import sys

def solution(n, money):
    answer = 0
    dp = [0] * (n+1)
    dp[0] = 1
    
    for coin in money:
        for v in range(coin, n+1):
            dp[v] += dp[v-coin]
    
    return dp[n]
