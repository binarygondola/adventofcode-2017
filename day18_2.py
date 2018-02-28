import queue


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


reg0, reg1 = dict(), dict()
reg0['p'] = 0
reg1['p'] = 1

q0, q1 = queue.Queue(), queue.Queue()

commands = list()
for i in open("day18.txt").read().strip().split("\n"):
    commands.append(i)

idx0, idx1 = 0, 0

inprog0 = True

reg = reg0
idx = idx0

waitingfor0, waitingfor1 = False, False
waitreg0, waitreg1 = None, None

add = 0

while True:
    if commands[idx] == 'jgz 1 3':
        idx += 3
        continue
    i = commands[idx].split(" ")
    reg.setdefault(i[1], 0)
    reg.setdefault("freq"+i[1], 0)
    r = i[1]

    if len(i) == 2:
        if i[0] == 'snd':
            if inprog0:
                q0.put(int(reg[i[1]]))
                if waitingfor0:
                    reg1[waitreg1] = q0.get()
                    waitingfor0 = False
            else:
                add += 1
                q1.put(int(reg[i[1]]))
                if waitingfor1:
                    reg0[waitreg0] = q1.get()
                    waitingfor1 = False

        elif i[0] == 'rcv':
            if inprog0:
                if q1.empty():
                    reg0 = reg
                    idx0 = idx
                    idx = idx1
                    reg = reg1
                    waitingfor1 = True
                    waitreg1 = i[1]
                    inprog0 = False
                else:
                    reg[i[1]] = q1.get()
            else:
                if q0.empty():
                    reg1 = reg
                    idx1 = idx
                    idx = idx0
                    reg = reg0
                    waitingfor0 = True
                    waitreg0 = i[1]
                    inprog0 = True
                else:
                    reg[i[1]] = q0.get()

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

    if waitingfor1 and waitingfor0:
        break

print('part2:', add)
