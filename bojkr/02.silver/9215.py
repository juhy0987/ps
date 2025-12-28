# 9215 신나는 분수 계산
# https://www.acmicpc.net/problem/9215
# Silver 3
# solved

def main():
    cnt = 0
    
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a%b)
    
    while True:
        N = int(input())
        if N == 0:
            break
        cnt += 1
        
        w = 0
        n = 0
        d = 1
        for _ in range(N):
            tmp = input().split(',')
            if len(tmp) > 1:
                w += int(tmp[0])
                tmp = tmp[1]
            else:
                tmp = tmp[0]
            tmp = tmp.split('/')
            
            if len(tmp) > 1:
                tmp_n, tmp_d = map(int, tmp)
                n = n * tmp_d + tmp_n * d
                d *= tmp_d
            else:
                w += int(tmp[0])
            
            while n >= d:
                n -= d
                w += 1
            
            if n > 0:
                div = gcd(n, d)
                n //= div
                d //= div
            else:
                d = 1
        
        print(f"Test {cnt}: ", end="")
        
        if w:
            print(w, end="")
        if n:
            if w:
                print(",", end="")
            print(f"{n}/{d}", end="")
        if not w and not n:
            print(0, end="")
        print()
    
if __name__ == "__main__":
    main()