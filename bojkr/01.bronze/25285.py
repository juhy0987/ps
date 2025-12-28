# 25285 심준의 병역판정검사
# https://www.acmicpc.net/problem/25285
# Bronze 3
# solved

def main():
    T = int(input())
    for _ in range(T):
        h, w = map(int, input().split())
        
        BMI = w / ((h / 100) ** 2)
        if h <= 140:
            print(6)
            continue
        elif h < 146:
            print(5)
            continue
        elif h < 159:
            print(4)
            continue
        elif h < 161:
            if BMI >= 16.0 and BMI < 35.0:
                print(3)
            else:
                print(4)
            continue
        elif h >= 204:
            print(4)
            continue
        else:
            if BMI >= 20.0 and BMI < 25.0:
                print(1)
            elif (BMI >= 18.5 and BMI < 20.0) or (BMI >= 25.0 and BMI < 30.0):
                print(2)
            elif (BMI >= 16.0 and BMI < 18.5) or (BMI >= 30.0 and BMI < 35.0):
                print(3)
            else:
                print(4)
            continue

if __name__ == "__main__":
    main()