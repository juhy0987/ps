# 14911 궁합 쌍 찾기
# https://www.acmicpc.net/problem/14911
# Silver 4
# solved

def main():
    l = list(map(int, input().split()))
    N = int(input())
    
    l.sort()
    q = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == N:
                q.append((l[i], l[j]))

    q = set(q)
    for a, b in q:
        print(f"{a} {b}")
    print(len(q))

if __name__ == "__main__":
    main()