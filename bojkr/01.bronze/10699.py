# 10699 오늘 날짜
# https://www.acmicpc.net/problem/10699
# Bronze 5
# solved

from datetime import datetime

def main():
    print(datetime.strftime(datetime.now(), "%Y-%m-%d"))

if __name__ == "__main__":
    main()