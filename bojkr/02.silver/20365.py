# 20365 블로그2
# https://www.acmicpc.net/problem/20365
# Silver 3
# solved

import sys

def main():
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    
    _min = 1e9
    # Blue base, Red covered
    result = 0
    start = N; end = -1
    for i in range(N):
        if S[i] == 'B':
            start = i
            break
    for i in range(N-1, -1, -1):
        if S[i] == 'B':
            end = i
            break
    if start <= end:
        result += 1

    cur = 0
    while cur < N:
        if S[cur] == 'R':
            while cur < N and S[cur] == 'R':
                cur += 1
            result += 1
        else:
            cur += 1
    
    _min = result
        
    # Red base, blue covered
    result = 0
    start = N; end = -1
    for i in range(N):
        if S[i] == 'R':
            start = i
            break
    for i in range(N-1, -1, -1):
        if S[i] == 'R':
            end = i
            break
    if start <= end:
        result += 1

    cur = 0
    while cur < N:
        if S[cur] == 'B':
            while cur < N and S[cur] == 'B':
                cur += 1
            result += 1
        else:
            cur += 1
    
    _min = min(_min, result)
    print(_min)

if __name__ == "__main__":
    main()