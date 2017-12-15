a, b = open("day15.txt").read().splitlines()
a, b = int(a.split(" ")[-1]), int(b.split(" ")[-1])

A, B = 16807, 48271
m = 2147483647

count = 0
for _ in range(40000000):
    a = a * A % m
    b = b * B % m

    if a % 2**16 == b % 2**16:
        count += 1

print("part 1:", count)

a, b = open("day15.txt").read().splitlines()
a, b = int(a.split(" ")[-1]), int(b.split(" ")[-1])

count = 0
for _ in range(5000000):
    a = a * A % m
    while a % 4 != 0:
        a = a * A % m

    b = b * B % m
    while b % 8 != 0:
        b = b * B % m

    if a % 2**16 == b % 2**16:
        count += 1

print("part 2:", count)
