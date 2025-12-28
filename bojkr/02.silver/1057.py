# 1057 토너먼트
# https://www.acmicpc.net/problem/1057
# Silver 4
# solved

import math

def main():
    N, a, b = map(int, input().split())
    a -= 1
    b -= 1
    cnt = 0
    while cnt < math.log(N, 2) + 1:
        cnt += 1
        
        a //= 2
        b //= 2
        if a == b:
            print(cnt)
            return
    print(-1)
        
    
if __name__ == "__main__":
    main()