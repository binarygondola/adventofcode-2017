registers = [int(i) for i in open("day06.txt").read().split("\t")]
states = list()
l = len(registers)

while registers not in states:
    tmp = list(registers)
    states.append(tmp)
    idx = registers.index(max(registers))
    value = registers[idx]
    registers[idx] = 0
    while value > 0:
        idx = (idx + 1) % l
        registers[idx] += 1
        value -= 1

print("part 1:", len(states))

print("part 2:", len(states) - states.index(registers))
