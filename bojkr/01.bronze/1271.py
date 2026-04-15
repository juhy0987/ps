# 1271 엄청난 부자2
# https://www.acmicpc.net/problem/1271
# Bronze 5
# solved

def main():
  n, m = map(int, input().split())
  
  print(n//m)
  print(n%m)

if __name__ == "__main__":
  main()