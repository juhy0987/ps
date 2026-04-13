# 13462 Battle Simulation
# https://www.acmicpc.net/problem/13462
# Bronze 2
# solved

import sys

def main():
  data = sys.stdin.read().strip()
  answer = []
  
  cur = 0
  while cur < len(data):
    if cur+2 < len(data):
      if len(set(data[cur:cur+3])) == 3:
        answer.append("C")
        cur += 3
        continue
    
    if data[cur] == 'R':
      answer.append('S')
    elif data[cur] == 'B':
      answer.append('K')
    else:
      answer.append('H')
    
    cur += 1
  print("".join(answer))

if __name__ == "__main__":
  main()