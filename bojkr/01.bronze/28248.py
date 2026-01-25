# 28248 Deliv-e-droid
# https://www.acmicpc.net/problem/28248
# Bronze 4
# solved

def main():
    P = int(input())
    C = int(input())
    
    print(50*P - 10*C + (500 if P > C else 0))

if __name__ == "__main__":
    main()