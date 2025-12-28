# 1094 막대기
# https://www.acmicpc.net/problem/1094
# Silver 5
# solved

def main():
    X = int(input())
    
    begin = 0
    end = 64
    cnt = 1
    
    if X == 64:
        print(1)
        return
    
    while begin < end:
        mid = (begin+end) // 2
        if mid == X:
            break
        elif mid < X:
            cnt += 1
            begin = mid
        else:
            end = mid
    print(cnt)
    
if __name__ == "__main__":
    main()