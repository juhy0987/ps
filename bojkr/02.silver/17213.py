# 17213 과일 서리
# https://www.acmicpc.net/problem/17213
# Silver 2
# solved
# important (중복 조합 문제)

import sys
import math

def main():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    
    print(math.comb(M-1, N-1))
    
    
if __name__ == "__main__":
    main()