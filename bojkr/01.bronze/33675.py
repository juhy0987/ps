# 33675 L-트로미노 타일링
# https://www.acmicpc.net/problem/33675
# Bronze 1
# solved

def solve(N):
    if N % 2 == 1:
        return 0
    
    return 2 ** (N // 2)

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))
    
if __name__ == "__main__":
    main()