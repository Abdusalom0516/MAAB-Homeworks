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
# **Image Manipulation with NumPy and PIL**

# Image file: `images/birds.jpg`. Your task is to perform the following image manipulations using the **NumPy** library while leveraging **PIL** for reading and saving the image.

# **Instructions:**

# 1. **Flip the Image**:
#    - Flip the image horizontally and vertically (left-to-right and up-to-down).

# 2. **Add Random Noise**:
#    - Add random noise to the image.

# 3. **Brighten Channels**:
#    - Increase the brightness of the channels (r.g. red channel) by a fixed value (e.g., 40). Clip the values to ensure they stay within the 0 to 255 range.

# 4. **Apply a Mask**:
#    - Mask a rectangular region in the image (e.g., a 100x100 area in the center) by setting all pixel values in this region to black (0, 0, 0).

# **Requirements:**
# - Use the **PIL** module onyl to:
#   - Read the image.
#   - Convert numpy array to image.
#   - Save the modified image back to a file.
# - Perform all manipulations using NumPy functions. Avoid using image editing functions from PIL or other libraries.


# **Bonus Challenge**:
# - Create a function for each manipulation (e.g., `flip_image`, `add_noise`, `brighten_channels`, `apply_mask`) to promote modularity and reusability of code.

# ---

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


