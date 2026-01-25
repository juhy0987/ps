# 18808 스티커 붙이기
# https://www.acmicpc.net/problem/18808
# Gold 3
# solved

def main():
    N, M, K = map(int, input().split())
    stickers = []
    
    def rotate(sticker):
        R, C = len(sticker[0]), len(sticker)
        new_sticker = [[sticker[c][r] for c in range(C-1, -1, -1)] for r in range(R)]
        # print(new_sticker)
        return new_sticker
    
    def print_cells(sticker):
        for row in sticker:
            print(row)
        print("============================")
    
    for _ in range(K):
        R, C = map(int, input().split())
        sticker = [list(map(int, input().split())) for _ in range(R)]
        d = [sticker]
        for i in range(3):
            sticker = rotate(sticker)
            d.append(sticker)
        stickers.append(d)
    
    notebook = [[0] * M for _ in range(N)]
    
    def is_able(sticker, i, j):
        R, C = len(sticker), len(sticker[0])
        if i + R-1 >= N or j + C-1 >= M:
            return False

        # if i == 0 and j == 2:
        #     print(i, j)
        #     print_cells(notebook)
        
        for r in range(R):
            for c in range(C):
                if sticker[r][c] and notebook[i+r][j+c]:
                    # print(r, c, i, j)
                    return False
        return True

    def insert(sticker, i, j):
        R, C = len(sticker), len(sticker[0])
        
        for r in range(R):
            for c in range(C):
                notebook[i+r][j+c] = notebook[i+r][j+c] | sticker[r][c]
    
    for d in stickers:
        for sticker in d:
            # print_cells(sticker)
            flag = False
            for i in range(N):
                for j in range(M):
                    if is_able(sticker, i, j):
                        insert(sticker, i, j)
                        flag = True
                        break
                if flag:
                    break
            if flag:
                break
    
    # for row in notebook:
    #     print(row)
    
    print(sum(sum(row) for row in notebook))
        

if __name__ == "__main__":
    main()