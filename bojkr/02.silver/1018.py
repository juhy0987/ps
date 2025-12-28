# 1018 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018
# Silver 3
# solved

def main():
    N, M = map(int, input().split())

    def classify(c):
        if c == 'W':
            return 1
        return 0

    def _print(board):
        for i in range(N):
            print(board[i])

    board = []
    for _ in range(N):
        board.append(list(map(classify, list(input()))))
    
    bw = [
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
    ]

    wb = [
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
    ]

    def bw_chk(n, m):
        cnt = 0
        for i in range(8):
            for j in range(8):
                if board[n+i][m+j] != bw[i][j]:
                    cnt += 1
        return cnt
    
    def wb_chk(n, m):
        cnt = 0
        for i in range(8):
            for j in range(8):
                if board[n+i][m+j] != wb[i][j]:
                    cnt += 1
        return cnt

    min_cnt = 1e9
    for n in range(N-7):
        for m in range(M-7):
            min_cnt = min(min_cnt, min(wb_chk(n, m), bw_chk(n, m)))
    print(min_cnt)

if __name__ == "__main__":
    main()