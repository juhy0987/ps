# 11608 Complexity
# https://www.acmicpc.net/problem/11608
# Bronze 2
# solved

def main():
    s = input().strip()
    q = [0] * 26
    for c in s:
        n = ord(c) - ord('a')
        q[n] += 1
    q = [n for n in q if n > 0]
    q.sort()
    
    print(sum(q[:max(0, len(q)-2)]))
    

if __name__ == "__main__":
    main()