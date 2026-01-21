# 20254 Site Score
# https://www.acmicpc.net/problem/20254
# Bronze 5

def main():
    UR, TR, UO, TO = map(int, input().split())
    
    print(56*UR + 24*TR + 14*UO + 6*TO)

if __name__ == "__main__":
    main()