# 1037 약수
# https://www.acmicpc.net/problem/1037
# Bronze 1
# solved

def main():
    N = int(input())
    L = list(map(int, input().split()))
    
    print(max(L) * min(L))
    
    
if __name__ == "__main__":
    main()