class Kletka():
    def __init__(self, numb_cells):
        self.numb_cells = numb_cells

    def __add__(self, other):
        return Kletka(self.numb_cells + other.numb_cells)

    def __sub__(self, other):
        sub_cells = self.numb_cells - other.numb_cells
        if sub_cells > 0:
            return Kletka(sub_cells)
        else:
            return Kletka(0)
            print('Subtraction is impossible, difference < 0')

    def __mul__(self, other):
        return Kletka(self.numb_cells * other.numb_cells)

    def __truediv__(self, other):
        return Kletka(self.numb_cells // other.numb_cells)

    def make_order(self, numb_in_row):
        full_clast = self.numb_cells // numb_in_row
        remainder = self.numb_cells % numb_in_row
        result = ""
        for clast_cell in range(full_clast):
            result += '*' * numb_in_row + '\n'
        result += '*' * remainder
        return result + '\n'


a1 = Kletka(9)
a2 = Kletka(6)
a3 = Kletka(5)

a4 = a1 + a2 + a3
a5 = a4 * a2
a6 = a1 / a2
a7 = a2 - a1

print(a4.make_order(3))
print(a5.make_order(7))
print(a6.make_order(3))
print(a7.make_order(6))
