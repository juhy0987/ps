# 1011 Fly me to the Alpha Centauri
# https://www.acmicpc.net/problem/1011
# Gold 5

import math

def main():
    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split())
        
        answer = 0
        dist = y-x

        n = math.sqrt(dist)
        moves = 2 * n - 1
        dist -= n * n
        
        moves += (dist // n) + (0 if dist % n == 0 else 1)
        print(moves)
        

if __name__ == "__main__":
    main()