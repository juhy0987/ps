# 26150 Identify, Sort, Index, Solve
# https://www.acmicpc.net/problem/26150
# Silver 5
# solved

def main():
    N = int(input())
    l = []
    for _ in range(N):
        S, I, D = input().split()
        l.append((S[int(D)-1].upper(), int(I)))
    l.sort(key=lambda x:x[1])
    print("".join([c for c, i in l]))

if __name__ == "__main__":
    main()