lengths = list(int(x) for x in open("day10.txt").read().split(","))
tohash = [i for i in range(256)]

skip = 0
moved = 0
for i in lengths:
    span = tohash[0:i]
    span = list(span[::-1])
    span.extend(tohash[i:])
    tohash = span

    toskip = (skip + i) % 256
    moved -= toskip

    tmp = tohash[toskip:]
    tmp.extend(tohash[0: toskip])
    tohash = list(tmp)
    skip += 1

moved = moved % 256

print("part 1:", tohash[moved] * tohash[moved + 1])
