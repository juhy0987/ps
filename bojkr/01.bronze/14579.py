# 14579 덧셈과 곱셈
# https://www.acmicpc.net/problem/14579
# Bronze 3
# solved

def main():
    a, b = map(int, input().split())

    result = 1
    for i in range(a, b+1):
        result = (result * (i * (i+1) // 2)) % 14579
    print(result)

if __name__ == "__main__":
    main()