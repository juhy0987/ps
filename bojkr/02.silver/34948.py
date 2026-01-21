# 34948 초콜릿 합치기
# https://www.acmicpc.net/problem/34948
# Silver 3
# solved

def main():
    N = int(input())
    H = list(map(int, input().split()))
    W = list(map(int, input().split()))
    
    ch = sorted([(h, w) for h, w in zip(H, W)], key=lambda x: x[0])
    
    sum_w = 0
    ans = 0
    
    for i in range(N-1, -1, -1):
        h, w = ch[i]
        sum_w += w
        area = h * sum_w
        if area > ans:
            ans = area
    print(ans)
    


if __name__ == "__main__":
    main()