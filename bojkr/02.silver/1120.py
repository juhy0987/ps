# 1120 문자열
# https://www.acmicpc.net/problem/1120
# Silver 4
# solved

def main():
    X, Y = input().split()
    l_x = len(X)
    l_y = len(Y)
    
    _min = 1e9
    for x in range(l_y-l_x+1):
        cnt = 0
        for i in range(l_x):
            if X[i] != Y[i+x]:
                cnt += 1
        if _min > cnt:
            _min = cnt
    print(_min)
    
if __name__ == "__main__":
    main()