
# 9. Create two 3x3 matrices and compute their dot product.  
# 10. Given a 4x4 matrix, find its transpose.  
# 11. Create a 3x3 matrix and calculate its determinant.  
# 12. Create two matrices \( A \) (3x4) and \( B \) (4x3), and compute the matrix product \( A \cdot B \).  
# 13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.  
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


# Task 9
