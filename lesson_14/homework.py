import numpy as np

# Task 1.

array = np.array([32, 68, 100, 212, 77])

@np.vectorize
def convert_fah_to_cel(a):
    return (a - 32) * (5/9)

converted = convert_fah_to_cel(array)
print(converted)


# Task 2.

numbers = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])

@np.vectorize
def power_of_number(number, power):
    return number ** power

result = power_of_number(numbers, powers)
print(result)


# Task 3.

a = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
b = np.array([7, 4, 5])

result = np.linalg.solve(a, b)
print(result)


# Task 4.

a = np.array([[10, -2, 3],[-2, 8, -1], [3, -1, 6]])
b = np.array([12, -5, 15])

result = np.linalg.solve(a, b)
print(result)

# Task 5

from PIL import Image

# 1.
with Image.open("images/bird.jpg") as img:
    array = np.array(img)
    array = np.flip(array, axis=1) # Left - Right
    array = np.flip(array, axis=0) # Up - Down

    flipped_img = Image.fromarray(array)
    flipped_img.save("images/flipped_img.jpg")

# 3.
with Image.open("images/bird.jpg") as img:
    array = np.array(img).astype(np.int16)
    array[:, :, 0] = np.clip(array[:, :, 0] + 40, 0, 255)

    brightened_img = Image.fromarray(array.astype(np.uint8))
    brightened_img.save("images/brightened_img.jpg")


# 4.
with Image.open("images/bird.jpg") as img:
    width, height = img.size
    a1 = int(height / 2 - 100)
    a2 = int(height / 2 + 100)
    b1 = int(width / 2 - 100)
    b2 = int(width / 2 + 100)
    array = np.array(img)
    array[a1:a2, b1:b2, :] = 0
    masked_img = Image.fromarray(array)
    masked_img.save("images/masked_img.jpg")


