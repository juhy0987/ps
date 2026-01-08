# 29997 Lexicographical Challenge
# https://www.acmicpc.net/problem/29997
# Bronze 1
# solved

def main():
    S = list(input())
    K = int(input())
    
    for index in range(K):
        S[index::K] = sorted(S[index::K])
    
    print("".join(S))

if __name__ == "__main__":
    main()