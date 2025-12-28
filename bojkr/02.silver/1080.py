# 1080. 행렬
# 문제: https://www.acmicpc.net/problem/1080
# 실버 1
# solved: 2025-11-28 23:19

def main():
    n, m = map(int, input().split())
    a = [list(map(int, list(input().strip()))) for _ in range(n)]
    b = [list(map(int, list(input().strip()))) for _ in range(n)]
    
    # print_matrix(a)
    # print_matrix(b)
    src = [[a[i][j] ^ b[i][j] for j in range(m)] for i in range(n)]

    if n < 3 or m < 3:
        if all(all(x == 0 for x in row) for row in src):
            print(0)
        else:
            print(-1)
        return
    # print_matrix(src)

    count = 0
    directions = [(0, 0), (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(0, n-2):
        for j in range(0, m-2):
            if src[i][j] == 1:
                for di in range(i, i+3):
                    for dj in range(j, j+3):
                        src[di][dj] ^= 1
                count += 1
            
    # print_matrix(src)
    if all(all(x == 0 for x in row) for row in src):
        print(count)
    else:
        print(-1)

def print_matrix(matrix):
    for row in matrix:
        print(row)
    print("=====================")

if __name__ == "__main__":
    main()