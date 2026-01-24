# 12971 숫자 놀이
# https://www.acmicpc.net/problem/12971
# Silver 4
# solved

def main():
    P1, P2, P3, X1, X2, X3 = map(int, input().split())
    
    def chk(N):
        return N % P1 == X1 and N % P2 == X2 and N % P3 == X3
    
    for i in range(1, P1*P2*P3+1):
        if chk(i):
            print(i)
            return
    
    print(-1)

if __name__ == "__main__":
    main()