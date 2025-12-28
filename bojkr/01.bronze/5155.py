# 5155 Gadget Purchases
# https://www.acmicpc.net/problem/5155
# Bronze 2
# solved

def main():
    K = int(input())
    for _ in range(K):
        N, M = map(int, input().split())
        prices = []
        needs = [ 0 ] * M
        for m in range(M):
            prices.append(list(map(int, input().split())))
        for n in range(N):
            needs[int(input())-1] += 1
        print(f"Data Set {_ + 1}:")
        
        for m in range(M):
            u = min(needs[m], prices[m][2])
            total_cost = prices[m][0] + u * prices[m][1]
            total_revenue = u * prices[m][3]
            
            if total_revenue - total_cost > 0:
                print(m+1)
        print()
    
if __name__ == "__main__":
    main()