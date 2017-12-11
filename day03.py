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
    return tmp


number = int(open("day03.txt").read())

counter = 1
num = 1
distance = 2
while True:
    num += distance * 4
    distance += 2
    if num >= number:
        # print(distance)
        distance -= 2
        # print("dist:", distance)
        tmp = num - number
        print("part 1:", distance - (tmp - 3 * distance))
        break

x, y = 500, 500
array = np.zeros((1000, 1000))
distance = 2

array[x][y] = sumofadjacent(x, y, array)
x += 1

exit = False
while not exit:
    if exit:
        break
    for i in range(distance - 1):
        array[x][y] = sumofadjacent(x, y, array)
        if array[x][y] > number:
            exit = True
            break
        y -= 1
    if exit:
        break
    for i in range(distance):
        array[x][y] = sumofadjacent(x, y, array)
        if array[x][y] > number:
            exit = True
            break
        x -= 1
    if exit:
        break
    for i in range(distance):
        array[x][y] = sumofadjacent(x, y, array)
        if array[x][y] > number:
            exit = True
            break
        y += 1
    if exit:
        break
    for i in range(distance):
        array[x][y] = sumofadjacent(x, y, array)
        if array[x][y] > number:
            exit = True
            break
        x += 1
    if exit:
        break
    for i in range(2):
        array[x][y] = sumofadjacent(x, y, array)
        if array[x][y] > number:
            exit = True
            break
        x += 1
    if exit:
        break
    x -= 1
    distance += 2

print("part 2:", array[x][y])
