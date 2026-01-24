# 21313 문어
# https://www.acmicpc.net/problem/21313
# Bronze 2
# solved

def main():
    N = int(input())
    ans = []
    
    for i in range(N):
        ans.append(str(i%2 + 1))
    
    if N % 2 == 1:
        ans[-1] = "3"
    
    print(" ".join(ans))

if __name__ == "__main__":
    main()