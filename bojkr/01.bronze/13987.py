# 13987 Six Sides
# https://www.acmicpc.net/problem/13987
# Bronze 2
# solved: 25.11.28 23:52

def main():
    f = list(map(int, input().split()))
    s = list(map(int, input().split()))

    count = 0
    total = 36
    for i in f:
        for j in s:
            if i > j:
                count += 1
            elif i == j:
                total -= 1
    
    print("%.5f" % (count / total))

if __name__ == "__main__":
    main()