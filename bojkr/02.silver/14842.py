# 14842 재홍의 사다리
# https://www.acmicpc.net/problem/14842
# Silver 5
# solved

def main():
    W, H, N = map(int, input().split())
    
    result = 0
    for i in range(1, N):
        result += abs((N-2*i)/N) * H
    
    print("%.6f" % result)

if __name__ == "__main__":
    main()