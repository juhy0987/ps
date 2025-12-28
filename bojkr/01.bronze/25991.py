# 25991 Lots of Liquid
# https://www.acmicpc.net/problem/25991
# Bronze 4
# solved

import math

def main():
    N = int(input())
    sides = list(map(float, input().split()))
    answer = sum(side ** 3 for side in sides) ** (1/3)
    if 1 - (answer  - int(answer)) < 1e-6:
        print(int(answer) + 1)
    elif answer - int(answer) < 1e-6:
        print(int(answer))
    else:
        print(answer)
    
if __name__ == "__main__":
    main()