# 15751 Teleportation
# https://www.acmicpc.net/problem/15751
# Bronze 3
# solved

def main():
    a, b, x, y = map(int, input().split())
    
    _a = min(a, b)
    _b = max(a, b)
    _x = min(x, y)
    _y = max(x, y)
    
    result = min(abs(_a-_x)+abs(_b-_y), _b-_a)
    print(result)

if __name__ == "__main__":
    main()