# 1058 친구
# https://www.acmicpc.net/problem/1058
# Silver 2
# solved

def main():
    N = int(input())
    f = []
    t = []
    def classify(c):
        if c == 'Y':
            return 1
        else:
            return 0
    
    for _ in range(N):
        row = list(map(classify, list(input())))
        f.append(row)
        t.append([0] * N)
    
    # for _ in range(N):
    #     print(f[_])
    # print("====================")
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if f[i][k] and f[k][j]:
                    t[i][j] = 1
    for i in range(N):
        for j in range(N):
            f[i][j] |= t[i][j]
    
    _max = -1
    for i in range(N):
        _max = max(sum(f[i]), _max)
    # for _ in range(N):
    #     print(f[_])
    print(_max)
    
if __name__ == "__main__":
    main()