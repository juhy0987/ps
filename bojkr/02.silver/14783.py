# 14783 Eenie Meenie Miney Moe
# https://www.acmicpc.net/problem/14783
# Silver 4
# solved

def main():
    N, L = map(int, input().split())
    A = list(map(int, input().split()))
    
    F = [i for i in range(1, N+1)]
    cur = -1; a = 0
    while len(F) > 1:
        index = (cur+A[a]) % len(F)
        F.pop(index)
        
        cur = index-1
        a = (a+1) % L
    print(F[0])

if __name__ == "__main__":
    main()