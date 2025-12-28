# 1195 킥다운
# https://www.acmicpc.net/problem/1195
# Silver 1

def main():
    a = list(map(int, list(input())))
    b = list(map(int, list(input())))
    
    _min = len(a) + len(b)
    _long = []
    _short = []
    if len(a) > len(b):
        _long = a
        _short = b
    else:
        _long = b
        _short = a
    
    for i in range(1, len(_long) + len(_short) + 1):
        
        flag = True
        if i <= len(_short):
            # print([0]*(len(_short)-i) + _long)
            # print(_short)
            for p in range(i):
                tmp_long = _long[p]
                tmp_short = _short[len(_short)-i+p]
                if tmp_long + tmp_short > 3:
                    flag = False
                    break
        elif i > len(_short) and i < len(_long):
            # print(_long)
            # print([0]*(i-len(_short)) + _short)
            for p in range(len(_short)):
                tmp_long = _long[i-len(_short)+p]
                tmp_short = _short[p]
                if tmp_long + tmp_short > 3:
                    flag = False
                    break
        else:
            # print(_long)
            # print([0]*(i-len(_short)) + _short)
            for p in range(len(_short)-(i-len(_long))):
                tmp_long = _long[i-len(_long)+p]
                tmp_short = _short[p]
                if tmp_long + tmp_short > 3:
                    flag = False
                    break
        if flag:
            _min = min(_min, max(len(_long), len(a)+len(b)-i))
    print(_min)
    
if __name__ == "__main__":
    main()