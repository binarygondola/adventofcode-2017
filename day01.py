file = open("day01.txt").read()
file = list(file)

l = len(file)
tmp = file[0]
sum = 0
for i in range(1, l):
    if file[i] == tmp:
        sum += int(tmp)
    tmp = file[i]

if tmp == file[-1]:
    sum += int(tmp)
print("part 1:", sum)


# part 2
half = int(l/2)
tmp = file[0]
sum = 0
for i in range(l - 1):
    if file[(i+half) % l] == tmp:
        sum += int(tmp)
    tmp = file[i+1]

if tmp == file[half-1]:
    sum += int(tmp)
print("part 2:", sum)

