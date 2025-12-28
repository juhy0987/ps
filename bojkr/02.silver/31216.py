# 31216 슈퍼 소수
# https://www.acmicpc.net/problem/31216
# Silver 5
# solved

import math

def main():
    T = int(input())
    _input = []
    MAX = 318137
    for _ in range(T):
        _input.append(int(input()))
    
    _is_not_prime = [False] * (MAX+5)
    _is_not_prime[0] = _is_not_prime[1] = True
    for i in range(2, MAX+1):
        for j in range(i*i, MAX+1, i):
            _is_not_prime[j] = True

    super_prime = []
    cnt = 0
    for i in range(2, MAX+1):
        if not _is_not_prime[i]:
            cnt += 1
            if not _is_not_prime[cnt]:
                super_prime.append(i)
    
    for i in _input:
        print(super_prime[i-1])

if __name__ == "__main__":
    main()