# 1158 요세푸스 문제
# https://www.acmicpc.net/problem/1158
# Silver 4
# solved

def main():
    N, K = map(int, input().split())
    
    K -= 1
    l = []
    for i in range(1, N+1):
        l.append(i)
    index = 0
    result = []
    while l:
        if len(l) == 1:
            result.append(str(l[0]))
            break
        index = (index + K) % len(l)
        # print(index)
        result.append(str(l.pop(index)))
    
    print(f"<{", ".join(result)}>")
if __name__ == "__main__":
    main()