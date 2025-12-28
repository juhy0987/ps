# 1021 회전하는 큐
# https://www.acmicpc.net/problem/1021
# Silver 3
# solved

def main():
    N, M = map(int, input().split())
    targets = list(map(int, input().split()))
    
    result = 0
    _sum = 0
    targets = [t-1 for t in targets]
    src = list(range(N))
    for i, target in enumerate(targets):
        # if (target + _sum - i) % (N-i) < (N-i) - ((target + _sum - i) % (N-i)):
        #     _min = (target + _sum - i) % (N-i)
        #     print(N-i, (target + _sum - i) % (N-i), _min)
        #     _sum -= _min
            
        # else:
        #     _min = (N-i) - ((target + _sum - i) % (N-i))
        #     print(N-i, (target + _sum - i) % (N-i), _min)
        #     _sum += _min
        
        # result += _min
        
        while True:
            if src[0] == target:
                src.pop(0)
                break
            
            if src.index(target) <= len(src) // 2:
                src.append(src.pop(0))
            else:
                src.insert(0, src.pop())
            result += 1
    print(result)
if __name__ == "__main__":
    main()