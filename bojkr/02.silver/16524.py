# 16524 Database of Clients
# https://www.acmicpc.net/problem/16524
# Silver 4
# solved

def main():
    n = int(input())

    s = set()
    for _ in range(n):
        username, provider = input().split('@')
        username = username.split('+')[0]
        username = username.replace('.', '')
        s.add((username, provider))
    print(len(s))
    

if __name__ == "__main__":
    main()