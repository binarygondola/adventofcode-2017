suma1 = 0
suma2 = 0

for i in open("day02.txt").readlines():
    i = i.split("\t")
    for j in range(len(i)):
        i[j] = int(i[j])
    ma = int(max(i))
    mi = int(min(i))
    suma1 += ma - mi
    for j in range(len(i)):
        for q in range(j + 1, len(i)):
            if i[j] % i[q] == 0:
                suma2 += i[j] / i[q]
            if i[q] % i[j] == 0:
                suma2 += i[q] / i[j]

print("part 1:", suma1)
print("part 2:", suma2)
