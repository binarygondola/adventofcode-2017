registers = dict()
maxes = list()
for i in open("day08.txt").read().split("\n"):
    reg, regfunc, regamount, _, comparereg, compareregsign, compareregamount = i.split(" ")
    compareregamount = int(compareregamount)
    regamount = int(regamount)

    registers.setdefault(comparereg, 0)
    registers.setdefault(reg, 0)

    func = lambda x, a: x+a if regfunc == "inc" else x - a
    
    e = str(registers[comparereg]) + compareregsign + str(compareregamount)
    if eval(e):
        registers[reg] = func(registers[reg], regamount)

    maxes.append(max(registers[key] for key in registers))

# part 1
print("part 1:", max(registers[key] for key in registers))

# part 2
print("part 2:", max(maxes))
