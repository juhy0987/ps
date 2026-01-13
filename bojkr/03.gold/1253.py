# 1253 좋다
# https://www.acmicpc.net/problem/1253
# Gold 4
# solved

from copy import deepcopy

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    A.sort()
    d = {}
    for k in A:
        if d.get(k):
            d[k] += 1
        else:
            d[k] = 1
    # print(d)        
    
    if N <= 2:
        print(0)
        return
    
    cnt = 0
    for i in range(N):
        cp = deepcopy(A)
        cp.pop(i)
        start = 0
        end = N-2
        while start < end:
            _sum = cp[start] + cp[end]
            if _sum == A[i]:
                cnt += 1
                break
            
            if _sum < A[i]:
                start += 1
            else:
                end -= 1
    print(cnt)
    
    
if __name__ == "__main__":
    main()