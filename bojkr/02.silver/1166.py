# 1166 선물
# https://www.acmicpc.net/problem/1166
# Silver 3
# solved

import math

def main():
    N, L, W, H = map(int, input().split())
    
    start = 0
    end = min(L, W, H)
    mid = 0
    for _ in range(10000):
        mid = (start + end) / 2
        l = L // mid
        w = W // mid
        h = H // mid
        
        if l * w * h < N:
            end = mid
        else:
            start = mid
    print(start)

if __name__ == "__main__":
    main()