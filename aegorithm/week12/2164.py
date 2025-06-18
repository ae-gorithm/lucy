from collections import deque

def card_game(cards):
    while cards:
        if len(cards) == 1:
            break
        first = cards.popleft()
        second = cards.popleft()
        cards.append(second)
    return cards.popleft()


n = int(input())

cards = deque([i for i in range(1, n+1)])
result = card_game(cards)
print(result)