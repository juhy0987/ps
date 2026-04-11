# 67259 경주로 건설
# https://school.programmers.co.kr/learn/courses/30/lessons/67259
# level 3
# bfs + heap + dp

import heapq

def solution(board):
    N = len(board)
    
    direc = [(1, 0), (0, 1), (0, -1), (-1, 0),]
    def chk(i, j):
        if i[0]+i[1] == 0:
            return False
        return abs(i[0]) != abs(j[0])
    
    q = []
    heapq.heappush(q, (0, 0, 0, (1, 0)))
    heapq.heappush(q, (0, 0, 0, (0, 1)))
    bill_board = [[{di: 1e9 for di in direc} for _ in range(N)] for _ in range(N)]
    for di in direc:
        bill_board[0][0][di] = 0
    while q:
        bill, x, y, d = heapq.heappop(q)
        # print(bill, x, y, d)
        
        for di in direc:
            nx, ny = x+di[0], y+di[1]
            if nx >= N or ny >= N or nx < 0 or ny < 0:
                continue
            if board[nx][ny]:
                continue
            
            _next_bill = bill + 100 + (500 if chk(d, di) else 0)
            
            if bill_board[nx][ny][di] < _next_bill:
                continue
            
            bill_board[nx][ny][di] = _next_bill
            heapq.heappush(q, (_next_bill, nx, ny, di))
    
    return min(bill_board[N-1][N-1].values())