# 24860 Counting Antibodies
# https://www.acmicpc.net/problem/24860
# Bronze 4
# solved

def main():
    Vk, Jk = map(int, input().split())
    Vy, Jy = map(int, input().split())
    Vh, Dh, Jh = map(int, input().split())
    
    print((Vk * Jk + Vy * Jy) * Vh * Dh * Jh )

if __name__ == "__main__":
    main()