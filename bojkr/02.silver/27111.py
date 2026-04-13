# 27111 출입 기록
# https://www.acmicpc.net/problem/27111
# Silver 5
# solved

import sys

def main():
  data = sys.stdin.read().strip().split()
  N = int(data[0]); data = data[1:]
  
  answer = 0
  report = set()
  for i in range(0, len(data), 2):
    a, b = int(data[i]), int(data[i+1])
    
    if b:
      if a in report:
        answer += 1
      else:
        report.add(a)
    else:
      if not a in report:
        answer += 1
      else:
        report.remove(a)
  answer += len(report)
  print(answer)

if __name__ == "__main__":
  main()