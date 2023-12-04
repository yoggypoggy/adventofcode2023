import re

color_dict = {"red": 12, "green": 13, "blue": 14}

with open('input') as f:
    games = [re.sub("Game .+: ", "", line) for line in f]

games = [game.split("; ") for game in games]
game_sets = [[game_set.split(", ") for game_set in game] for game in games]

def valid_cubes(num_color):
    x = num_color.split()
    num = int(x[0])
    color = x[1]
    if num > color_dict[color]:
        return False
    else:
        return True

def valid_game(game):
    for game_set in game:
        for num_color in game_set:
            if valid_cubes(num_color) == False:
                return False
    return True

sum = 0

for i in range(len(game_sets)):
    if valid_game(game_sets[i]) == True:
        sum += i + 1

print(sum)