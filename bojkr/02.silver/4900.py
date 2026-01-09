# 4900 7 더하기
# https://www.acmicpc.net/problem/4900
# Silver 3
# solved

def main():
    d = {
        "063": "0",
        "010": "1",
        "093": "2",
        "079": "3",
        "106": "4",
        "103": "5",
        "119": "6",
        "011": "7",
        "127": "8",
        "107": "9" 
    }
    
    d_i = {v:k for k, v in d.items()}
    
    while (s := input()) != "BYE":
        A, B = s[:-1].split("+")
        
        a = ""
        b = ""
        for i in range(0, len(A), 3):
            a = a + d[A[i:i+3]]
        for i in range(0, len(B), 3):
            b = b + d[B[i:i+3]]
        c = int(a) + int(b)
        
        result = ""
        for target in str(c):
            result = result + d_i[target]
        print(s+result)

if __name__ == "__main__":
    main()