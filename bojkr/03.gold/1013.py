# 1013 Contact
# https://www.acmicpc.net/problem/1013
# Gold 5
# solved

def solve(s):
    state = 0
    cur = 0
    while cur < len(s):
        c = s[cur]
        # print(cur, c, state)
        if state == 0:
            if c == '1':
                state = 1
            else:
                state = 5
        elif state == 1:
            if c == '0':
                state = 2
            else:
                return False
        elif state == 2:
            if c == '0':
                state = 3
            else:
                return False
        elif state == 3:
            if c == '0':
                state = 3
            else:
                state = 4
        elif state == 4:
            if c == '1':
                state = 4
            else:
                state = 5
        elif state == 5:
            if c == '1':
                state = 0
            else:
                if cur > 5 and s[cur-3] == '1':
                    state = 3
                else:
                    return False
        cur += 1
        
    
    return state == 0 or state == 4

def main():
    T = int(input())
    for _ in range(T):
        s = input()
        if solve(s):
            print("YES")
        else:
            print("NO")
    
if __name__ == "__main__":
    main()