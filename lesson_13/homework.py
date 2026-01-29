
# 14. Solve the linear system \( Ax = b \) where \( A \) is a 3x3 matrix, and \( b \) is a 3x1 column vector.  
# 15. Given a 5x5 matrix, find the row-wise and column-wise sums.

import numpy

# Task 1
vector = numpy.arange(10, 50)
print(vector)


# Task 2
matrix = numpy.arange(9).reshape((3, 3))
print(matrix)


# Task 3
matrix = numpy.eye(3, 3)
print(matrix)


# Task 4
matrix = numpy.random.randint(1, 100, (3, 3, 3))
print(matrix)


# Task 5
matrix = numpy.random.randint(1, 100, (10, 10))
max_number = matrix.max()
min_number = matrix.min()
print(matrix)
print(max_number)
print(min_number)


# Task 6
matrix = numpy.random.randint(1, 100, 30)
mean_value = round(matrix.sum() / matrix.size, 2)
print(matrix)
print(mean_value)


# Task 7
matrix = numpy.random.randint(1, 100, (5, 5))
norm = numpy.linalg.norm(matrix)
normalized_matrix = matrix / norm
print(matrix)
print(normalized_matrix)


# Task 8
matrix1 = numpy.random.randint(1, 10, (5, 3))
matrix2 = numpy.random.randint(1, 10, (3, 2))

new_matrix = matrix1 @ matrix2
print(matrix1)
print(matrix2)
print(new_matrix)


# Task 9
matrix1 = numpy.random.randint(1, 10, (3, 3))
matrix2 = numpy.random.randint(1, 10, (3, 3))

matrix_result = numpy.dot(matrix1, matrix2)
print(matrix_result)


# Task 10
matrix = numpy.random.randint(1, 10, (4, 4))
transposed_matrix = matrix.transpose()
print(matrix)
print(transposed_matrix)


# Task 11
matrix = numpy.random.randint(1, 10, (3, 3))
determinant = numpy.linalg.det(matrix)

print(matrix)
print(determinant)


# Task 12
matrix1 = numpy.random.randint(1, 10, (3, 4))
matrix2 = numpy.random.randint(1, 10, (4, 3))

matrix_result = matrix1 @ matrix2


# Task 13
matrix1 = numpy.random.randint(1, 10, (3, 3))
vector = numpy.array([3, 7, 9])

matrix_result = matrix1 * vector
print(matrix_result)


# Task 15
matrix = numpy.random.randint(1, 10, (5, 5))
row_wise_sum = matrix.sum(axis=0)
column_wise_sum = matrix.sum(axis=1)

print(matrix)
print(row_wise_sum)
print(column_wise_sum)

