# 34850 포도주 상인
# https://www.acmicpc.net/problem/34850
# Bronze 1
# solved

def main():
    x, y, p, a, b = map(int, input().split())
    
    start = p + (y-1)*b
    last = start - (x-1)*a
    print((start+last) * x // 2)
    
if __name__ == "__main__":
    main()