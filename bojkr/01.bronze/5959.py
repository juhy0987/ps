# 5959 Crop Circles
# https://www.acmicpc.net/problem/5959
# Bronze 1
# solved

def main():
    N = int(input())
    circles = []
    for _ in range(N):
        Xi, Yi, Ri = map(int, input().split())
        circles.append((Xi, Yi, Ri))
    
    def dis(a: tuple, b: tuple):
        return (a[0]-b[0]) ** 2 + (a[1]-b[1]) ** 2 < (a[2] + b[2]) ** 2
    
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i == j:
                continue
            cnt += 1 if dis(circles[i], circles[j]) else 0
        
        print(cnt)
    
if __name__ == "__main__":
    main()