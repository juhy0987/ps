# 1205 등수 구하기
# https://www.acmicpc.net/problem/1205
# Silver 4
# solved

def main():
    N, n, P = map(int, input().split())
    
    if N == 0:
        print(1)
        return
    
    scores = list(map(int, input().split()))
    
    if N == P and scores[-1] >= n:
        print(-1)
        return
    
    rank = 1
    for s in scores:
        if s > n:
            rank += 1
        else:
            break
    print(rank)
    
if __name__ == "__main__":
    main()