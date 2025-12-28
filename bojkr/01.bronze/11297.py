# 11297 Cypher
# https://www.acmicpc.net/problem/11297
# Bronze 2
# solved

def main():
    while True:
        y, m, d = map(int, input().split())
        if y == 0 and m == 0 and d == 0:
            return
        s = input()
        key = (y + m + d) % 25 + 1
        
        result = []
        for c in s:
            a = ord(c)
            if a < ord('a') or a > ord('z'):
                result.append(c)
                continue
            
            a -= key
            if a < ord('a'):
                a += ord('z') - ord('a') + 1
            result.append(chr(a))
        print("".join(result))
            

if __name__ == "__main__":
    main()