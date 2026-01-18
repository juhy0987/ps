# 2668 숫자고르기
# https://www.acmicpc.net/problem/2668
# Gold 5
# solved

from itertools import combinations

def main():
    N = int(input())
    A = [(i+1, int(input())) for i in range(N)]
    targeted = [0] * N
    visited = [False] * N
    
    for i, target in A:
        targeted[target-1] += 1
    
    q = []
    for i in range(N):
        if not targeted[i]:
            q.append(i)
    # print(q)
    
    while q:
        cur = q.pop(0)
        targeted[cur] -= 1
        
        # print("cur:", cur+1, targeted)
        if targeted[cur] > 0 or visited[cur]:
            continue
        visited[cur] = True
        
        if not visited[A[cur][1]-1]:
            q.append(A[cur][1]-1)
        
    result = [i+1 for i, v in enumerate(targeted) if v > 0]
    print(len(result))
    for tmp in result:
        print(tmp)
    
if __name__ == "__main__":
    main()