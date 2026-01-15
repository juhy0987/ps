# 12540 Investing at the Market (Large)
# https://www.acmicpc.net/problem/12540
# Bronze 1
# solved

def main():
    N = int(input())
    for x in range(N):
        M = int(input())
        P = list(map(int, input().split()))
        
        result = 0
        index = [-1, -1]
        
        for i in range(len(P)-1):
            for j in range(i+1, len(P)):
                if P[i] > M:
                    continue
                profit = (M // P[i]) * (P[j]-P[i])
                if profit > result or \
                    (profit == result and index[0] < P[i]):
                    result = profit
                    index = [i, j]
        
        if not result:
            print(f"Case #{x+1}: IMPOSSIBLE")
        else:
            print(f"Case #{x+1}: {index[0]+1} {index[1]+1} {result}")
                

if __name__ == "__main__":
    main()