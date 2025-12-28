# 1189 컴백홈
# https://www.acmicpc.net/problem/1189
# Silver 1
# solved

from copy import deepcopy

def main():
    R, C, K = map(int, input().split())

    board = []
    for _ in range(R):
        row = []
        _input = input()
        for c in _input:
            if c == 'T':
                row.append(1)
            else:
                row.append(0)
        board.append(row)
    board.reverse()
    
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    cnt = 0
    q = [(0, 0, set([(0, 0)]))]
    while q:
        cur = q.pop(0)
        pos = cur[0], cur[1]
        history = cur[2]
        
        # print(pos, history)
        if board[pos[0]][pos[1]]:
            continue
        
        if pos == (R-1, C-1):
            if len(history) == K:
                cnt += 1
            continue
        
        for d in directions:
            _next_pos = (pos[0] + d[0], pos[1] + d[1])
            if _next_pos[0] < 0  or _next_pos[0] > R-1 \
                or _next_pos[1] < 0 or _next_pos[1] > C-1:
                continue
            if _next_pos in history:
                continue
            if board[_next_pos[0]][_next_pos[1]]:
                continue
            _next_history = deepcopy(history)
            _next_history.add(_next_pos)
            q.append((_next_pos[0], _next_pos[1], _next_history))
    print(cnt)
    
if __name__ == "__main__":
    main()