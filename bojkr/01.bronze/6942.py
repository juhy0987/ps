# 6942 9966
# https://www.acmicpc.net/problem/6942
# Bronze 1
# solved

def main():
    d = {
        "0": "0",
        "1": "1",
        "2": "\0",
        "3": "\0",
        "4": "\0",
        "5": "\0",
        "6": "9",
        "7": "\0",
        "8": "8",
        "9": "6"
    }
    
    m = int(input())
    n = int(input())
    
    cnt = 0
    for k in range(m, n+1):
        s = str(k)
        flag = True
        for i in range(len(s) // 2+1):
            # print(k, d[s[i]], s[len(s)-1-i])
            if i == len(s)-1-i:
                if s[i] not in ["0", "1", "8"]:
                    flag = False
                    break
                continue
            elif d[s[i]] == '\0' or d[s[i]] != s[len(s)-1-i]:
                flag = False
                break
            
        if flag:
            # print(k)
            cnt += 1
    print(cnt)
    
if __name__ == "__main__":
    main()