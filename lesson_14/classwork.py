import numpy as np

vectorA = np.array([4, 5, 5, 2, 2, 2])

vectorB = np.array([3, 2, 3 ,45, 35, 91])

@np.vectorize
def multiply(a, b):
    return a*b

print(vectorA * vectorB)
print(multiply(vectorA, vectorB))


chosen = np.random.choice(vectorB)
print(chosen)

chosen = np.random.choice(vectorB, size=3)
print(chosen)

np.random.shuffle(vectorB)
print(vectorB)

permuted = np.random.permutation(vectorB)
print(permuted)

array = np.array([1,2,3,4,5])
print(array[array >= 3])

array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

whereUsage = np.where(array > 3, array, -1)
print(whereUsage)

rng = np.random.default_rng()

print(rng.integers(low=1, high=11,size=(10, 10)))


