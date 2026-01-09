# 22941 RPG 마스터 오명진
# https://www.acmicpc.net/problem/22941
# Silver 2
# solved

def main():
    HP_Y, ATK_Y, HP_M, ATK_M = map(int, input().split())
    P, S = map(int, input().split())
    
    Y2M = (HP_M + ATK_Y - 1) // ATK_Y
    if 1 <= (HP_M - ATK_Y * (Y2M-1)) <= P:
        Y2M = (HP_M + S + ATK_Y - 1) // ATK_Y
    print("Victory!" if (HP_Y - ATK_M * (Y2M-1)) > 0 else "gg")
        
if __name__ == "__main__":
    main()