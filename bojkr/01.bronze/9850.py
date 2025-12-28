# 9850 Cipher
# https://www.acmicpc.net/problem/9850
# Bronze 1
# solved

def main():
    s = input()
    for shift in range(0, 26):
        src = ""
        for c in s:
            n = ord(c)-ord('A')
            if n < 0 or n > 25:
                src = src + c
            else:
                src = src + chr((n+shift) % 26 + ord('A'))
        
        if src.find("LIVE") > -1 and src.find("CHIPMUNKS") > -1:
            print(src)
            return

if __name__ == "__main__":
    main()