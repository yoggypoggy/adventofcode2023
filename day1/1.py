with open('input') as f:
    stuff = [line for line in f]

x = 0

for line in stuff:
    y = []
    for letter in line:
        if letter.isnumeric():
            y.append(letter)
    x += (int(y[0]) * 10) + int(y[-1])

print(x)