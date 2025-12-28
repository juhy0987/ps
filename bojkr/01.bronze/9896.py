# 9896 Gray
# https://www.acmicpc.net/problem/9896
# Bronze 2

def main():
    n = int(input())
    s = [bool(c == '1') for c in input()]
    result = [s[0]]
    for i in range(1, n):
        result.append(s[i-1] ^ s[i])
    print("".join(map(lambda x: "1" if x else "0", result)))
        

if __name__ == "__main__":
    main()