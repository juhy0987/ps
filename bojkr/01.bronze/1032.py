"""
https://www.acmicpc.net/problem/1032
명령 프롬프트 : bronze 1
"""

def main():
    n = int(input())
    criteria = [c for c in input()]
    for _ in range(n-1):
        word = [c for c in input()]
        for i in range(len(criteria)):
            if criteria[i] == '?':
                continue
            if criteria[i] != word[i]:
                criteria[i] = '?'
    print("".join(criteria))


if __name__ == "__main__":
    main()