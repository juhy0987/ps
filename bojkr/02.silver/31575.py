# 31826 주식 시장
# https://www.acmicpc.net/problem/31826
# Silver 3
# solved

import sys
from collections import deque

def main():
  data = sys.stdin.read().strip().split()
  N = int(data[0]); M = int(data[1]); data = data[2:]
  
  m = [list(map(int, data[i*N:(i+1)*N])) for i in range(M)]
  
  d = [(1, 0), (0, 1)]
  q = deque([(0, 0)])
  visited = [[False]*N for _ in range(M)]
  while q:
    # print(q)
    cur = q.popleft()
    # print(cur)
    if cur[0] == M-1 and cur[1] == N-1:
      print("Yes")
      return
    if visited[cur[0]][cur[1]]:
      continue
    
    visited[cur[0]][cur[1]] = True
    
    for direc in d:
      _next = (cur[0]+direc[0], cur[1]+direc[1])
      # print("next:", _next)
      if _next[0] >= M or _next[1] >= N:
        continue
      
      if not visited[_next[0]][_next[1]] and m[_next[0]][_next[1]]:
        q.append(_next)

  print("No")

if __name__ == "__main__":
  main()