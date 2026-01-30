# 16521 A symmetrical Pizza
# https://www.acmicpc.net/problem/16521
# Silver 3
# solved
# important (부동 소수점 표현에 따른 테스트 케이스 차이)

def main():
    R = int(input().strip().replace('.', ''))
    
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    criteria = 36000    
    print(criteria // gcd(criteria, R))

if __name__ == "__main__":
    main()