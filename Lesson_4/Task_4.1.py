# Task 4.1 wage script

import sys

n, hour, wage, prem = sys.argv
print(f'total wage: {int(hour) * int(wage) + int(prem)}$')
