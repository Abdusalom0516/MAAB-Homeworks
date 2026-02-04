import matplotlib.pyplot as plt
import numpy as np

# #### **1. Basic Plotting**
# - **Task**: Plot the function $ f(x) = x^2 - 4x + 4 $ for $ x $ values between -10 and 10.
# Customize the plot with appropriate labels for the axes and a title.

array = np.linspace(-10, 10, 100)
array = array ** 2 - 4 * array + 4

plt.plot(array)
plt.show()


# #### **2. Sine and Cosine Plot**
# - **Task**: Plot $ \sin(x) $ and $ \cos(x) $ on the same graph for $ x $ values ranging from 0 to $ 2\pi $. 
# Use different line styles, markers, and colors to distinguish between the two functions. Add a legend.

array = np.linspace(0, (2/np.pi)+1, 10)

array_sin = np.sin(array)
array_cos = np.cos(array)

plt.plot(array_sin, label="sin", color="b", marker="*", linestyle="-.")
plt.plot(array_cos, label="cos", color="r", marker="o", linestyle="--")
plt.legend()

plt.show()


# #### **3. Subplots**
# - **Task**: Create a 2x2 grid of subplots. In each subplot, plot:
#   - Top-left: $ f(x) = x^3 $
#   - Top-right: $ f(x) = \sin(x) $
#   - Bottom-left: $ f(x) = e^x $
#   - Bottom-right: $ f(x) = \log(x+1) $ (for $ x \geq 0 $)

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


# #### **4. Scatter Plot**
# - **Task**: Create a scatter plot of 100 random points in a 2D space.
# The x and y values should be randomly generated from a uniform distribution between 0 and 10.
# Use different colors and markers for the points. Add a title, axis labels, and a grid.

x = np.random.randint(0, 11, 100)
y = np.random.randint(0, 11, 100)

plt.scatter(x, y, c=y,cmap="plasma")
plt.title("Scatter Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(visible=0.5)
plt.colorbar()

plt.show()


# #### **5. Histogram**
# - **Task**: Generate a random dataset of 1000 values sampled from a normal distribution (mean=0, std=1).
# Plot a histogram of the data with 30 bins. Add a title and axis labels.
# Adjust the transparency of the bars using the `alpha` parameter.

array = np.random.normal(0, 1, 1000)
print(array)

plt.hist(array, edgecolor= "w", color="purple", bins=30, alpha=0.5)
plt.xlabel("x")
plt.ylabel("y")

plt.show()


# #### **6. 3D Plotting**

# over the range of $ x $ and $ y $ values from -5 to 5. Use a suitable colormap and add a colorbar.
# Set appropriate labels for the axes and title.

fig = plt.figure()
ax = plt.axes(projection="3d")

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)

surf = ax.plot_surface(X, Y, Z, cmap="gist_rainbow")
fig.colorbar(surf, shrink=0.7,  aspect=11)
plt.tight_layout()

plt.show()


# #### **7. Bar Chart**
# - **Task**: Create a vertical bar chart displaying the sales data for five different products:
# `['Product A', 'Product B', 'Product C', 'Product D', 'Product E']`.
# The sales values for each product are `[200, 150, 250, 175, 225]`.
# Customize the chart with a title, axis labels, and different bar colors.

categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = np.array([200, 150, 250, 175, 225])
colors = ["blue", "red", "green", "purple", "brown"]

plt.bar(categories, sales, width=0.6, color=colors)
plt.title("Sales Chart")
plt.xlabel("Categories")
plt.ylabel("Sales")
plt.show()


# #### **8. Stacked Bar Chart**
# - **Task**: Create a stacked bar chart that shows the contribution of three different
# categories (`'Category A'`, `'Category B'`, and `'Category C'`) over four time
# periods (`'T1'`, `'T2'`, `'T3'`, `'T4'`). Use sample data for each category at each time period.
# Customize the chart with a title, axis labels, and a legend.


categories = ['Category A', 'Category B', 'Category C']

t1 = np.random.randint(15, 75, 3)
t2 = np.random.randint(15, 75, 3)
t3 = np.random.randint(15, 75, 3)
t4 = np.random.randint(15, 75, 3)

plt.bar(categories, t1, width=0.4, color="purple", label="t1")
plt.bar(categories, t2, width=0.4, color="yellow", label="t2", bottom=t1)
plt.bar(categories, t3, width=0.4, color="blue", label="t3", bottom=t1+t2)
plt.bar(categories, t4, width=0.4, color="green", label="t4", bottom=t1+t2+t3)

plt.legend()
plt.show()











