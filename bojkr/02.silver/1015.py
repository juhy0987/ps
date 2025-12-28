# 1015 수열 정렬
# https://www.acmicpc.net/problem/1015
# Silver 4
# solved

def main():
    N = int(input())
    A = list(map(int, input().split()))

    B = [(v, i) for i, v in enumerate(A)]
    B.sort()
    
    P = [(v[1], i) for i, v in enumerate(B)]
    P.sort()

    for i in range(len(P)):
        print(P[i][1], end=(" " if i != len(P)-1 else "\n"))
    

if __name__ == "__main__":
    main()