# 34953 SSHS 문자열
# https://www.acmicpc.net/problem/34953
# Silver 5
# solved

def main():
  N = int(input())
  
  answer = [("H" if i % 3 == 2 else "S") for i in range(N)]
  print("".join(answer))

if __name__ == "__main__":
  main()