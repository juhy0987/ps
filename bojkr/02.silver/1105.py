# 1105. 팔
# 문제: https://www.acmicpc.net/problem/1105
# 실버 1
# solved: 2025-11-28 23:30

def main():
    l, r = input().split()
    
    # if len(l) > len(r):
    #     r = '0' * (len(l) - len(r)) + r
    # elif len(l) < len(r):
    #     l = '0' * (len(r) - len(l)) + l
    if len(l) != len(r):
        print(0)
        return
    
    count = 0
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] == '8':
                count += 1
        else:
            break
    print(count)

if __name__ == "__main__":
    main()