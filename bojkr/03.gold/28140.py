"""
https://www.acmicpc.net/problem/28140
빨강~ 빨강~ 파랑! 파랑! 달콤한 솜사탕! : gold 5
"""

def main():
    n, q = map(int, input().split())
    s = input().strip()
    pos = {'R': [], 'B': []}
    for i, c in enumerate(s):
        if c in 'RB':
            pos[c].append(i)
    pos['B'].reverse()
    
    for _ in range(q):
        l, r = map(int, input().split())
        r_index = -1
        b_index = -1
        
        for i in range(len(pos['R'])-1):
            if l <= pos['R'][i]:
                r_index = i+1
                break
        for i in range(len(pos['B'])-1):
            if pos['B'][i] <= r:
                b_index = i+1
                break
        
        
        if r_index == -1 or b_index == -1:
            print(f"-1")
            continue
                 
        if pos['R'][r_index] > pos['B'][b_index]:
            print(f"-1")
            continue
        
        print(f"{pos['R'][r_index-1]} {pos['R'][r_index]} {pos['B'][b_index]} {pos['B'][b_index-1]}")
if __name__ == "__main__":
    main()
        