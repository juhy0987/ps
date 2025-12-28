# 1063 킹
# https://www.acmicpc.net/problem/1063
# Silver 3
# solved

def main():
    K, R, N = input().split()
    N = int(N)
    k = (-1, -1)
    r = (-1, -1)

    k = (ord(K[0])-ord('A'), int(K[1])-1)
    r = (ord(R[0])-ord('A'), int(R[1])-1)
    
    for _ in range(N):
        cmd = input()
        move = [0, 0]
        if 'B' in cmd:
            move[1] = -1
        elif 'T' in cmd:
            move[1] = 1
        if 'L' in cmd:
            move[0] = -1
        elif 'R' in cmd:
            move[0] = 1
        
        if k[0] + move[0] == r[0] and k[1] + move[1] == r[1]:
            r_next_pos = (r[0] + move[0], r[1] + move[1])
            if r_next_pos[0] >= 8 or r_next_pos[0] < 0 \
                or r_next_pos[1] >= 8 or r_next_pos[1] < 0:
                continue
            r = r_next_pos
        
        k_next_pos = (k[0] + move[0], k[1] + move[1])
        if k_next_pos[0] >= 8 or k_next_pos[0] < 0 \
            or k_next_pos[1] >= 8 or k_next_pos[1] < 0:
            continue
        k = k_next_pos
    
    print(chr(k[0]+ord('A'))+str(k[1]+1))
    print(chr(r[0]+ord('A'))+str(r[1]+1))
    
if __name__ == "__main__":
    main()