# 13170 떨어진 수정
# https://www.acmicpc.net/problem/13170
# Silver 4
# solved

import sys

def main():
  data = sys.stdin.read().strip().split()
  
  N, K, P, W = map(int, data[:4])
  
  print((P + W - 1)// W)
  

if __name__ == "__main__":
  main()