import re

color_dict = {"red": 0, "green": 0, "blue": 0}

with open('input') as f:
    games = [re.sub("Game .+: ", "", line) for line in f]

cubes = [[cube.split(", ") for cube in game_set] for game_set in [game.split("; ") for game in games]]

def min_cubes(num_color):
    x = num_color.split()
    num = int(x[0])
    color = x[1]
    if num > color_dict[color]:
        color_dict[color] = num

def game_power(game):
    for game_set in game:
        for num_color in game_set:
            min_cubes(num_color)
    return color_dict["red"] * color_dict["green"] * color_dict["blue"]

sum = 0

for game in cubes:
    color_dict["red"] = 0
    color_dict["green"] = 0
    color_dict["blue"] = 0
    sum += game_power(game)

print(sum)