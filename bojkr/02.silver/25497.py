# 25497 기술 연계마스터 임스
# https://www.acmicpc.net/problem/25497
# Silver 4
# solved

import sys

def main():
    N = int(sys.stdin.readline().strip())
    C = sys.stdin.readline().strip()
    
    L = 0; S = 0
    cnt = 0
    for c in C:
        if c in "123456789":
           cnt += 1
        elif c == "L":
            L += 1
        elif c == "S":
            S += 1
        elif c == "R":
            if L:
                cnt += 1
                L -= 1
            else:
                break
        elif c == "K":
            if S:
                cnt += 1
                S -= 1
            else:
                break
    print(cnt)
                 

if __name__ == "__main__":
    main()