suma = 0
for i in open("day02.txt").readlines():
    i = i.split("\t")
    for j in range(len(i)):
        i[j] = int(i[j])
    # ma = int(max(i))
    # mi = int(min(i))
    # print(ma, mi, (ma - mi))
    # suma += ma - mi
    print(i)
    for j in range(len(i)):
        for q in range(j + 1, len(i)):
            if i[j] % i[q] == 0:
                print("1", i[j] % i[q])
                suma += i[j] / i[q]
            if i[q] % i[j] == 0:
                print("2", i[q] % i[j])
                suma += i[q] / i[j]

print(suma)
