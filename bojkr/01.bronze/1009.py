# 1009 분산 처리
# https://www.acmicpc.net/problem/1009
# Bronze 2

def main():
    T = int(input())

    d = {
        0: [10],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }
    
    for _ in range(T):
        a, b = map(int, input().split())
        
        target = d[a % 10]
        print(target[(b-1) % len(target)])

if __name__ == "__main__":
    main()