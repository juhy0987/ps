# 1183 약속
# https://www.acmicpc.net/problem/1183
# Silver 2
# solved

def main():
    N = int(input())

    l = []
    for _ in range(N):
        A, B = map(int, input().split())
        T = -(A-B)
        l.append(T)
    l.sort()
    if N % 2 == 1:
        print(1)
    else:
        print(l[N//2] - l[N//2-1] + 1)

if __name__ == "__main__":
    main()