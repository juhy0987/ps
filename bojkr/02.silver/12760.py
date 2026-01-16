# 12760 최후의 승자는 누구?
# https://www.acmicpc.net/problem/12760
# Silver 5
# solved

def main():
    N, M = map(int, input().split())
    players = [sorted(list(map(int, input().split())), key=lambda x: -x) for _ in range(N)]
    scores = [0] * N
    
    for m in range(M):
        _max = -1
        for n in range(N):
            _max = max(_max, players[n][m])
        
        for n in range(N):
            if _max == players[n][m]:
                scores[n] += 1
    
    max_score = max(scores)
    print(" ".join([str(i+1) for i, v in enumerate(scores) if v == max_score]))

if __name__ == "__main__":
    main()