# 1007 벡터 매칭
# https://www.acmicpc.net/problem/1007
# Gold 2

import math
from itertools import combinations

def main():
    T = int(input())
    for t in range(T):
        n = int(input())
        pos = []
        sum_x = 0
        sum_y = 0
        for _ in range(n):
            a, b = map(int, input().split())
            sum_x += a
            sum_y += b
            pos.append([a, b])
        initial = list(combinations(pos, n // 2))
        answer = 1e9

        for init_pos in initial:
            init_pos = list(init_pos)
            init_x, init_y = 0, 0
            for pos in init_pos:
                init_x += pos[0]
                init_y += pos[1]
            ter_x, ter_y = sum_x - init_x, sum_y - init_y
            answer = min(answer, math.sqrt((ter_x - init_x) ** 2 + (ter_y - init_y) ** 2))
        print(answer)
        
        

if __name__ == "__main__":
    main()