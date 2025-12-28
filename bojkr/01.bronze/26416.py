# 26416 New Password
# https://www.acmicpc.net/problem/26416
# Bronze 2
# solved

def main():
    T = int(input())
    for t in range(T):
        n = int(input())
        s = input()
        
        isdigit = False
        islower = False
        isupper = False
        isspecial = False
        
        for c in s:
            a = ord(c)
            if a >= ord('0') and a <= ord('9'):
                isdigit = True
            elif a >= ord('a') and a <= ord('z'):
                islower = True
            elif a >= ord('A') and a <= ord('Z'):
                isupper = True
            elif c in ['#', '@', '*', '&']:
                isspecial = True
        
        if not isdigit:
            s += '1'
        if not islower:
            s += 'a'
        if not isupper:
            s += 'A'
        if not isspecial:
            s += '@'
        if len(s) < 7:
            s += '1' * (7-len(s))

        print(f"Case #{t+1}:", s)

if __name__ == "__main__":
    main()