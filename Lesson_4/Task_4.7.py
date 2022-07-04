# Task 4.7 
from math import factorial


def gen_fact(n):
    for el in range(1, n + 1):
        yield factorial(el)


for el in gen_fact(6):
    print(el)
