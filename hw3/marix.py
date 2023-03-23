import numpy as np


class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            raise ValueError
        if len(self.matrix) != 0 and len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError

        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(self.matrix[i])):
                new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(new_matrix)

    def __mul__(self, other):
        if len(other.matrix) != 0 and len(self.matrix) != len(other.matrix[0]):
            raise ValueError
        if len(self.matrix) != 0 and len(self.matrix[0]) != len(other.matrix):
            raise ValueError

        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(other.matrix[0])):
                q = 0
                for k in range(len(self.matrix[0])):
                    q += self.matrix[i][k] * other.matrix[k][j]
                new_matrix[i].append(q)
        return Matrix(new_matrix)

    def __matmul__(self, other):
        if len(self.matrix) != len(other.matrix):
            raise ValueError
        if len(self.matrix) != 0 and len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError

        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(self.matrix[i])):
                new_matrix[i].append(self.matrix[i][j] * other.matrix[i][j])
        return Matrix(new_matrix)


m1 = Matrix(np.random.randint(0, 10, (10, 10)))
m2 = Matrix(np.random.randint(0, 10, (10, 10)))

np.savetxt('artifacts/matrix+.txt', (m1+m2).matrix, fmt='%d')
np.savetxt('artifacts/matrix(mul).txt', (m1*m2).matrix, fmt='%d')
np.savetxt(r'artifacts/matrix@.txt', (m1@m2).matrix, fmt='%d')
