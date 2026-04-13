# 28431 양말 짝 맞추기
# https://www.acmicpc.net/problem/28431
# Bronze 4
# solved

import sys

def main():
  data = sys.stdin.read().strip().split()
  socks = set()
  for s in data:
    if s in socks:
      socks.remove(s)
    else:
      socks.add(s)
    
  print(list(socks)[0])
  

if __name__ == "__main__":
  main()