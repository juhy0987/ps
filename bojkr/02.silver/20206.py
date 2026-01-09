# 20206 푸앙이가 길을 건너간 이유
# https://www.acmicpc.net/problem/20206
# Silver 1
# solved

def main():
    A, B, C = map(int, input().split())
    X1, X2, Y1, Y2 = map(int, input().split())
    
    if A == 0:
        if Y1 < -C / B < Y2:
            print("Poor")
        else:
            print("Lucky")
        return
    
    if B == 0:
        if X1 < -C / A < X2:
            print("Poor")
        else:
            print("Lucky")
        return
    
    begin = (-A * X1 - C) / B
    end = (-A * X2 - C) / B
    
    begin = 1 if begin >= Y2 else -1 if begin <= Y1 else 0
    end = 1 if end >= Y2 else -1 if end <= Y1 else 0
    
    if not begin or not end or begin != end:
        print("Poor")
    else:
        print("Lucky")

if __name__ == "__main__":
    main()