# 10859 뒤집어진 소수
# https://www.acmicpc.net/problem/10859
# Silver 2
# solved
# important (소수 판별 시간 최적화)

import sys
import math

def main():
    d = {
        '0': '0',
        '1': '1',
        '2': '2',
        '5': '5',
        '6': '9',
        '8': '8',
        '9': '6'
    }
    
    def is_prime(x):
        if x < 2:
            return False

        if x == 2 or x == 3:
            return True
        
        if x % 2 == 0 or x % 3 == 0:
            return False
        
        
        for i in range(5, int(math.sqrt(x))+1, 6):
            if x % i == 0 or x % (i + 2) == 0:
                return False
        return True
    
    S = sys.stdin.readline().strip()
    
    N = int(S)
    if not is_prime(N):
        print("no")
        return
    
    s = []
    for c in S:
        if (tmp := d.get(c)) is not None:
            s.insert(0, tmp)
        else:
            print("no")
            return
    
    s = "".join(s)
    n = int(s)
    if is_prime(n):
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()