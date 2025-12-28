# 3254 김밥 21개
# https://www.acmicpc.net/problem/3254
# Silver 3
# solved

def main():
    board = []
    for _ in range(7):
        board.append([])
    
    winner = None
    directions = [
        [(0,0), (0,1), (0,2), (0,3)],
        [(0,0), (1,1), (2,2), (3,3)],
        [(0,0), (1,0), (2,0), (3,0)],
        [(0,0), (1,-1), (2,-2), (3,-3)]
    ]
    def chk():
        # for i in range(7):
        #     print(board[i])
        # print("=======================")
        
        for i in range(7):
            for j in range(len(board[i])):
                for di in directions:
                    flag = True
                    target = None
                    for c, r in di:
                        pos = (i+c, j+r)
                        # print(pos)
                        if pos[0] >= 7 or pos[1] >= 6 or pos[1] < 0:
                            flag = False
                            break
                        if pos[1] >= len(board[pos[0]]):
                            flag = False
                            break
                        
                        if not target:
                            target = board[pos[0]][pos[1]]
                        elif target != board[pos[0]][pos[1]]:
                            flag = False
                            break
                    
                    if flag and target:
                        # print(target)
                        return target
                    # print(i, j, di)
        return None
    
    cnt = -1
    for _ in range(21):
        Si, Ji = map(int, input().split())
        
        board[Si-1].append("sk")
        if cnt < 0 and (winner := chk()):
            cnt = _
            
        board[Ji-1].append("ji")
        if cnt < 0 and (winner := chk()):
            cnt = _
    if winner:
        print(winner, cnt+1)
    else:
        print("ss")

if __name__ == "__main__":
    main()