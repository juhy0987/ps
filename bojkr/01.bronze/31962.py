# 31962 등교
# https://www.acmicpc.net/problem/31962
# Bronze 4
# solved

def main():
    N, X = map(int, input().split())
    bus = [list(map(int, input().split())) for _ in range(N)]
    
    bus = [(S, S+T) for S, T in bus]
    s = -1
    for start, duration in bus:
        if duration <= X and start > s:
            s = start
    print(s)

if __name__ == "__main__":
    main()