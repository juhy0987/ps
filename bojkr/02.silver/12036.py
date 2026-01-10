# 12036 Dance Around The Clock (Large)
# https://www.acmicpc.net/problem/12036
# Silver 2
# solved

def solve(D, K, N):
    index = -1
    if K % 2 == 0:
        index = (K-1 - 2 * N) % D
    else:
        index = (K-1 + 2 * N) % D
        
    return (index+1) % D + 1, (index-1) % D + 1
    

def main():
    T = int(input())
    
    for x in range(T):
        D, K, N = map(int, input().split())
        
        y, z = solve(D, K, N)
        print(f"Case #{x+1}: {y} {z}")

if __name__ == "__main__":
    main()