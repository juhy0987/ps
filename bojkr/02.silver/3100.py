# 3100 국기 인식
# https://www.acmicpc.net/problem/3100
# Silver 3
# solved

def main():
    board = [input().strip() for _ in range(6)]
    INF = 10**9

    def horizontal_cost():
        ranges = [(0,2), (2,4), (4,6)]
        block_cost = [[0]*26 for _ in range(3)]

        for b, (s, e) in enumerate(ranges):
            for r in range(s, e):
                for col in range(9):
                    cur = board[r][col]
                    for c in range(26):
                        if cur != chr(c + ord('A')):
                            block_cost[b][c] += 1

        best = INF
        for A in range(26):
            for B in range(26):
                if A == B: continue
                for C in range(26):
                    if C == B: continue
                    best = min(best,
                               block_cost[0][A] +
                               block_cost[1][B] +
                               block_cost[2][C])
        return best

    def vertical_cost():
        ranges = [(0,3), (3,6), (6,9)]
        block_cost = [[0]*26 for _ in range(3)]

        for b, (l, r) in enumerate(ranges):
            for row in range(6):
                for col in range(l, r):
                    cur = board[row][col]
                    for c in range(26):
                        if cur != chr(c + ord('A')):
                            block_cost[b][c] += 1

        best = INF
        for A in range(26):
            for B in range(26):
                if A == B: continue
                for C in range(26):
                    if C == B: continue
                    best = min(best,
                               block_cost[0][A] +
                               block_cost[1][B] +
                               block_cost[2][C])
        return best

    print(min(horizontal_cost(), vertical_cost()))


if __name__ == "__main__":
    main()