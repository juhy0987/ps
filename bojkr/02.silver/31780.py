# 31780 불사조
# https://www.acmicpc.net/problem/31780
# Silver 5
# solved

import sys

def main():
    X, M = map(int, sys.stdin.readline().strip().split())
    
    print(X * (M+1))
    

if __name__ == "__main__":
    main()