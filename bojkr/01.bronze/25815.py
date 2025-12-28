# 25815 Cat's Age
# https://www.acmicpc.net/problem/25815
# Bronze 3
# solved: 25.11.28 23:46

def main():
    y, m = map(int, input().split())

    first = False
    second = False
    result_y, result_m = 0, 0
    if y >= 1:
        y -= 1
        result_y += 15
        first = True
    
    if y >= 1:
        y -= 1
        result_y += 9
        second = True
    
    if not first:
        result_m += m * 15
    elif not second:
        result_m += m * 9
    else:
        result_y += y * 4
        result_m += m * 4

    if result_m >= 12:
        result_y += result_m // 12
        result_m %= 12
    
    print(result_y, result_m)

if __name__ == "__main__":
    main()