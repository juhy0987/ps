# 6974 Long Division
# https://www.acmicpc.net/problem/6974
# Bronze 3
# solved

def main():
    N = int(input())
    for _ in range(N):
        base = int(input())
        div = int(input())
        
        print(base // div)
        print(base % div)
        print()
    
if __name__ == "__main__":
    main()