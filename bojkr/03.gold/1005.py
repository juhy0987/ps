"""
https://www.acmicpc.net/problem/1005
ACM Craft : gold 3
"""

def solve():
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    order = {}
    for _ in range(k):
        x, y = map(int, input().split())
        if y-1 in order:
            order[y-1].append(x-1)
        else:
            order[y-1] = [x-1]
    w = int(input())
    
    dp = [-1] * n
    
    def dfs(x):
        if dp[x] != -1:
            return dp[x]
        
        if x not in order:
            dp[x] = d[x]
            return dp[x]
        
        max_time = 0
        for prereq in order[x]:
            time = dfs(prereq)
            if time > max_time:
                max_time = time
        
        dp[x] = max_time + d[x]
        return dp[x]
    print(dfs(w-1))
    

def main():
    t = int(input())
    
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()