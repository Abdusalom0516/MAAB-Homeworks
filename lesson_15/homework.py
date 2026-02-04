import matplotlib.pyplot as plt
import numpy as np

# #### **1. Basic Plotting**
# - **Task**: Plot the function $ f(x) = x^2 - 4x + 4 $ for $ x $ values between -10 and 10.
# Customize the plot with appropriate labels for the axes and a title.

# array = np.linspace(-10, 10, 100)
# array = array ** 2 - 4 * array + 4

# plt.plot(array)
# plt.show()


# #### **2. Sine and Cosine Plot**
# - **Task**: Plot $ \sin(x) $ and $ \cos(x) $ on the same graph for $ x $ values ranging from 0 to $ 2\pi $. 
# Use different line styles, markers, and colors to distinguish between the two functions. Add a legend.

# array = np.linspace(0, (2/np.pi)+1, 10)

# array_sin = np.sin(array)
# array_cos = np.cos(array)

# plt.plot(array_sin, label="sin", color="b", marker="*", linestyle="-.")
# plt.plot(array_cos, label="cos", color="r", marker="o", linestyle="--")
# plt.legend()

# plt.show()


# #### **3. Subplots**
# - **Task**: Create a 2x2 grid of subplots. In each subplot, plot:
#   - Top-left: $ f(x) = x^3 $
#   - Top-right: $ f(x) = \sin(x) $
#   - Bottom-left: $ f(x) = e^x $
#   - Bottom-right: $ f(x) = \log(x+1) $ (for $ x \geq 0 $)

#   Customize each plot with titles, axis labels, and different colors.

array = np.linspace(-10, 10, 100)
top_left = array ** 3
top_right = np.sin(array)
bottom_left = np.e ** array
array = array[array >= 0]
bottom_right = np.log(array+1)

plt.subplot(2, 2, 1)
plt.plot(top_left, color="g")
plt.title("$ f(x) = x^3 $")

plt.subplot(2, 2, 2)
plt.plot(top_right,  color="r")
plt.title("$ f(x) = \sin(x) $")

plt.subplot(2, 2, 3)
plt.plot(bottom_left,  color="blue")
plt.title("$ f(x) = e^x $")

plt.subplot(2, 2, 4)
plt.plot(bottom_right,  color="purple")
plt.title("$ f(x) = \log(x+1) $ (for $ x \geq 0 $")

plt.tight_layout()
plt.show()


