# 1026 보물
# https://www.acmicpc.net/problem/1026
# Silver 4
# solved

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A.sort()
    B.sort(reverse=True)
    result = sum(a * b for a, b in zip(A, B))
    print(result)
if __name__ == "__main__":
    main()