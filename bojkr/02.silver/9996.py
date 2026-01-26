# 9996 한국이 그리울 땐 서버에 접속하지
# https://www.acmicpc.net/problem/9996
# Silver 3
# solved

def main():
    N = int(input())
    s = input().split('*')
    
    for _ in range(N):
        target = input()
        if len(s[0]) + len(s[1]) > len(target):
            print("NE")
            continue
        
        flag = False
        for i, c in enumerate(s[0]):
            if target[i] != c:
                flag = True
                break
        for i, c in enumerate(s[1]):
            if target[len(target)-len(s[1])+i] != c:
                flag = True
                break
            
        if flag:
            print("NE")
        else:
            print("DA")
        

if __name__ == "__main__":
    main()