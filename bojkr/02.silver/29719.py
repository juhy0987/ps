# 29719 브실이의 불침번 근무
# https://www.acmicpc.net/problem/29719
# Silver 4
# solved

import math

def main():
    N, M = map(int, input().split())
    
    a = 1
    for _ in range(N):
        a *= M
        a %= 1000000007
    b = 1
    for _ in range(N):
        b *= M-1
        b %= 1000000007
    
    print((a-b) % 1000000007)

if __name__ == "__main__":
    main()