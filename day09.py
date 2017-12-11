s = str(open("day09.txt").read())

add = 0
nest = 0
garbo = False

# for part 2
chars = 0

idx = 0
while idx < len(s):
    if s[idx] == "!":
        idx += 2
        continue
    if garbo:
        chars += 1
        if s[idx] == '>':
            garbo = False
            chars -= 1
        idx += 1
        # part 2
    else:
        if s[idx] == "<":
            garbo = True
        elif s[idx] == '{':
            nest += 1
        elif s[idx] == '}':
            add += nest
            nest -= 1
        idx += 1

print("part 1:", add)
print("part 2:", chars)
