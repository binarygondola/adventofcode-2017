layers = list()

m = 0
for i in open("day13.txt"):
    layer, depth = map(int, i.rstrip().split(": "))
    layers.append([layer, depth, 0, -1])
    m = max(m, layer)
m += 1

l = [x[0] for x in layers]
idx = 0
busted = 0
for i in range(m):
    if i in l:
        if layers[idx][2] == 0:
            busted += i * layers[idx][1]
        idx += 1
    for j in layers:
        if j[2] == j[1] - 1 or j[2] == 0:
            j[3] *= -1
        j[2] += j[3]

print("part 1:", busted)

for x in layers:
    q = x[1] - 1
    t = 2 * q
    r = x[0] % t
    if r // q == 0:
        x[2] = r % q
        x[3] = 1
    else:
        x[2] = t - r
        x[3] = -1

count = 0
while True:
    busted = False
    for x in layers:
        x[2] += x[3]
        if x[2] == x[1] - 1 or x[2] == 0:
            x[3] *= -1
        if x[2] == 0:
            busted = True
    count += 1
    if not busted:
        break

print("part 2:", count)
