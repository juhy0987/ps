# 1244 스위치 켜고 끄기
# https://www.acmicpc.net/problem/1244
# Silver 4
# solved

def main():
    N = int(input())
    switches = list(map(int, input().split()))
    
    M = int(input())
    students = [list(map(int, input().split())) for _ in range(M)]
    
    for s, n in students:
        s = s-1
        if not s:
            for i in range(n-1, N, n):
                switches[i] ^= 1
        else:
            start = n-1
            end = n-1
            while start > 0 and end < N-1 and switches[start] == switches[end]:
                start -= 1
                end += 1
            if switches[start] != switches[end]:
                start += 1
                end -= 1
            for i in range(start, end+1):
                switches[i] ^= 1
        
        # print(" ".join([str(i) for i in switches]))
    for r in range(N // 20+1):
        print(" ".join([str(i) for i in switches[r * 20:min((r+1) * 20, N)]]))

if __name__ == "__main__":
    main()