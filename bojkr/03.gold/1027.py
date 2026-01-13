# 1027 고층 건물
# https://www.acmicpc.net/problem/1027
# Gold 4
# solved

def main():
    N = int(input())
    L = list(map(int, input().split()))
    
    _max = 0
    for i in range(N):
        cnt = 0
        
        for k in range(N):
            if i == k:
                continue
            
            _begin = min(i, k)
            _end = max(i, k)
            flag = True
            for m in range(_begin+1, _end):
                if (L[_end] - L[_begin]) / (_end - _begin) * (m - _begin) + L[_begin] <= L[m]:
                    flag = False
                    break
            if flag:
                cnt += 1
        
        _max = max(cnt, _max)
    print(_max)

if __name__ == "__main__":
    main()