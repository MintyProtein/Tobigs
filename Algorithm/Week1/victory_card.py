import sys

N, M = map(int, sys.stdin.readline().split(' '))
selected_cards = []
for tobigee in range(N):
    cards = list(map(int, sys.stdin.readline().split(' ')))
    selected_cards.append(min(cards))
print(max(selected_cards))