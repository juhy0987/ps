# 5351 전투 드로이드 가격
# https://www.acmicpc.net/problem/5361
# Bronze 3
# solved

def main():
    T = int(input())

    price = [350.34, 230.90, 190.55, 125.30, 180.90]

    for _ in range(T):
        l = list(map(int, input().split()))
        result = 0
        
        for i in range(len(l)):
            result += l[i] * price[i]
        print("$%.2f" % result)

if __name__ == "__main__":
    main()