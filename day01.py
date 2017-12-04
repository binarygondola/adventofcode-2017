file = open("day01.txt").read()


# part 2
l = len(file)
half = int(l/2)
tmp = file[0]
sum = 0
for i in range(len(file) - 1):
    if file[(i+half) % l] == tmp:
        sum += int(tmp)
    tmp = file[i+1]

if tmp == file[half-1]:
    sum += int(tmp)
print("endsum =", sum)

