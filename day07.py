# for part 2
def calculatemass(dict, item):
    top = d[item].get('top')
    d[item]['all'] = d[item]['w']
    if top is not None:
        d[item]['all'] += sum(calculatemass(dict, x) for x in top)
    return d[item]['all']


d = dict()

for i in open("day07.txt").read().split("\n"):
    i = i.split(" ")
    d.setdefault(i[0], dict())['w'] = int(i[1][1:-1])
    d.setdefault(i[0], dict())['all'] = 0
    if len(i) != 2:
        d.setdefault(i[0], dict())['top'] = [x.replace(",", "") for x in i[3::1]]

# part 1
search = next(iter(d))

done = False
while not done:
    done = True
    for q in d:
        a = d[q].get('top')
        if a is not None and search in a:
            search = q
            done = False

print("On the bottom of the tower is:", search)

# part 2

d[search]['all'] = calculatemass(d, search)

prevmasses = [(d[i]['all'], i) for i in d[search]['top']]
while True:
    mass = d[search]['all']
    masses = [(d[i]['all'], i) for i in d[search]['top']]
    masses.sort(key=lambda x: x[0])
    if masses[0][0] == masses[-1][0]:
        print(search, "has the bad weight", d[search]['w'], "it should be",
              d[search]['w'] + (prevmasses[0][0] - d[search]['all']), "instead")
        break

    prev = search
    prevmasses = list(masses)
    if masses[0][0] != masses[1][0]:
        search = masses[0][1]
    elif masses[-1][0] != masses[1][0]:
        search = masses[-1][1]



