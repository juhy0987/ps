# 18127 모형결정
# https://www.acmicpc.net/problem/18127
# Bronze 3
# solved

def main():
    A, B = map(int, input().split())
    
    result = 0
    for i in range(B+1):
        result += (A-2) * i + 1
    print(result)

if __name__ == "__main__":
    main()