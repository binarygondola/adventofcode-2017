file = open('day22.txt').read().split()

size = 400

dimx, dimy = len(file), len(file[0])
x, y = int(dimx / 2), int(dimy / 2)
x, y = x + size, y + size

# 0 1 2 3 are the directions, starting 0 is up, clockwise
facing = 0

lines = list()
for _ in range(size):
    lines.append("." * (2 * size + len(file)))
for a in range(len(file)):
    lines.append('.' * size + file[a] + '.' * size)
for _ in range(size):
    lines.append("." * (2 * size + len(file)))

copy = list()
for line in lines:
    copy.append(line)

add = 0

for _ in range(10000):
    if lines[y][x] == "#":
        facing += 1
        facing %= 4
        lines[y] = lines[y][:x] + '.' + lines[y][x + 1:]

    elif lines[y][x] == ".":
        facing -= 1
        facing %= 4
        lines[y] = lines[y][:x] + '#' + lines[y][x + 1:]
        add += 1

    if facing == 0:
        y -= 1
    elif facing == 1:
        x += 1
    elif facing == 2:
        y += 1
    elif facing == 3:
        x -= 1

print("part1:", add)

dimx, dimy = len(file), len(file[0])
x, y = int(dimx / 2), int(dimy / 2)
x, y = x + size, y + size
facing = 0
add = 0

lines = list()
for line in copy:
    lines.append(line)

for _ in range(10000000):
    if lines[y][x] == "#":  # infected
        facing += 1
        facing %= 4
        lines[y] = lines[y][:x] + 'F' + lines[y][x + 1:]

    elif lines[y][x] == "W":  # weakened
        lines[y] = lines[y][:x] + '#' + lines[y][x + 1:]
        add += 1

    elif lines[y][x] == "F":  # flagged
        facing += 2
        facing %= 4
        lines[y] = lines[y][:x] + '.' + lines[y][x + 1:]

    elif lines[y][x] == ".":  # clean
        facing -= 1
        facing %= 4
        lines[y] = lines[y][:x] + 'W' + lines[y][x + 1:]

    if facing == 0:
        y -= 1
    elif facing == 1:
        x += 1
    elif facing == 2:
        y += 1
    elif facing == 3:
        x -= 1

print("part2:", add)
