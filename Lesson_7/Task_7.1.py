class Matrix():

    def __init__(self, inp_matrix):
        total_row = len(inp_matrix)
        self.inp_matrix = inp_matrix
        if total_row > 0:
            row_1 = inp_matrix[0]
        else:
            raise  # matrix is Empty
        for row in inp_matrix:
            if len(row) != len(row_1):
                raise  # length of matrix rows are diferent
        for el in row:
            if isinstance(el, int):
                pass
            else:
                raise  # elemets of matrix are not int

    def __str__(self):
        result = ""
        for row in self.inp_matrix:
            for el in row:
                result += str(f'{el}\t')
            result += '\n'
        return result

    def __add__(self, other):
        x_row = []
        x = []
        if len(self.inp_matrix[0]) != len(self.inp_matrix[0]):
            raise  # matrixs have different number of coulmns
        if len(self.inp_matrix) != len(other.inp_matrix):
            raise  # matrixs have different number of rows
        for i in range(len(self.inp_matrix)):
            for j in range(len(self.inp_matrix[0])):
                x_row.append(self.inp_matrix[i][j] + other.inp_matrix[i][j])
            x.append(x_row.copy())
            x_row.clear()
        return Matrix(x)


a = [[3, 5, 32], [2, 4, 6], [-1, 64, -8], [-1, 64, -8]]
b = [[1, 1, 1], [1, 2, 1], [0, -64, -8], [0, 0, 0]]
c = [[3, 4, 6, 1, 2], [2, 3, 5, 1, 3]]
d = [[3, 4, 6, 1, 2], [2, 3, 5, 1, 3]]
mat_1 = Matrix(a)
mat_2 = Matrix(b)
mat_3 = Matrix(c)
mat_4 = Matrix(d)

print(str(mat_1))
print(str(mat_2))
print(str(mat_1 + mat_2))
print(type(mat_1 + mat_2))

print(str(mat_3))
print(str(mat_4))
print(str(mat_3 + mat_4))
