# 1138 한 줄로 서기
# https://www.acmicpc.net/problem/1138
# Silver 2
# solved

def main():
    N = int(input())
    l = list(map(int, input().split()))
    
    result = []
    for i in range(N-1, -1, -1):
        result.insert(l[i], i+1)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()