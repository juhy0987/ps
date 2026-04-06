# 7891 Can you add this?
# https://www.acmicpc.net/problem/7891
# Bronze 5
# solved

import sys

def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        x, y = map(int, sys.stdin.readline().strip().split())
        
        print(x+y)

if __name__ == "__main__":
    main()