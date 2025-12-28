# 1051 숫자 정사각형
# https://www.acmicpc.net/problem/1051
# Silver 3
# solved

def main():
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, list(input().strip()))))
    
    max_side = min(N, M)
    for side in range(max_side, 0, -1):
        for i in range(N-side+1):
            for j in range(M-side+1):
                if board[i][j] == board[i][j+side-1] ==  board[i+side-1][j] == board[i+side-1][j+side-1]:
                    print(side * side)
                    return
if __name__ == "__main__":
    main()