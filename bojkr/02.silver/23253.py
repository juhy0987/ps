# 23253 자료구조는 정말 최고야
# https://www.acmicpc.net/problem/23253
# Silver 5
# solved

import sys

def main():
    N, M = map(int, sys.stdin.readline().strip().split())
    flag = True
    for i in range(M):
        k = int(sys.stdin.readline().strip())
        kl = list(map(int, sys.stdin.readline().strip().split()))
        if flag:
            for ki in range(k-1):
                if kl[ki] < kl[ki+1]:
                    flag = False
                    break
    if flag:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()