num = int(open("day17.txt").read().strip())

vals = [0]
# before 0, after 0
j = 0

for i in range(2017):
    idx = (num + j) % len(vals)
    j = idx + 1
    vals = vals[0: j] + [i + 1] + vals[j:]

print('part 1:', vals[vals.index(2017) + 1])

k = 0
numbercount = 1
ans = 0
for i in range(50 * 1000 ** 2):
    idx = (num + k) % numbercount
    k = idx + 1
    if idx == 0:
        ans = i + 1
    numbercount += 1

print("part 2:", ans)
