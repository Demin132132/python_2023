import numpy as np
import sys


#функция взята из https://stackoverflow.com/questions/45393694/size-of-a-dictionary-in-bytes
def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


class Matrix():
    cache = {}

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

        hash = self.__hash__() + other.__hash__()
        if hash in Matrix.cache:
            return Matrix.cache[hash]

        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(other.matrix[0])):
                q = 0
                for k in range(len(self.matrix[0])):
                    q += self.matrix[i][k] * other.matrix[k][j]
                new_matrix[i].append(q)

        Matrix.cache[hash] = Matrix(new_matrix)

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

    def __hash__(self):
        # get_size - вес объекта в байтах
        return get_size(self) + sum(
            10 ** (i) * sum(10 ** (j) * self.matrix[i][j] for j in range(len(self.matrix[i]))) for i in range(len(self.matrix))
        )


A = Matrix([[1,2,1], [1,1,1], [1,1,1]])
C = Matrix([[11,1,1], [1,1,1], [1,1,1]])
B = Matrix([[1,0,1], [1,1,1], [1,1,1]])
D = Matrix([[1,0,1], [1,1,1], [1,1,1]])
AB = A * B
Matrix.cache = {}
CD = C * D


np.savetxt('artifacts/hard/A.txt', A.matrix, fmt='%d')
np.savetxt('artifacts/hard/B.txt', B.matrix, fmt='%d')
np.savetxt(r'artifacts/hard/C.txt', C.matrix, fmt='%d')
np.savetxt('artifacts/hard/AB.txt', AB.matrix, fmt='%d')
np.savetxt(r'artifacts/hard/CD.txt', CD.matrix, fmt='%d')

