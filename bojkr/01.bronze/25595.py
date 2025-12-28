# 25595 86 -에이티식스- 2
# https://www.acmicpc.net/problem/25595
# Bronze 1
# solved

def main():
    N = int(input())
    field = []
    
    lena = None
    for i in range(N):
        field.append(list(map(int, input().split())))
        for j in range(N):
            if field[i][j] == 2:
                lena = (i + j) & 1
                
    # for i in range(N):
    #     print(field[i])
        
    for i in range(N):
        for j in range(N):
            if field[i][j] == 1:
                if (i + j) & 1 == lena:
                    print("Kiriya")
                    return
            
    print("Lena")
    
if __name__ == "__main__":
    main()