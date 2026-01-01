# 4892 숫자 맞추기 게임
# https://www.acmicpc.net/problem/4892
# Bronze 3
# solved

def solve(n0):
    return ("even", n0 // 2) if n0 % 2 == 0 else ("odd", (n0-1) // 2)

def main():
    cnt = 0
    while (_input := int(input())) != 0:
        cnt += 1
        oe, n4 = solve(_input)
        print(f"{cnt}. {oe} {n4}")

if __name__ == "__main__":
    main()