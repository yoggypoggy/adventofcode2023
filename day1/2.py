with open('input') as f:
    stuff = [line for line in f]

three = ['one','two','six']
four = ['four','five','nine']
five = ['three','seven','eight']
numbers = ['one','two','three','four','five','six','seven','eight','nine']
x = 0

def convert(number):
    if number.isnumeric():
        return int(number)
    else:
        return numbers.index(number) + 1

for line in stuff:
    y = []
    for i in range(len(line)):
        if line[i].isnumeric():
            y.append(line[i])
            if i > len(line) - 2:
                continue
        elif line[i:i+3] and line[i:i+3] in three:
            y.append(line[i:i+3])
            if i > len(line) > len(line) - 3:
                continue
        elif line[i:i+4] and line[i:i+4] in four:
            y.append(line[i:i+4])
            if i > len(line) > len(line) - 4:
                continue
        elif line[i:i+5] and line[i:i+5] in five:
            y.append(line[i:i+5])


    x += (convert(y[0]) * 10) + convert(y[-1])

print(x)