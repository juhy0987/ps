# 19699 소-난다!
# https://www.acmicpc.net/problem/19699
# Silver 2
# important (정렬 순서 차이에 따른 결과 차이)
# 문자열 정렬 vs 숫자 정렬

import sys
import math
from itertools import combinations

def main():
    N, M = map(int, sys.stdin.readline().strip().split())
    H = list(map(int, sys.stdin.readline().strip().split()))
    
    def is_prime(x):
        if x < 2:
            return False
        if x == 2 or x == 3:
            return True
        if x % 2 == 0 or x % 3 == 0:
            return False
        
        for i in range(5, int(math.sqrt(x))+1, 6):
            if x % i == 0 or x % (i+2) == 0:
                return False
        return True
    
    result = set()
    for v in combinations(H, M):
        if is_prime(tmp := sum(v)):
            result.add(tmp)
    
    if not len(result):
        print(-1)
    else:
        print(" ".join([str(n) for n in sorted(list(result))]))

if __name__ == "__main__":
    main()