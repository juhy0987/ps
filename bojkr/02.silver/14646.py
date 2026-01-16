# 14646 욱제는 결정장애야!!
# https://www.acmicpc.net/problem/14646
# Silver 5
# solved

def main():
    N = int(input())
    M = list(map(int, input().split()))
    _max = -1
    
    chk = [0] * N
    cur = 0
    for m in M:
        if not chk[m-1]:
            cur += 1
            _max = max(_max, cur)
        else:
            cur -= 1
        chk[m-1] += 1
    print(_max)

if __name__ == "__main__":
    main()