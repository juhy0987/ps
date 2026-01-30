# 20301 반전 요세푸스
# https://www.acmicpc.net/problem/20301
# Silver 3
# solved

def main():
    N, K, M = map(int, input().split())
    
    L = [i for i in range(1, N+1)]
    cur = -1; cnt = 0; dir = 1
    while L:
        index = (cur+K*dir) % len(L)
        print(L.pop(index))
        
        cnt = (cnt+1) % M
        if cnt == 0:
            dir *= -1
        cur = index-(1 if dir > 0 else 0)

if __name__ == "__main__":
    main()