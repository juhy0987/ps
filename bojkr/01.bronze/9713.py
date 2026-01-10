# 9713 Sum of Odd Sequence
# https://www.acmicpc.net/problem/9713
# Bronze 3
# solved

def solve(N):
    return (N+1) * (N // 2 + 1) // 2

def main():
    T = int(input())
    for _ in range(T):
        print(solve(int(input())))

if __name__ == "__main__":
    main()