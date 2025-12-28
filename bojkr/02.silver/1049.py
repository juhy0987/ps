# 1049 기타줄
# https://www.acmicpc.net/problem/1049
# Silver 4
# solved

def main():
    N, M = map(int, input().split())
    min_package_price = 1e9
    min_single_price = 1e9
    
    for _ in range(M):
        package_price, single_price = map(int, input().split())
        min_package_price = min(min_package_price, package_price)
        min_single_price = min(min_single_price, single_price)
    
    total = 0
    if min_single_price * 6 <= min_package_price:
        total = N * min_single_price
    else:
        total += (N // 6) * min_package_price
        total += min((N % 6) * min_single_price, min_package_price)
    
    print(total)
    
if __name__ == "__main__":
    main()