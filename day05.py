idx = 0
steps = 0

values = list(int(i) for i in open("day05.txt").read().split())
# part 1
while True:
    values[idx] += 1
    idx += values[idx] - 1
    steps += 1
    if idx >= len(values):
        break

print("steps part 1:", steps)

# part 2

idx = 0
steps = 0

values = list(int(i) for i in open("day05.txt").read().split())

while True:
    if values[idx] < 3:
        values[idx] += 1
        idx += values[idx] - 1
    else:
        values[idx] -= 1
        idx += values[idx] + 1
    steps += 1
    if idx >= len(values):
        break

# print(values)
# print(idx, len(values))

print("steps part 2:", steps)
