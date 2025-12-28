# 1072 게임
# https://www.acmicpc.net/problem/1072
# Silver 3
# solved

def main():
    X, Y = map(int, input().split())
    Z = Y * 100 // X
    cnt = 0
    if X == Y or Z == 99:
        print(-1)
        return

    cnt = ((Z+1) * X - 100 * Y) // (99 - Z)
    # print(cnt)
    if cnt * (99 - Z) < (Z+1) * X - 100 * Y:
        cnt += 1
    
    print(cnt)

if __name__ == "__main__":
    main()