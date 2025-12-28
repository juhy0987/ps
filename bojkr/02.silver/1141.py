# 1141 접두사
# https://www.acmicpc.net/problem/1141
# Silver 1
# solved

from itertools import combinations

def main():
    N = int(input())
    src = []
    for _ in range(N):
        src.append(input())
    
    def cmp(s):
        return (len(s), s)
    
    src.sort(key=cmp)
    # print(src)
    Z = set()
    for tmp in src:
        for target in Z:
            if len(target) >= len(tmp):
                big = target
                small = tmp
            else:
                big = tmp
                small = target
            if big.startswith(small):
                if big == tmp:
                    Z.remove(small)
                break
        Z.add(tmp)
            
    print(len(Z))

if __name__ == "__main__":
    main()