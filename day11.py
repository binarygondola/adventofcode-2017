dirs = open("day11.txt").read().rstrip().split(",")

dist = 0

sw = dirs.count("sw")
n = dirs.count("n")
ne = dirs.count("ne")
nw = dirs.count("nw")
s = dirs.count("s")
se = dirs.count("se")

x, y, z = 0, 0, 0
maxes = list()

for d in dirs:
    if d == "n":
        x += 1
        z -= 1
    elif d == "s":
        x -= 1
        z += 1
    elif d == "ne":
        y += 1
        z -= 1
    elif d == "sw":
        y -= 1
        z += 1
    elif d == "nw":
        x += 1
        y -= 1
    elif d == "se":
        x -= 1
        y += 1
    else:
        pass
    maxes.append(max(x, y, z))

print("part 1:", max(x, y, z))
print("part 2:", max(maxes))
