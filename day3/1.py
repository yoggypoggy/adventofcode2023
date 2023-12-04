with open('input') as f:
    lines = [line for line in f]

def check_symbol(row, col):
    for x in [-1, 0, 1]:
        if (row + x) not in range(0, len(lines)):
            continue
        for y in [-1, 0, 1]:
            if (col + y) not in range (0, len(lines[row + x])):
                continue
            if is_symbol(lines[row + x][col + y]) == True:
                return True
    return False
            
def is_symbol(char):
    return (char.isnumeric() == False) and (char != '.') and (char != '\n')

sum = 0

for i in range(len(lines)):
    is_part = False
    num = 0
    for j in range(len(lines[i])):
        if lines[i][j].isnumeric():
            num = num*10 + int(lines[i][j])
            if is_part == False:
                is_part = check_symbol(i,j)
        else:
            if is_part == True:
                sum += num
            is_part = False
            num = 0

print(sum)