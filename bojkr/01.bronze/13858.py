# 13858 Reading Digits
# https://www.acmicpc.net/problem/13858
# Bronze 1
# solved

def main():
    k, pos = map(int, input().split())
    s = input()
    
    for _ in range(k):
        decoded = []
        for i in range(0, len(s)-1, 2):
            decoded.append(s[i+1] * int(s[i]))
        s = "".join(decoded)
    
    print(s[pos])

if __name__ == "__main__":
    main()