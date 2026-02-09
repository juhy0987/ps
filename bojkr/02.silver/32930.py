# 32930 슈팅 연습
# https://www.acmicpc.net/problem/32930
# Silver 5
# solved

import sys
import heapq

def main():
    N, M = map(int, sys.stdin.readline().strip().split())
    
    def dis_sq(src, dst):
        return (src[0]-dst[0]) ** 2 + (src[1]-dst[1]) ** 2
    
    targets = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    add_targets = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
    
    cur = [0, 0]
    result = 0
    cnt = 0
    while targets and cnt < M:
        index = -1; max_dis = -1
        for i, dst in enumerate(targets):
            if (tmp := dis_sq(cur, dst)) > max_dis:
                max_dis = tmp
                index = i
        result += max_dis
        cur = targets.pop(index)
        # print(cur, result)
        
        if add_targets:
            targets.append(add_targets.pop(0))
        cnt += 1
    
    print(result)
    

if __name__ == "__main__":
    main()