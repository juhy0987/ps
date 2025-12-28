# 13531 인생 점수
# https://www.acmicpc.net/problem/13531
# Bronze 2
# solved

def main():
    N = int(input())

    for _ in range(N):
        s = input()
        _sum = 0
        for c in s:
            tmp = ord(c)
            if tmp >= ord('A') and tmp <= ord('Z'):
                tmp -= ord('A') - 1
            else:
                continue
            _sum += tmp
        if _sum == 100:
            print("PERFECT LIFE")
        else:
            print(_sum)

if __name__ == "__main__":
    main()