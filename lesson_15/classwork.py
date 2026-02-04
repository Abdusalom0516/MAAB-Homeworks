from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np

# a = [1, 2, 4, 3, 5, 7]
# b = [5, 6, 8, 1, 3, 2]

# plt.plot(a, b, color='black', marker="o", linestyle="-.")
# plt.show()

# plt.plot(a, b, "k--o")
# plt.show()

# plt.scatter(a, b, marker="*",)
# plt.show()

# plt.bar(["Naruto", "Bleach", "one Pieace"], [750, 450, 1150])
# plt.title("Anime Data")
# plt.xlabel("Animes")
# plt.ylabel("Episodes")
# plt.show()

# numbers = np.random.randint(0, 100, 30)
# plt.hist(numbers, bins=10, color='g', edgecolor='k', cumulative=True)
# plt.show()


categories = ["Hunter X Hunter", "Bleach", "Vinland Saga", "Demon Slayer", "Jojo", "Naruto"]
values = [87, 80, 93, 85, 88, 85]
colors = ["b", "g", "y", "r", "orange", "pink"]

plt.pie(values, labels=categories,colors=colors,autopct="%1.1f%%",explode=[0, 0, 0.1, 0, 0, 0], )

plt.show()




