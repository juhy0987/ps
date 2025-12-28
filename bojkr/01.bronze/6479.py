# 6479 Factorial Frequencies
# https://www.acmicpc.net/problem/6479
# Bronze 2
# solved

from math import factorial

def main():
    while True:
        N = int(input())
        if N == 0:
            return
        input()
        
        f = factorial(N)
        
        f = str(f)
        count = [f.count(str(i)) for i in range(10)]
        
        print(f"{N}! --")
        for i in range(2):
            for j in range(5):
                if j == 0:
                    print("   (%d)%5d" % (5*i + j, count[5*i + j]), end='')
                else:
                    print("    (%d)%5d" % (5*i + j, count[5*i + j]), end = '')
            print(' ')
    

if __name__ == "__main__":
    main()