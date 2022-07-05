# Task 4.5 multiply even number in 100 to 1000
import functools

even_numbers = [even_number for even_number in range(100, 1001, 2)]


def mult_func(prev_el, el):
    return prev_el * el


print(functools.reduce(mult_func, even_numbers))
