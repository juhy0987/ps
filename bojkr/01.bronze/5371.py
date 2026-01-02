# 5371 Annoying Mosquitos
# https://www.acmicpc.net/problem/5371
# Bronze 1
# solved

import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for t in range(T):
        n = int(input())
        mosquitos = [list(map(int, input().split())) for i in range(n)]
        cnt = [False] * n
        m = int(input())
        
        for _ in range(m):
            x, y = map(int, input().split())
            for i in range(len(mosquitos)):
                if abs(mosquitos[i][0] - x) <= 50 and abs(mosquitos[i][1] - y) <= 50:
                    cnt[i] = True
                    
    
        print(cnt.count(True))

if __name__ == "__main__":
    main()