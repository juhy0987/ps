# 27515 1차원 2048과 쿼리
# https://www.acmicpc.net/problem/27515
# Silver 2
# solved
# bit calculation
# important

import sys
import math

def main():
    Q = int(input())
    S = 0
        
    for _ in range(Q):
        _input = sys.stdin.readline().rstrip()
        x = int(_input)
        if x == 0:
            pass
        else:
            S += x
        
        if S == 0:
            print(0)
        else:
            print(1 << (S.bit_length()-1))

if __name__ == "__main__":
    main()