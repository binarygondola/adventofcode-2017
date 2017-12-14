def movestart(l, n):
    tmp = l[n:]
    tmp.extend(l[:n])
    return tmp


def getHash(s):
    rng = 256
    lens = [ord(x) for x in s]
    lens.extend([17, 31, 73, 47, 23])

    tohash = [x for x in range(rng)]

    skip = 0
    moved = 0

    for _ in range(64):
        # moved = 0
        tohash = movestart(tohash, -moved)
        for i in lens:
            span = tohash[:i]
            span = span[::-1]
            span.extend(tohash[i:])
            tohash = list(span)

            toskip = (skip + i) % rng
            moved -= toskip

            tohash = movestart(tohash, toskip)
            skip += 1

        moved = moved % rng
        tohash = movestart(tohash, moved)

    out = ''
    for i in range(16):
        char = tohash[i * 16]
        for j in range(1, 16):
            char ^= tohash[i * 16 + j]
        out += format(char, '02x')
    return out


def bits(b):
    a = ''
    for ib in range(3):
        d = 2 ** (3 - ib)
        a += str(b // d)
        b %= d
    a += str(b % 2)
    return a


def remove(x, y, g):
    g[x] = g[x][:y] + '0' + g[x][y+1:]
    if g[x+1][y] == '1':
        remove(x+1, y, g)
    if g[x][y+1] == '1':
        remove(x, y+1, g)
    if g[x-1][y] == '1':
        remove(x-1, y, g)
    if g[x][y-1] == '1':
        remove(x, y-1, g)


grid = list()

# boundaries
grid.append("0"*130)

string = open("day14.txt").read()
count = 0
for i in range(128):
    s = getHash(string + "-" + str(i))
    tmp = '0'
    for j in s:
        j = ord(j)
        if j >= ord('a'):
            j -= ord('a')
            j += 10
        else:
            j -= ord('0')
        tmp += bits(j)

    tmp += '0'
    grid.append(tmp)
    for x in tmp:
        if x == '1':
            count += 1

print("part 1:", count)

# boundaries
grid.append("0"*130)

groups = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '1':
            groups += 1
            remove(i, j, grid)

print("part 2:", groups)
