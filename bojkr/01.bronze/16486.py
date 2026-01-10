# 16486 운동장 한 바퀴
# https://www.acmicpc.net/problem/16486
# Bronze 4
# solved

def main():
    pi = 3.141592
    d1 = int(input())    
    d2 = int(input())
    
    print("%.6f" % (2 * d1 + 2* d2 * pi))

if __name__ == "__main__":
    main()