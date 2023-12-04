with open('input') as f:
    lines = [line for line in f]

ratios = [[[] for _ in line] for line in lines]

def check_gear(row, col):
    for x in [-1, 0, 1]:
        if (row + x) not in range(0, len(lines)):
            continue
        for y in [-1, 0, 1]:
            if (col + y) not in range (0, len(lines[row + x])):
                continue
            if lines[row + x][col + y] == '*':
                return [row + x, col + y]
    return [-1, -1]
            
for i in range(len(lines)):
    gear = [-1, -1]
    num = 0
    for j in range(len(lines[i])):
        if lines[i][j].isnumeric():
            num = num*10 + int(lines[i][j])
            if gear == [-1, -1]:
                gear = check_gear(i,j)
        else:
            if gear != [-1, -1]:
                ratios[gear[0]][gear[1]].append(num)
            gear = [-1, -1]
            num = 0

sum = sum([sum([gr[0]*gr[1] for gr in line if len(gr) == 2]) for line in ratios])
print(sum)