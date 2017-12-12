connections = dict()

for i in open("day12.txt").read().split("\n"):
    a, bs = i.split(" <-> ")
    connections.setdefault(a, bs.split(", "))


vis = list('0')
tovisit = connections.pop('0')
tmp = tovisit
for i in tovisit:
    if i not in vis:
        vis.append(i)
        tovisit.extend(connections[i])

print("part 1:", len(vis))

# part 2
connections.setdefault('0', tmp)

groups = 0
while len(connections) > 0:
    poppedkey, poppedval = connections.popitem()
    vis = list(poppedval)
    for i in vis:
        if i in connections:
            pop = connections.pop(i)
            vis.extend(pop)
    groups += 1

print(groups)
