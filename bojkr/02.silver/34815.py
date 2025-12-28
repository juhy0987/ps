# 34815 K + 1의 배수
# https://www.acmicpc.net/problem/34815
# Silver 3
# solved
# noticed

from itertools import combinations

def main():
    N, K = map(int, input().split())
    
    if N >= K+1:
        print("YES")
        return
    elif N == K:
        if K % 2 == 0:
            print("YES")
            return
        
    print("NO")

if __name__ == "__main__":
    main()