# 1064 평행사변형
# https://www.acmicpc.net/problem/1064
# Silver 4
# solved

import math

def main():
    xa, ya, xb, yb, xc, yc = map(int, input().split())
    
    _ab = [xb-xa, yb-ya]
    _bc = [xc-xb, yc-yb]
    _ca = [xa-xc, ya-yc]
    
    if _ab[0] * _bc[1] == _bc[0] * _ab[1] \
        or _bc[0] * _ca[1] == _ca[0] * _bc[1] \
            or _ca[0] * _ab[1] == _ab[0] * _ca[1]:
        print(float(-1))
        return
    
    ab = math.sqrt(_ab[0]**2 + _ab[1]**2)
    bc = math.sqrt(_bc[0]**2 + _bc[1]**2)
    ca = math.sqrt(_ca[0]**2 + _ca[1]**2)
    
    _max = max(ab, bc, ca)
    _min = min(ab, bc, ca)
    tmp = [ab, bc, ca]
    tmp.remove(_max)
    tmp.remove(_min)
    _mid = tmp[0]
    
    print(abs(_max-_min) * 2)
    
if __name__ == "__main__":
    main()