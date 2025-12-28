    """
    현대 오토에버 코딩 테스트 1번 문제
    s: 시작 단어
    c: 시작단어에서 c[0]에 해당하는 alphabet을 c[1]로 수정 

    수정한 단어를 출력하는데 출력하는 방식이 시작단어 길이의 2배까지만 출력하고 나머지는 그 길이 구해서 +n으로 표현
    
    Examples:
        Input:
            s: 'h'
            c: [['h','helo'],['o','world'],['l','llo']]]
        Output:
            'he+8'
        
        Input:
            s: 'a'
            c: [['a','abbbbbbbbbbbbbbbbbbbbbbb'],['b','cccccccccccccccccccccccccccc'],['c','ddddddddddddddddddddd']]
        Output:
            'ad+n'

    Returns:
        str: The modified string after all replacements.
    """


s = 'h'
c = [['h','helo'],['o','world'],['l','llo']]

def solve(s, c):
    result = s
    max_length = len(s) * 2
    for char, replacement in c:
        result = result.replace(char, replacement)
    
    max_length = min(len(result), len(s)*2)
    result = result[:max_length] + ('+' + str(len(result[max_length:])) if len(result) > max_length else '')
    return result

def solve2(s, c):
    s = list(s)
    dict_c = {char: replacement for char, replacement in c}
    max_length = len(s) * 2
    result = []
    
    while len(result) < max_length and s:
        char = s[0]
        if key in dict_c:
            
        
    

def main():
    # s = input()
    # c = list(input().split())
    print(s)
    print(c)
    
    result = solve(s, c)
    print(result)

if __name__ == "__main__":
    main()