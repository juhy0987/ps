# 24523 내 뒤에 나와 다른 수
# https://www.acmicpc.net/problem/24523
# Silver 2
# solved

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    chk = [False] * N
    for i in range(N-1):
        if A[i] == A[i+1]:
            chk[i] = True
    
    result = []
    cur = 0
    cnt = 0
    while cur < N-1:
        if not chk[cur]:
            result += [str(cur+2)] * (cnt+1)
            cnt = 0
        else:
            cnt += 1
        cur += 1
    result += [str(-1)] * (cnt+1)
    print(" ".join(result))

if __name__ == "__main__":
    main()