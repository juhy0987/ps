# 25704 출석 이벤트
# https://www.acmicpc.net/problem/25704
# Bronze 4
# solved

def main():
    N = int(input())
    P = int(input())
    
    _min = P
    if N >= 5:
        _min = min(_min, P - 500)
    if N >= 10:
        _min = min(_min, P * 90 / 100)
    if N >= 15:
        _min = min(_min, P - 2000)
    if N >= 20:
        _min = min(_min, P * 75 / 100)
    
    print(int(max(_min, 0)))

if __name__ == "__main__":
    main()