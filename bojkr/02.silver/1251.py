# 1251 단어 나누기
# https://www.acmicpc.net/problem/1251
# Silver 5
# solved

from itertools import combinations

def main():
    S = input()
    
    def r(s):
        return "".join(reversed(s))
    
    _min = "z" * len(S)
    for a, b in combinations(range(1, len(S)), 2):
        _min = min(_min, r(S[:a]) + r(S[a:b]) + r(S[b:]))
    print(_min)

if __name__ == "__main__":
    main()