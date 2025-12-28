"""
https://www.acmicpc.net/problem/12865
평범한 배낭 : gold 5
"""

def main():
    n, k = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (k + 1)
    for item in items:
        for i in range(k, item[0] - 1, -1):
            dp[i] = max(dp[i], dp[i - item[0]] + item[1])
    print(dp[k])

if __name__ == "__main__":
    main()