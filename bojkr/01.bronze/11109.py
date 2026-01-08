# 11109 괴짜 교수
# https://www.acmicpc.net/problem/11109
# Bronze 3
# solved

def solve(d, n, s, p):
    if d + p * n > s * n:
        print("do not parallelize")
    elif d + p * n == s * n:
        print("does not matter")
    else:
        print("parallelize")

def main():
    T = int(input())
    
    for _ in range(T):
        d, n, s, p = map(int, input().split())
        solve(d, n, s, p)
        

if __name__ == "__main__":
    main()