# 34723 피막치
# https://www.acmicpc.net/problem/34723
# Bronze 3
# solved

import sys

def main():
    P, M, C = map(int, sys.stdin.readline().strip().split())
    X = int(sys.stdin.readline().strip())
    
    _min = 1e9
    for p in range(1, P+1):
        for m in range(1, M+1):
            for c in range(1, C+1):
                _min = min(_min, abs((p+m)*(m+c)-X))
    print(_min)

if __name__ == "__main__":
    main()