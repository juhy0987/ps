# 21177 No Thanks!
# https://www.acmicpc.net/problem/21177
# Silver 5
# solved

def main():
    N = int(input())
    l = sorted(list(map(int, input().split())))
    
    result = 0
    pre = -1
    for v in l:
        if v != pre + 1:
            result += v
        pre = v
    print(result)

if __name__ == "__main__":
    main()