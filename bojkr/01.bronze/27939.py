# 27939 가지 교배
# https://www.acmicpc.net/problem/27939
# Bronze 1
# solved

def main():
    n = int(input())
    l = list(map(lambda x : 1 if x == 'P' else 0, input().split()))
    m, k = map(int, input().split())
    a = []
    for _ in range(m):
        a.append(list(l[i-1] for i in map(int, input().split())))
    
    tmp = []
    for ai in a:
        if any(ai):
            tmp.append(1)
        else:
            tmp.append(0)
    
    if any(x == 0 for x in tmp):
        print('W')
    else:
        print('P')

if __name__ == "__main__":
    main()