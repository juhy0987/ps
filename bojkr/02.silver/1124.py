# 1124 언더프라임
# https://www.acmicpc.net/problem/1124
# Silver 1
# solved

import math

def main():
    
    prime_set = set()

    for i in range(2, 50000):
        flag = True
        for k in range(2, int(math.sqrt(i))+1):
            if i%k == 0:
                flag = False
                break
        if flag:
            prime_set.add(i)
    
    a, b = map(int, input().split())
    cnt = 0
    for i in range(a, b+1):
        tmp = i
        
        count = 0
        for prime in prime_set:
            while tmp % prime == 0:
                tmp //= prime
                count += 1
            if tmp == 1:
                break

        if count in prime_set:
            cnt += 1
    
    print(cnt)

if __name__ == "__main__":
    main()