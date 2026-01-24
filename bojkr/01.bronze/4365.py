# 4365 Stack 'em Up
# https://www.acmicpc.net/problem/4365
# Bronze 1
# solved

import sys

def main():
    n = int(input())
    
    shapes = [
        "Clubs", "Diamonds", "Hearts", "Spades"
    ]
    numbers = [
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"
    ]
    
    shuffles = []
    for _ in range(n):
        shuffles.append([])
        while (_input := sys.stdin.readline()):
            shuffle = list(map(int, _input.split()))
            shuffles[-1] += shuffle
            if len(shuffles[-1]) >= 52:
                break
        shuffles[-1] = [v-1 for v in shuffles[-1]]
    
    deck = [i for i in range(52)]
    
    def print_deck():
        for v in deck:
            shape = v // 13
            number = v % 13
            print(f"{numbers[number]} of {shapes[shape]}")
        print()
    
    while (_input := sys.stdin.readline()):
        k = int(_input)-1
        
        next_deck = [-1] * 52
        for j, i in enumerate(shuffles[k]):
            next_deck[j] = deck[i]

        deck = next_deck
        print_deck()

if __name__ == "__main__":
    main()