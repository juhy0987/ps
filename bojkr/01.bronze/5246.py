# 5246 Checkerboard Rows
# https://www.acmicpc.net/problem/5246
# Bronze 3
# solved

import sys

def main():
  data = sys.stdin.read().strip().split()
  K = int(data[0]); data = data[1:]
  for _ in range(K):
    n = int(data[0]); data = data[1:]
    l = data[:2*n]; data = data[2*n:]
    cnt = [0]*8
    for i in range(n):
      cnt[int(l[2*i+1])-1] += 1
    print(max(enumerate(cnt), key=lambda x: x[1])[1])

if __name__ == '__main__':
  main()