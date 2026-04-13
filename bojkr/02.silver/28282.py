# 28282 운명
# https://www.acmicpc.net/problem/28282
# Silver 5
# solved

import sys

def main():
  data = sys.stdin.read().strip().split()
  X, K = int(data[0]), int(data[1]); data = data[2:]
  
  left = list(map(int, data[:X]))
  right = list(map(int, data[X:]))
  
  l_d, r_d = {}, {}
  for i in range(X):
    # if left[i] in l_d:
    #   l_d[left[i]] += 1
    # else:
    #   l_d[left[i]] = 1
    
    if right[i] in r_d:
      r_d[right[i]] += 1
    else:
      r_d[right[i]] = 1
  
  inter = 0
  for l in left:
    if l in r_d:
      inter += r_d[l]
  
  print(X*X - inter)

if __name__ == "__main__":
  main()