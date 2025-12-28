# 2491 수열
# https://www.acmicpc.net/problem/2491
# Silver 4
# solved

def main():
    N = int(input())
    l = list(map(int, input().split()))

    if N == 1:
        print(1)
        return
    
    gap_l = [l[i+1] - l[i] for i in range(len(l)-1)]
    pre_gap = 0
    _max_length = 2
    cnt = 1
    for index in range(len(gap_l)):
        gap = gap_l[index]
        if gap == 0:
            cnt += 1
            continue
            
        if gap > 0:
            if pre_gap < 0:
                _max_length = max(_max_length, cnt)
                cnt = 1
                cur = index-1
                while cur > -1 and gap_l[cur] == 0:
                    cnt += 1
                    cur -= 1
        else:
            if pre_gap > 0:
                _max_length = max(_max_length, cnt)
                cnt = 1
                cur = index-1
                while cur > -1 and gap_l[cur] == 0:
                    cnt += 1
                    cur -= 1
        cnt += 1
        pre_gap = gap
    _max_length = max(_max_length, cnt)
    print(_max_length)

if __name__ == "__main__":
    main()