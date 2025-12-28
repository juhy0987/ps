# 31561 시계탑
# https://www.acmicpc.net/problem/31561
# Bronze 3
# solved: 25.11.28 23:36

def main():
    m = int(input())

    if m <= 30:
        print("%.1f" % (m / 2))
    else:
        print("%.1f" % ((m - 30) * 3 / 2 + 15))

if __name__ == "__main__":
    main()