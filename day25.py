# tuple (do if 0, do if 1)
# do if is a triple (write_1or0, move_L/R, next_state)
def get_state_function(desc):
    desc = desc.split('\n')
    x = 2
    doif0 = (int(desc[x][-2]), 1 if desc[x + 1][-3] == 'h' else -1, str(desc[x + 2][-2][0]))
    x = 6
    doif1 = (int(desc[x][-2]), 1 if desc[x + 1][-3] == 'h' else -1, str(desc[x + 2][-2][0]))
    return doif0, doif1


def perform_action(a):
    tape_ = a[0]
    idx = a[1]
    state = a[2]

    do = states[state][tape_[idx]]
    tape_[idx] = do[0]

    if do[1] + idx > len(tape_) - 1:
        tape_.append(0)
    elif do[1] + idx < 0:
        tape_ = [0] + tape_
        idx += 1
    tape_[idx] = do[0]
    idx += do[1]
    state = do[2]

    triple = tape_, idx, state
    return triple


file = open('day25.txt').read().split('\n\n')

states = dict()

for x in range(1, len(file)):
    states[chr(ord('A') + x - 1)] = get_state_function(file[x])

file = file[0].split('\n')
state = file[0][-2]
steps = int(file[1].split(" ")[-2])

tape = [0]
idx = 0

triple_state = [tape, idx, state]

for _ in range(steps):
    triple_state = perform_action(triple_state)

print('part1:', sum(triple_state[0]))
print('part2:', 'no part2!')
