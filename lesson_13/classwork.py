import numpy as np

array = np.array([1, 2, 3, 4, 5])

print(array)
print(type(array))

array = np.arange(10)
print(array)

array = np.linspace(1, 10, 5)
print(array)

array = np.zeros((3, 4))
print(array)
print(array.ndim) # returns number of dimensions

array = np.ones((3, 3))
array = array * 7
print(array)

array = np.full((3, 5), fill_value=999)
print(array)

array = np.eye(5, 6)
print(array)

array = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
print(array.sum(axis=0))
print(array.sum(axis=1))


array = np.loadtxt("tasks.csv", delimiter=", ", skiprows=1, dtype=int)