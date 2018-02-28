def spin(vals, val):
    l = len(vals)
    return vals[l - val:] + vals[:l - val]


def exchange(vals, a, b):
    vals[a], vals[b] = vals[b], vals[a]
    return vals


def partner(vals, a, b):
    A = vals.index(a)
    B = vals.index(b)
    vals[A], vals[B] = vals[B], vals[A]
    return vals


def execute(vals, comm):
    if comm[0] == 's':
        vals = spin(vals, int(comm[1:]))
    elif comm[0] == 'p':
        a, b = map(str, comm[1:].split("/"))
        vals = partner(vals, a, b)
    elif comm[0] == 'x':
        a, b = map(int, comm[1:].split("/"))
        vals = exchange(vals, a, b)
    return vals


commands = open("day16.txt").read().split(",")

start = [chr(x) for x in range(ord('a'), ord('a') + 16)]
states = list()

for i in commands:
    start = execute(start, i)

print("part 1:", "".join(start))

bil = 1000000000

for j in range(bil - 1):
    if start in states:
        break
    else:
        states.append(start)

    for i in commands:
        start = execute(start, i)

cycle = len(states)

print("part 2:", "".join(states[bil % cycle - 1]))
