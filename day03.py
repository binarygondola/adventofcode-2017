import numpy as np


def sumofadjacent(x, y, array):
    # print(x, y)
    tmp = 0
    tmp += array[x + 1][y]
    tmp += array[x + 1][y + 1]
    tmp += array[x + 1][y - 1]
    tmp += array[x][y + 1]
    tmp += array[x][y - 1]
    tmp += array[x - 1][y]
    tmp += array[x - 1][y + 1]
    tmp += array[x - 1][y - 1]
    if x == 500 and y == 500:
        tmp += 1
    # print(tmp)
    return tmp


number = int(open("day03.txt").read())

print(number)

counter = 1
num = 1
distance = 2
while True:
    num += distance * 4
    distance += 2
    print(num, distance)
    if num >= number:
        # print(distance)
        distance -= 2
        # print("dist:", distance)
        tmp = num - number
        # print("ans:", distance - (tmp - 3 * distance))
        break

print(num - number)

x, y = 500, 500
array = np.zeros((1000, 1000))
distance = 2

array[x][y] = sumofadjacent(x, y, array)
x += 1

while True:
    for i in range(distance - 1):
        array[x][y] = sumofadjacent(x, y, array)
        y -= 1
    for i in range(distance):
        array[x][y] = sumofadjacent(x, y, array)
        x -= 1
    for i in range(distance):
        array[x][y] = sumofadjacent(x, y, array)
        y += 1
    for i in range(distance):
        array[x][y] = sumofadjacent(x, y, array)
        x += 1
    for i in range(2):
        array[x][y] = sumofadjacent(x, y, array)
        x += 1
    x -= 1
    distance += 2
    input()
