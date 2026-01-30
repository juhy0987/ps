# 7656 만능 오라클
# https://www.acmicpc.net/problem/7656
# Silver 4
# solved

import re

def main():
    S = input()
    
    questions = re.findall(r"What is[a-z ,;'\-]*\?", S)
    for q in questions:
        
        print("Forty-two"+q[4:-1]+".")

if __name__ == "__main__":
    main()