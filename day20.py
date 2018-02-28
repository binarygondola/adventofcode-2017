import math


class Vector3(object):
    def __init__(self, l):
        self.x = l[0]
        self.y = l[1]
        self.z = l[2]

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __repr__(self):
        return '<' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + '>'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Particle(object):
    def __init__(self, id, p, v, a):
        self.p = Vector3(p)
        self.v = Vector3(v)
        self.a = Vector3(a)
        self.id = id

    def __repr__(self):
        return 'p=' + str(self.p) + ', ' + \
               'v=' + str(self.v) + ', ' + \
               'a=' + str(self.a)

    def update(self):
        self.v += self.a
        self.p += self.v


def dist(v1, v2):
    v1 = v1.p
    v2 = v2.p
    return math.sqrt(math.pow(abs(v1.x - v2.x), 2) +
                     math.pow(abs(v1.y - v2.y), 2) +
                     math.pow(abs(v1.z - v2.z), 2))


def removecollisions(particles):
    positions = list()
    newlistofparticles = list()
    todelete = list()
    for particle in particles:
        if particle.p in positions:
            pos = positions.index(particle.p)
            if pos not in todelete:
                todelete.append(pos)
        else:
            positions.append(particle.p)
            newlistofparticles.append(particle)
    for i in range(len(todelete)):
        del newlistofparticles[todelete[i] - i]
    return newlistofparticles


l = ['p', 'v', 'a']
idx = 0
particles = list()

for i in open("day20.txt").read().split("\n"):
    i = i.split(', ')
    for x in range(3):
        tmp = list(map(int, i[x][3:-1].split(",")))
        l[x] = tmp
    particles.append(Particle(idx, l[0], l[1], l[2]))
    idx += 1

z = [0, 0, 0]
zero = Particle(-1, z, z, z)

minimum = 2 ** 32 - 1
answer = -1

for j in range(40):
    for i in particles:
        d = dist(i, zero)
        if d < minimum:
            minimum = d
            answer = i.id
        i.update()
    minimum = 2 ** 32 - 1
    particles = removecollisions(particles)

# without removecollisions and with at least 350 iteratioins
# the proper answer for part 1 is 170
print('part1:', answer)
# for part 2 the answer is 571 (40 iterations)
print('part2:', len(particles))
