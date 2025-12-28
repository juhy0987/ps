# 3787 Count on Canton
# https://www.acmicpc.net/problem/3787
# Silver 5
# solved

import sys

def main():
    while True:
        try:
            n_str = sys.stdin.readline()
            if not n_str:
                break
            n = int(n_str) - 1
        except (IOError, ValueError):
            break
        # n = int(_input) - 1
        
        _sum = 0
        gap = -1
        for i in range(1, 10**7):
            if _sum <= n and n < _sum + i:
                _sum += i
                gap = i
                break
            _sum += i
        
        a, b = 0, 0
        if gap % 2 == 0:
            b = _sum - n
            a = gap - b + 1
        else:
            a = _sum - n
            b = gap - a + 1
        
        print(f"TERM {n+1} IS {a}/{b}")

if __name__ == "__main__":
    main()