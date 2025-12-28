# 15788 밸런스 스톤
# https://www.acmicpc.net/problem/15788
# Silver 4
# solved

def main():
    N = int(input())
    m = []
    pos = (-1, -1)
    for i in range(N):
        row = list(map(int, input().split()))
        m.append(row)
        for j in range(N):
            if row[j] == 0:
                pos = (i, j)
                break
    _sum = -1
    if pos[0] == 0:
        _sum = sum(m[1])
    else:
        _sum = sum(m[0])
    m[pos[0]][pos[1]] = _sum - sum(m[pos[0]])
    
    tmp = [0] * (2*N+2)
    for i in range(N):
        for j in range(N):
            tmp[i] += m[i][j]
            tmp[N+j] += m[i][j]
        tmp[-2] += m[i][i]
        tmp[-1] += m[i][N-1-i]
    
    for i in range(1, len(tmp)):
        if tmp[i] != tmp[0]:
            print(-1)
            return
    print(m[pos[0]][pos[1]])
    
if __name__ == "__main__":
    main()