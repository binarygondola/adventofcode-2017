import math


def rotate2(a):
    a = list(a)
    a[0], a[1], a[3], a[4] = a[3], a[0], a[4], a[1]
    a = ''.join(a)
    return a


def rotate3(a):
    s = ['/']
    a = list(a)
    left = a[0:9:4]
    middle = a[1:10:4]
    right = a[2:11:4]
    a = left[::-1] + s + middle[::-1] + s + right[::-1]
    a = ''.join(a)
    return a


def flip3(a):
    a = list(a)
    s = ['/']
    t1 = a[8:] + s + a[4:7] + s + a[:3]
    t2 = a[:3][::-1] + s + a[4:7][::-1] + s + a[8:][::-1]
    return ''.join(t1), ''.join(t2)


def rot2(a):
    l = list()
    l.append(a)
    for _ in range(3):
        a = rotate2(a)
        l.append(a)
    return l


def rot3(a):
    l = list()
    l.append(a)
    l.extend(flip3(a))
    for _ in range(3):
        a = rotate3(a)
        l.append(a)
        l.extend(flip3(a))
    return l


def img(a):
    return a.replace('/', '\n')


def split2(a):
    t = a.split('/')
    prod = list()

    for x in range(0, len(t), 2):
        for y in range(0, len(t), 2):
            prod.append(t[x][y:y + 2] + '/' + t[x + 1][y:y + 2])

    return prod


def split3(a):
    t = a.split('/')
    prod = list()

    for x in range(0, len(t), 3):
        for y in range(0, len(t), 3):
            prod.append(t[x][y:y + 3] + '/' + t[x + 1][y:y + 3] + '/' + t[x + 2][y:y + 3])

    return prod


def convert2(a):
    # print(img(a))

    tmp = []
    for x in split2(a):
        tmp.extend([tupl[1].split('/') for tupl in productions if tupl[0] == x])

    tmp2 = []

    # print(len(tmp))

    if len(tmp) == 4:
        for w in range(2):
            for q in range(3):
                tmp2.append(tmp[w * 2][q] + tmp[w * 2 + 1][q])
    else:
        for w in range(3):
            for q in range(3):
                tmp2.append(tmp[w * 3][q] + tmp[w * 3 + 1][q] + tmp[w * 3 + 2][q])

    # print(img('/'.join(tmp2)))
    return '/'.join(tmp2)


def dostep(a):
    l = a.split('/')
    if len(l[0]) == 3:
        for x in productions:
            if a == x[0]:
                return x[1]
    elif len(l[0]) == 4:
        return convert2(a)
    elif len(l[0]) == 6:
        return convert2(a)


def extendme(a):
    tmp = []
    for x in split3(a):
        tmp.append(dostep(x))
    return tmp

productions = list()

for i in open('day21.txt').read().split('\n'):
    i = i.split(' => ')
    if len(i[0]) == 5:
        for x in rot2(i[0]):
            if (x, i[1]) not in productions:
                productions.append((x, i[1]))
    else:
        for x in rot3(i[0]):
            if (x, i[1]) not in productions:
                productions.append((x, i[1]))


start = '.#./..#/###'

for _ in range(5):
    if isinstance(start, list):
        for q in range(len(start)):
            start[q] = dostep(start[q])
    elif len(start) == 89:
        start = split3(start)
        for q in range(len(start)):
            start[q] = dostep(start[q])
    else:
        start = dostep(start)

add = 0
for w in start:
    add += w.count('#')
print('part1:', add)

start = ['.#./..#/###']

for q in range(18):
    if len(start[0]) == 89:
        tmp = []
        for x in range(len(start)):
            tmp.extend(extendme(start[x]))
        start = tmp
    else:
        for x in range(len(start)):
            start[x] = dostep(start[x])

add = 0
for w in start:
    add += w.count('#')
print('part2:', add)
