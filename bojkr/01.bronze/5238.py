# 5238 Stacked Floating Mountains
# https://www.acmicpc.net/problem/5238
# Bronze 2
# solved

import sys

def main():
  data = sys.stdin.read().strip().split()
  N = int(data[0]); data = data[1:]
  for _ in range(N):
    K = int(data[0]); data = data[1:]
    
    q = []; flag = True
    for _ in range(K):
      cur = int(data[0]); data = data[1:]
      if flag and len(q) > 1:
        if q[0] + q[1] != cur:
          flag = False
        q.pop(0)
      q.append(cur)
    if flag:
      print("YES")
    else:
      print("NO")

if __name__ == "__main__":
  main()