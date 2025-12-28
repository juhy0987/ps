# 13567 로봇
# https://www.acmicpc.net/problem/13567
# Silver 4

def main():
    M, n = map(int, input().split())
    cmd_dict = {
        "MOVE": 0,
        "TURN": 1
    }

    flag = False
    dir_list = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    dir = 0
    pos = (0, 0)
    for _ in range(n):
        cmd, d = input().split()

        if flag:
            continue
        cmd = cmd_dict[cmd]
        d = int(d)
        
        if cmd:
            d = 1 if d else -1
            dir = (dir + d) % 4
        else:
            pos = (pos[0] + dir_list[dir][0] * d, pos[1] + dir_list[dir][1] * d)
            if any(p < 0 for p in pos) or any(p > M for p in pos):
                flag = True
                continue
    
    if flag:
        print(-1)
    else:
        print(f"{pos[0]} {pos[1]}")

if __name__ == "__main__":
    main()