# 9777 Birthday Statistics
# https://www.acmicpc.net/problem/9777
# Bronze 2
# solved

def main():
    N = int(input())
    
    cnt = [0] * 12
    for _ in range(N):
        s = input()
        s = s.split()
        month = int(s[1].split('/')[1])
        cnt[month-1] += 1
    
    for i, c in enumerate(cnt):
        print(f"{i+1} {c}")

if __name__ == "__main__":
    main()