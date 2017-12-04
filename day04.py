suma1 = 0
suma2 = 0
for i in open("day04.txt").read().split("\n"):
    # part1
    suma1 += (1 if sum(i.count(q) for q in i.split()) == len(i.split()) else 0)

    # part 2
    i = list(sorted(q) for q in i.split())
    suma2 += (1 if sum(i.count(q) for q in i) == len(i) else 0)

print(suma1, suma2)
