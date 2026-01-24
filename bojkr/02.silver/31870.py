# 31870 버블버블
# https://www.acmicpc.net/problem/31870
# Silver 3
# solved

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [v for v in A]
    
    def swap_A(i):
        tmp = A[i]
        A[i] = A[i+1]
        A[i+1] = tmp
    
    def swap_B(i):
        tmp = B[i]
        B[i] = B[i+1]
        B[i+1] = tmp
    
    cnt_asc = 0
    for i in range(N-1):
        for j in range(N-1-i):
            # print(i, j, j+1)
            if A[j] > A[j+1]:
                swap_A(j)
                cnt_asc += 1
                # print(A)
    
    cnt_desc = 0
    for i in range(N-1):
        for j in range(N-2, i-1, -1):
            # print(i, j, j+1)
            if B[j] < B[j+1]:
                swap_B(j)
                cnt_desc += 1
                # print(B)
        
    print(min(cnt_asc, cnt_desc+1))
                

if __name__ == "__main__":
    main()