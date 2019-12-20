#!/usr/bin/python3
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
print("Tuple 1 value "+str(tuple_1))
print("Tuple 2 value "+str(tuple_2))
r=tuple(map(lambda i, j: i + j, tuple_1, tuple_2))
print("Result"+str(r))
