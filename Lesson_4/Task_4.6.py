# Task 4.6 some scripts
from sys import argv
import itertools

name, start_numb, cycle_var = argv
start_numb = int(start_numb)
for i in itertools.count(start_numb):
    print(i)
    if i > start_numb + 15:
        break
count = 0
cycle_var = [1, 2, 53, 4, 6]
for i in itertools.cycle(cycle_var):
    if count < 7:
        print(i)
        count += 1
    else:
        break
