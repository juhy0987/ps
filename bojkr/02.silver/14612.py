# 14612 김식당
# https://www.acmicpc.net/problem/14612
# Silver 4
# solved

def main():
    N, M = map(int, input().split())
    q = []
    
    def print_q():
        if q:
            print(" ".join([str(n) for t, n in q]))
        else:
            print("sleep")
    
    for _ in range(N):
        cmd = input().split()
        if cmd[0] == 'order':
            q.append((int(cmd[2]), int(cmd[1])))
        elif cmd[0] == 'complete':
            for i in range(len(q)):
                if q[i][1] == int(cmd[1]):
                    q.pop(i)
                    break
        elif cmd[0] == 'sort':
            q.sort()
        print_q()

if __name__ == "__main__":
    main()