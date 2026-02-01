# 26170 사과 빨리 먹기
# https://www.acmicpc.net/problem/26170
# Silver 2
# solved

import sys
from copy import deepcopy

def main():
    board = [
        list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)
    ]
    R, C = map(int, sys.stdin.readline().strip().split())
    _min = -1
    
    q = [(R, C, board, 3, 0)]; dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        r,c, cur_board, rest, mv = q.pop(0)
        
        if cur_board[r][c] == 1:
            rest -= 1
        if rest <= 0:
            _min = mv
            break
        cur_board[r][c] = -1
        
        for d in dir:
            tmp_r = r+d[0]; tmp_c = c+d[1]
            if tmp_r < 0 or tmp_r > 4 or tmp_c < 0 or tmp_c > 4:
                continue
            
            if cur_board[r+d[0]][c+d[1]] < 0:
                continue
            q.append((r+d[0], c+d[1], deepcopy(cur_board), rest, mv+1))        
        
    print(_min)

if __name__ == "__main__":
    main()