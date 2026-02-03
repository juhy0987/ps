# 17090 미로 탈출하기
# https://www.acmicpc.net/problem/17090
# Gold 3
# solved

import sys

def main():
    N, M = map(int, sys.stdin.readline().strip().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(N)]
    
    is_visited = [[False] * M for _ in range(N)]
    chk = [[False] * M for _ in range(N)]
    
    def m(r, c):
        q = []
        while r >= 0 and r <  N and c >= 0 and c < M:
            if is_visited[r][c]:
                for target_r, target_c in q:
                    chk[target_r][target_c] = chk[r][c]
                return
            # print(r,c)
            is_visited[r][c] = True
            q.append((r, c))
            
            if board[r][c] == 'U':
                r -= 1
            elif board[r][c] == 'R':
                c += 1
            elif board[r][c] == 'D':
                r += 1
            elif board[r][c] == 'L':
                c -= 1
        
        for target_r, target_c in q:
            chk[target_r][target_c] = True
    
    for r in range(N):
        for c in range(M):
            if is_visited[r][c]:
                continue
            
            m(r, c)

    # for i in range(N):
    #     print(is_visited[i])

    # for i in range(N):
    #     print(chk[i])

    print(sum([chk[i].count(True) for i in range(N)]))

if __name__ == "__main__":
    main()