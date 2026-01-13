# 1262 알파벳 다이아몬드
# https://www.acmicpc.net/problem/1262
# Silver 1
# solved

def main():
    N, R1, C1, R2, C2 = map(int, input().split())
    
    length = 2*N-1
    def _pattern(i, j):
        cur_r = -1
        if i % length < N:
            cur_r = i % length
        else:
            cur_r = 2*N-2-(i % length)
        
        cur_c = j % length
        if cur_c < (N-1-cur_r) or cur_c >= length - (N-1-cur_r):
            return "."

        return chr((N-1-(cur_r-abs(N-1-cur_c))) % 26 + ord('a'))
    for i in range(R1, R2+1):
        tmp = []
        for j in range(C1, C2+1):
            tmp.append(_pattern(i, j))
        print("".join(tmp))
        
if __name__ == "__main__":
    main()