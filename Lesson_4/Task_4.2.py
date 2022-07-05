# Task 4.2 transform some list
x = [202, 22, 123, 321, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([z for y, z in enumerate(x) if y != 0 and z > x[y - 1]])
