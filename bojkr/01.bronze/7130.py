# 7130 Milk and Honey
# https://www.acmicpc.net/problem/7130
# Bronze 3
# solved

def main():
    M, H = map(int, input().split())
    
    N = int(input())
    result = 0
    for _ in range(N):
        C, B = map(int, input().split())
        result += max(C*M, B*H)
    print(result)
    
    
    
if __name__ == "__main__":
    main()