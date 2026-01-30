# 2563 색종이
# https://www.acmicpc.net/problem/2563
# Silver 5
# solved

def main():
    N = int(input())
    
    g = [[False]*100 for _ in range(100)]
    for _ in range(N):
        x, y = map(int, input().split())
        for i in range(x, x+10):
            for j in range(y, y+10):
                g[i][j] = True
    
    print(sum(sum(g[i]) for i in range(100)))
        

if __name__ == "__main__":
    main()