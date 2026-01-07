# Primative VS Container(Reference) types

a = 16
b = a

print(id(a))
print(id(b))

a += 1

print(a)
print(b)

print(id(a))
print(id(b))

print("------------------")

a = [1, 2, 3]
b = a.copy()

print(id(a))
print(id(b))

print("------------------")

a = [[1, 2, 3], [5, 6]]
b = a.copy()

a[1].append(9)

print(a)
print(b)

print("------------------")

from copy import copy, deepcopy

a = [[1, 2, 3], [5, 6]]
b = deepcopy(a)

a[1].append(9)

print(a)
print(b)

print("------------------")

from collections import namedtuple

Color = namedtuple("Color", ["r", "g", "b"])

s1 = (10, 40, 241)

white = Color(r=255, g=255, b=255)
black = Color(0, 0, 0)

print(white.r)

print(white.index(255))

print(white.count(255))

print(black[2])

print(s1[0])






