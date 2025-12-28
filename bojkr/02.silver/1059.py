# 1059 좋은 구간
# https://www.acmicpc.net/problem/1059
# Silver 4
# solved

from itertools import combinations

def main():
    L = int(input())
    S = list(map(int, input().split()))
    n = int(input())
    
    S.sort()
    begin = 51
    end = -1
    for i in range(L-1):
        if S[i] < n and S[i+1] > n:
            begin = S[i]+1
            end = S[i+1]-1
            break
    
    if 1 <= n < S[0]:
        begin = 1
        end = S[0]-1
    
    if begin >= end:
        print(0)
        return
    
    result = 0
    for b, e in combinations(range(begin, end+1), 2):
        if b <= n <= e:
            # print(f"[{b},{e}]")
            result += 1
    print(result)
    
if __name__ == "__main__":
    main()