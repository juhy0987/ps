# 31826 주식 시장
# https://www.acmicpc.net/problem/31826
# Silver 3

import sys

def main():
  data = sys.stdin.read().strip().split()
  
  N = int(data[0]); data = data[1:]
  
  p_l = [0] * 13131
  cur = 10000
  for i in range(N):
    p, x, f = map(int, data[i*3:(i+1)*3])
    
    if (p_l[p] < 0 and f > 0) or (p_l[p] > 0 and f < 0):
      cur = p
      
    p_l[p] += x * f
  
  print(cur)
  

if __name__ == "__main__":
  main()