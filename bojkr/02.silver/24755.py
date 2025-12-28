# 24755 Electron Paradox
# https://www.acmicpc.net/problem/24755
# Silver 5
# solved

def main():
    N = int(input())
    populations = list(map(int, input().split()))
    populations.sort(reverse=True)
    result = 0
    for i in range(N//2):
        result += populations[i]
    for i in range(N//2, N):
        result += populations[i] // 2
        
    print(result)
    
if __name__ == "__main__":
    main()