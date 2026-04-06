# 16337 Die
# https://www.acmicpc.net/problem/16337
# Bronze 2
# solved

import sys

def main():
    d = {
        1: [(4,)],
        2: [(0, 8), (2, 6)],
        # 2: [(1, 7), (3, 5)],
        3: [(0, 4, 8), (2, 4, 6)],
        4: [(0, 2, 6, 8)],
        5: [(0, 2, 4, 6, 8)],
        6: [(0, 1, 2, 6, 7, 8), (0, 2, 3, 5, 6, 8)]
    }
    
    s = {tuple(v): k for k, l in d.items() for v in l}
    # print(s)
    target = []
    for r in range(3):
        src = sys.stdin.readline().strip()
        
        for i, c in enumerate(src):
            if c == "o":
                target.append(r*3+i)
    # print(tuple(target))
    if (tmp := s.get(tuple(target))):
        print(tmp)
    else:
        print("unknown")

if __name__ == "__main__":
    main()