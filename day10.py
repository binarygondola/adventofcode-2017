def movestart(l, n):
    tmp = l[n:]
    tmp.extend(l[:n])
    return tmp


rng = 256

lengths = list(int(x) for x in open("day10.txt").read().split(","))
tohash = [i for i in range(rng)]

skip = 0
moved = 0
for i in lengths:
    span = tohash[:i]
    span = list(span[::-1])
    span.extend(tohash[i:])
    tohash = span

    toskip = (skip + i) % rng
    moved -= toskip

    tohash = movestart(tohash, toskip)
    skip += 1

moved = moved % rng

tohash = movestart(tohash, moved)
print("part 1:", tohash[0] * tohash[1], "( skip =", skip, 'moved =', moved, ')')
'''
# '''

# part 2
lens = [ord(x) for x in open("day10.txt").read()]
lens.extend([17, 31, 73, 47, 23])

tohash = [x for x in range(rng)]

skip = 0
moved = 0
toright = 0

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
    char = tohash[i*16]
    for j in range(1, 16):
        char ^= tohash[i*16 + j]
    out += format(char, '02x')
print("part 2:", out)

