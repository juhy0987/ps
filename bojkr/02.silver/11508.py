# 11508 2+1 세일
# https://www.acmicpc.net/problem/11508
# Silver 4
# solved

def main():
    n = int(input())
    c = []
    for _ in range(n):
        c.append(int(input()))
    
    c.sort()
    c.reverse()
    
    result = 0
    for i in range(0, len(c), 3):
        result += c[i]
        if i+1 < len(c):
            result += c[i+1]

    print(result)

if __name__ == "__main__":
    main()