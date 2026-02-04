# 27918 탁구 경기
# https://www.acmicpc.net/problem/27918
# Bronze 4
# solved

import sys

def main():
    N = int(sys.stdin.readline().strip())
    
    D, P = 0, 0
    flag = False
    for _ in range(N):
        tmp = sys.stdin.readline().strip()
        if flag:
            continue
        
        if tmp == 'D':
            D += 1
        else:
            P += 1
        if abs(D-P) >= 2:
            break
    print(f"{D}:{P}")

if __name__ == "__main__":
    main()