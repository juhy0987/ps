# 1024 수열의 합
# https://www.acmicpc.net/problem/1024
# Silver 2
# solved

def main():
    n, l = map(int, input().split())

    for length in range(l, 101):
        tmp = length * (length+1) // 2 - length
        result = n
        
        result -= tmp
        if result < 0 or (result // length) * length != result:
            continue
    
        result //= length
        output = [str(i) for i in range(result, result + length)]
        print(" ".join(output)) 
        return
    print(-1)

if __name__ == "__main__":
    main()