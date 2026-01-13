# 1254 팰린드롬 만들기
# https://www.acmicpc.net/problem/1254
# Silver 2
# solved

def main():
    S = input()
    
    for index in range(len(S)-1):
        flag = True
        for i in range((len(S)-index) // 2 + 1):
            if S[i+index] != S[len(S)-1-i]:
                flag = False
                break
        if flag:
            print(len(S)+index)
            return
    print((len(S)-1) * 2 + 1)
            
if __name__ == "__main__":
    main()