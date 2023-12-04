with open('input') as f:
    cards = [[set(map(int, card[i].split())) for i in range(len(card))] for card in [line[10:-1].split(' | ') for line in f]]

tally = [1 for _ in cards]

for i in range(len(cards)):
    num_matches = len(cards[i][0].intersection(cards[i][1]))
    for j in range(1, num_matches + 1):
        tally[i+j] += tally[i]

print(sum(tally))