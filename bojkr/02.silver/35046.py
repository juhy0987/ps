# 35046 Honey Cake
# https://www.acmicpc.net/problem/35046
# Silver 3
# solved

import math

def main():
    w, h, d = list(map(int, input().split()))
    n = int(input())
    
    def div(x):
        res = []
        for i in range(1, int(math.sqrt(x))+1):
            if x % i == 0:
                res.append(i)
                if i * i != x:
                    res.append(x // i)
        return res
        
    dw = div(w); dh = div(h)
    for aw in dw:
        if n % aw != 0:
            continue
        tmp = n // aw
        for ah in dh:
            if tmp % ah != 0:
                continue
            ad = tmp // ah
            if ad >= 1 and d % ad == 0:
                print(aw-1, ah-1, ad-1)
                return
    print(-1)
    
        
if __name__ == "__main__":
    main()