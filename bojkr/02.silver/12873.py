# 12873 기념품
# https://www.acmicpc.net/problem/12873
# Silver 3
# solved

def main():
    N = int(input())
    L = [i+1 for i in range(N)]
    cur = 0
    for i in range(1, N):
        index = (cur + i ** 3 - 1) % len(L)
        L.pop(index)
        cur = index % len(L)
        # print(index, cur, L)
    print(L[0])

if __name__ == "__main__":
    main()