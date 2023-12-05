import sys

with open('input') as f:
    lines = [line for line in f]

seeds = [int(x) for x in lines[0][6:].split()]
maps = []

for line in lines[2:]:
    if line[0].isalpha():
        if maps != []:
            maps[-1].sort(key=lambda x: x[1])
        maps.append([])
        continue
    if line[0].isnumeric():
        maps[-1].append([int(x) for x in line.split()])

min_location = sys.maxsize

for seed in seeds:
    n = seed
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if n >= maps[i][j][1]:
                if n < maps[i][j][1] + maps[i][j][2]:
                    n = maps[i][j][0] + (n - maps[i][j][1])    
                    break           
    if n < min_location:
        min_location = n

print(min_location)
