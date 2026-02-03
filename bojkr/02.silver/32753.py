# 32753 네 또 수열입니다
# https://www.acmicpc.net/problem/32753
# Silver 4
# solved

import sys

def main():
    N, K = map(int, sys.stdin.readline().strip().split())
    
    
    if N > 1:
        if N == 2 and K == 1:
            print("1 2")
        else:
            print(-1)
        return
    
    print(" ".join(["1"] * K))

if __name__ == "__main__":
    main()