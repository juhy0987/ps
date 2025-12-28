# 1198 삼각형으로 자르기
# https://www.acmicpc.net/problem/1198
# Silver 2
# solved

import math
from itertools import combinations

def main():
    N = int(input())
    
    _max = -1
    pnt = []
    for _ in range(N):
        pnt.append(tuple(map(int, input().split())))
    
    for x, y, z in combinations(pnt, 3):
        a = (y[0]-x[0], y[1]-x[1])
        b = (z[0]-x[0], z[1]-x[1])
        _max = max(_max, abs(a[0]*b[1] - a[1]*b[0]) / 2)
    print(_max)
    
if __name__ == "__main__":
    main()