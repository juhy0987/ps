# 3100 국기 인식
# https://www.acmicpc.net/problem/3100
# Silver 3

def main():
    board = [input().strip() for _ in range(6)]
    INF = 10**9
    ans = INF

    horizontal_patterns = [
        [(0, 2), (2, 4), (4, 6)],
        [(0, 4), (4, 6), (0, 0)]
    ]

    for rows in horizontal_patterns:
        for c1 in range(26):
            for c2 in range(26):
                if c1 == c2:
                    continue
                for c3 in range(26):
                    if c3 == c1 or c3 == c2:
                        continue

                    cost = 0
                    for i in range(6):
                        for j in range(9):
                            if rows[0][0] <= i < rows[0][1]:
                                target = chr(ord('A') + c1)
                            elif rows[1][0] <= i < rows[1][1]:
                                target = chr(ord('A') + c2)
                            else:
                                target = chr(ord('A') + c3)
                            if board[i][j] != target:
                                cost += 1
                    ans = min(ans, cost)

    vertical_patterns = [
        [(0, 3), (3, 6), (6, 9)],
        [(0, 3), (3, 6), (0, 0)]
    ]

    for cols in vertical_patterns:
        for c1 in range(26):
            for c2 in range(26):
                if c1 == c2:
                    continue
                for c3 in range(26):
                    if c3 == c1 or c3 == c2:
                        continue

                    cost = 0
                    for i in range(6):
                        for j in range(9):
                            if cols[0][0] <= j < cols[0][1]:
                                target = chr(ord('A') + c1)
                            elif cols[1][0] <= j < cols[1][1]:
                                target = chr(ord('A') + c2)
                            else:
                                target = chr(ord('A') + c3)
                            if board[i][j] != target:
                                cost += 1
                    ans = min(ans, cost)

    print(ans)


if __name__ == "__main__":
    main()