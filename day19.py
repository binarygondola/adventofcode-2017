lines = open("day19.txt").read().split("\n")
m = max(len(i) for i in lines)

for i in range(len(lines)):
    lines[i] = lines[i] + ' ' * (m - len(lines[i]))
    lines[i] = ' ' + lines[i] + ' '

x = lines[0].index("|")
y = 0
vertical = True
add = 1

print("part1: ", end='')
count = 0

while True:
    count += 1

    if vertical:
        y += add
    else:
        x += add

    if lines[y][x] == '|' or lines[y][x] == '-':
        continue
    elif lines[y][x] == '+':
        if vertical:
            vertical = False
            if lines[y][x + 1] == ' ':
                add = -1
            elif lines[y][x - 1] == ' ':
                add = 1
        else:
            vertical = True
            if lines[y + 1][x] == ' ':
                add = -1
            elif lines[y - 1][x] == ' ':
                add = 1
    elif lines[y][x] == ' ':
        break
    else:
        print(lines[y][x], end='')

print()
print('part2:', count)
