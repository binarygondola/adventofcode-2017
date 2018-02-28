def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


reg = dict()

commands = list()
for i in open("day18.txt").read().strip().split("\n"):
    commands.append(i)

idx = 0
while True:
    i = commands[idx].split(" ")
    reg.setdefault(i[1], 0)
    reg.setdefault("freq"+i[1], 0)
    r = i[1]

    if len(i) == 2:
        if i[0] == 'snd':
            reg['freq'+i[1]] = int(reg[i[1]])

        elif i[0] == 'rcv':
            if reg[i[1]] != 0 and reg['freq'+i[1]] != 0:
                print('part 1:', reg['freq'+i[1]])
                break
    else:
        if is_number(i[2]):
            v = int(i[2])
        else:
            v = reg[i[2]]

        if i[0] == 'mul':
            reg[r] *= v

        elif i[0] == 'mod':
            reg[r] %= v

        elif i[0] == 'set':
            reg[r] = v

        elif i[0] == 'add':
            reg[r] += v

        elif i[0] == 'jgz':
            tmp = reg[i[1]]
            if tmp > 0:
                idx += v
                idx -= 1
    idx += 1
