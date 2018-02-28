def make_bridge(parts, current, end, m):
    possible = [x for x in parts if end == x[0] or end == x[1]]
    for p in possible:
        parts.remove(p)
        current.append(p)

        if end == p[0]:
            tmp = p[1]
        else:
            tmp = p[0]

        b = sum(sum(x) for x in current)
        max_length = max(b, m[0])

        parts_len_max = m[1]
        longest_max_length = m[2]

        if len(current) > parts_len_max:
            parts_len_max = len(current)
            longest_max_length = b

        elif len(current) == parts_len_max:
            longest_max_length = max(b, m[2])

        triple = [max_length, parts_len_max, longest_max_length]

        m = make_bridge(parts, current, tmp, triple)
        current.remove(p)
        parts.append(p)
    return m


file = open('day24.txt').read().split('\n')

parts = []

for i in file:
    a = list(map(int, i.split('/')))
    a.sort()
    parts.append(a)

parts.sort()

mm = make_bridge(parts, [], 0, [0, 0, 0])
print("part1:", mm[0])
print("part2:", mm[2])
