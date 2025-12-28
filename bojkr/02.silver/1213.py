# 1213 팰린드롬 만들기
# https://www.acmicpc.net/problem/1213
# Silver 3
# solved

def main():
    s = input()
    count = [[s.count(chr(i + ord('A'))), i] for i in range(26)]
    
    if [c % 2 != 0 for c, i in count].count(True) > 1:
        print("I'm Sorry Hansoo")
        return
    
    for i in range(len(count)):
        if count[i][0] % 2 == 1:
            count.append([1, count[i][1]])
            count[i][0] -= 1
            break
    
    new_s = ""
    for i, c in count:
        new_s = new_s[:len(new_s) // 2] + chr(ord('A') + c) * i + new_s[len(new_s) // 2:]
        
    print(new_s)
    
if __name__ == "__main__":
    main()