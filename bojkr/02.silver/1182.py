# 1182 부분수열의 합
# https://www.acmicpc.net/problem/1182
# Silver 2
# solved

from itertools import combinations

def main():
    N, S = map(int, input().split())
    
    s = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N+1):
        for l in combinations(s, i):
            if sum(l) == S:
                cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()