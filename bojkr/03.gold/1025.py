# 1025 제곱수 찾기
# https://www.acmicpc.net/problem/1025
# Gold 5
# solved

import math

def main():
    N, M = map(int, input().split())
    A = []
    d = set()
    for i in range(100000):
        tmp = i ** 2
        if tmp >= 999999999:
            break
        d.add(tmp)
    
    for _ in range(N):
        A.append(list(input()))
    
    def select(i, j, gap_n, gap_m, s):
        if i >= N or j >= M or i < 0 or j < 0:
            return -1
        
        cur = [i, j]
        # print(i, j, gap_n, gap_m)
        s = s + A[i][j]
        _return = select(i+gap_n, j+gap_m, gap_n, gap_m, s)
        
        # print(int(s))
        if s:
            tmp = int(s)
            if tmp in d:
                _return = max(_return, tmp)
            
            tmp = int("".join(reversed(s)))
            if tmp in d:
                _return = max(_return, tmp)
        
        return _return
    
    _max = -1
    for a in range(-N+1, N):
        for b in range(-M+1, M):
            for i in range(N):
                for j in range(M):
                    if not a and not b:
                        continue
                    _max = max(_max, select(i, j, a, b, ""))
    if N == 1 and M == 1:
        tmp = int(A[0][0])
        if tmp in d:
            _max = tmp
    print(_max)
            
    
if __name__ == "__main__":
    main()