# 1551 수열의 변화
# https://www.acmicpc.net/problem/1551
# Bronze 1
# solved

def main():
    N, K = map(int, input().split())
    target = list(map(int, input().split(',')))
    for _ in range(K):
        target = [target[i+1]-target[i] for i in range(len(target)-1)]
    print(",".join(map(str, target)))

if __name__ == "__main__":
    main()