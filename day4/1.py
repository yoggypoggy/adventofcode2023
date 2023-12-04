with open('input') as f:
    cards = [[set(map(int, card[i].split())) for i in range(len(card))] for card in [line[10:-1].split(' | ') for line in f]]

def points(index, num):
    if num == 0:
        return 0
    return pow(2, num - 1)

winning = sum([points(len(card[0].intersection(card[1]))) for card in cards])
print(winning)