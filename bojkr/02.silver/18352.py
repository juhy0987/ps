# 18352 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352
# Silver 2
# solved

import sys
from collections import deque

def main():
  data = sys.stdin.read().split()
  N, M, K, X = map(int, data[:4])
  
  graph = [[] for _ in range(N+1)]
  ptr = 4
  for m in range(M):
    a, b = map(int, data[ptr:ptr+2])
    
    graph[a].append(b)
    ptr += 2
    
  dis = [-1] * (N+1)
  dis[X] = 0
  
  q = deque([X])
  while q:
    cur = q.popleft()
    if dis[cur] == K:
      continue
    
    for b in graph[cur]:
      if dis[b] < 0:
        dis[b] = dis[cur] + 1
        q.append(b)
  
  flag = True
  for i, v in enumerate(dis):
    if v == K:
      print(i)
      flag = False
        
  if flag:
    print(-1)

if __name__ == "__main__":
  main()