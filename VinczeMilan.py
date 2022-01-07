from bisect import bisect_left, bisect_right
import numpy as np
from scipy.linalg import block_diag

#Exercise 1
def cubes(inputArray):
    surfArea = 0
    for colN in range(len(inputArray)):
        left_sides_exposed = colN - 1 >= 0 and inputArray[colN] - inputArray[colN - 1] or inputArray[colN]
        right_sides_exposed = colN + 1 < len(inputArray) and inputArray[colN] - inputArray[colN + 1] or inputArray[colN]
        if left_sides_exposed > 0:
            surfArea += left_sides_exposed
        if right_sides_exposed > 0:
            surfArea += right_sides_exposed
    surfArea += sum(inputArray)*2
    surfArea += len(inputArray)*2
    return surfArea

print("The surface area of the cubes: ")
print(cubes([3,1,2]))

#Exercise 2
def find_diagonal(np_array):
    for i in range(-len(np_array), len(np_array)):
        if 'Q' in np.diagonal(np_array, i):
            return i

def rindex(mylist, myvalue):
    if myvalue in mylist:
        return len(mylist) - mylist[::-1].index(myvalue) - 1
    return -1


def count_list(lst):
    first, second = [i.split() for i in ' '.join(lst).split('Q')]
    right_index = rindex(first, 'X')
    left_index = 'X' in second and second.index('X') or -1
    if right_index > 0:
        first = first[bisect_left(first, 'X'):]
    if left_index and left_index > 0:
        second = second[bisect_right(second, 'X'):]
    return first + second


def queen(n, r_q, c_q, obstacles):
    can_attack = 0
    table = [[0] * n for i in range(n)]
    for obstaclePos in obstacles:
        table[n - obstaclePos[0]][obstaclePos[1] - 1] = "X"
    table[n - r_q][c_q - 1] = "Q"

    np_table = np.flipud(np.asarray(table))
    diagonal1 = np_table.diagonal(find_diagonal(np_table))
    np_table = np.fliplr(np_table)
    diagonal2 = np_table.diagonal(find_diagonal(np_table))
    can_attack += count_list(diagonal1).count('0')
    can_attack += count_list(diagonal2).count('0')
    np_table = np.fliplr(np_table)
    can_attack += count_list(np_table[:, r_q-1]).count('0')
    can_attack += count_list(np_table[:, c_q-1]).count('0')

    return can_attack

print("The number of squares the queen can attack: ")
print(queen(10, 4, 4, [[3, 5]]))

#Exercise 3
def chessboard(value):
    a = []
    for i in range(value*value):
        if i % 2 == 0:
            a.append(1)
        else:
            a.append(-1)
    nparray = np.vstack(a).reshape((value, value))
    return nparray

print("Custom made chessboard: ")
print(chessboard(11))

#Exercise 4
def euclidean_norm(a, b):
    point1 = np.array([a])
    point2 = np.array([b])
    dist = np.linalg.norm(point2-point1)
    return round(dist, 4)

print("The Euclidean norm of a line: ")
print(euclidean_norm([1,2], [3,4]))

#Exercise 5
def block_matrix(list_of_matrices):
    matrix = block_diag(*list_of_matrices)
    return matrix

print("The block matrix of a list of square matices")
print(block_matrix([[[1,2],[2,3]], [[1,3],[4,5]], [[7,8],[2,1]]]))

#Exercise 6
def cookies_got(money, price, wrap):
    cookies = 0
    cookies += int(money / price)
    money = int(((money / price) / wrap) * price)
    if money == 1:
        return cookies
    else:
        cookies += cookies_got(money, price, wrap)
    return cookies

print("The number of cookies: ")
print(cookies_got(16, 2, 2))
