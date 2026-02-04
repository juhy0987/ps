# 11944 NN
# https://www.acmicpc.net/problem/11944
# Bronze 2
# solved

import sys

def main():
    N, M = map(int, sys.stdin.readline().strip().split())
    
    S = str(N)
    length = min(N * len(S), M)
    
    if length == M and length % len(S) > 0:
        print(S*(M // len(S)) + S[:M % len(S)])
    else:
        print(S * (length // len(S)))

if __name__ == "__main__":
    main()