
# 6. Create a random vector of size 30 and find the mean value.
# 7. Normalize a 5x5 random matrix.
# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).
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