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

print(search)
