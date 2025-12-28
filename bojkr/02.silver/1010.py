# 1010 다리 놓기
# https://www.acmicpc.net/problem/1010
# Silver 5
# solved

def main():
    T = int(input())

    def combination(m, n):
        result = 1
        for i in range(n+1, m+1):
            result *= i
        for i in range(2, m-n+1):
            result //= i

        return result
    
    for _ in range(T):
        N, M = map(int, input().split())

        if N == M:
            print(1)
            continue

        print(combination(M, N))


if __name__ == "__main__":
    main()