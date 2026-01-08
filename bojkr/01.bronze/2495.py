# 2495 연속구간
# https://www.acmicpc.net/problem/2495
# Bronze 2
# solved

def main():
    for _ in range(3):
        _max = 1
        s = input()
        pre = s[0]
        cnt = 1
        for c in s[1:]:
            if pre == c:
                cnt += 1
            else:
                _max = max(cnt, _max)
                cnt = 1
                pre = c
        _max = max(cnt, _max)
        print(_max)

if __name__ == "__main__":
    main()