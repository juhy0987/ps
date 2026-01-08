# 25965 미션 도네이션
# https://www.acmicpc.net/problem/25965
# Bronze 3
# solved

def solve(M, missions, k, d, a):
    result = 0
    for mk, md, ma in missions:
        _sum = mk*k - md*d + ma*a
        if _sum > 0:
            result += _sum
    
    return result

def main():
    N = int(input())
    for _ in range(N):
        M = int(input())
        missions = []
        for _ in range(M):
            missions.append(list(map(int, input().split())))
        k, d, a = map(int, input().split())
        print(solve(M, missions, k, d, a))
        

if __name__ == "__main__":
    main()