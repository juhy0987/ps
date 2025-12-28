# 1181 단어 정렬
# https://www.acmicpc.net/problem/1181
# Silver 5
# solved

def main():
    N = int(input())
    def criteria(s):
        return (len(s), s)

    l = list(set(input() for _ in range(N)))
    l.sort(key=criteria)
    for s in l:
        print(s)

if __name__ == "__main__":
    main()