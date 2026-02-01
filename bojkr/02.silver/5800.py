# 5800 성적 통계
# https://www.acmicpc.net/problem/5800
# Silver 5
# solved

import sys

def main():
    K = int(sys.stdin.readline().strip())
    for c in range(1, K+1):
        C = sorted(list(map(int, sys.stdin.readline().strip().split()))[1:])
        
        _max = -1
        for i in range(len(C)-1):
            _max = max(_max, C[i+1]-C[i])
        
        print(f"Class {c}")
        print(f"Max {C[-1]}, Min {C[0]}, Largest gap {_max}")

if __name__ == "__main__":
    main()