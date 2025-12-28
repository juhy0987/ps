# 9237 이장님 초대
# https://www.acmicpc.net/problem/9237
# Silver 5
# solved

def main():
    N = int(input())
    t = list(map(int, input().split()))
    t.sort(reverse=True)
    for i in range(N):
        t[i] += i
    print(max(t) + 2)
    
if __name__ == "__main__":
    main()