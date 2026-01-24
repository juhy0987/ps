# 4359 Forests
# https://www.acmicpc.net/problem/4359
# Silver 5
# solved

import sys

def main():
    P, T = map(int, input().split())
    opinions = [[False] * T for _ in range(P)]
    
    while (_input := sys.stdin.readline()):
        if len(_input) < 2:
            break
        i, j = map(int, _input.split())
        
        opinions[i-1][j-1] = True
    
    T = set()
    for v in opinions:
        T.add(tuple(v))
    print(len(T))

if __name__ == "__main__":
    main()