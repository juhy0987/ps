# 32776 가희와 4시간의 벽 2
# https://www.acmicpc.net/problem/32776
# Bronze 4
# solved

def main():
    Sab = int(input())
    Ma, Fab, Mb = map(int, input().split())
    
    if Sab <= 60 * 4:
        print("high speed rail")
        return
    
    if Sab <= Ma + Fab + Mb:
        print("high speed rail")
        return
    
    print("flight")

if __name__ == "__main__":
    main()