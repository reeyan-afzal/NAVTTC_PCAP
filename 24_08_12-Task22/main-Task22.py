# Exploring Matplotlib

import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(1000) * 100
y_data = np.random.random(1000) * 100

# Scatter Plot
# plt.scatter(x_data, y_data, c="#00f", s=150, marker="*", alpha=0.5)


# Line Plot
"""
years = [2006 + x for x in range(16)]
weights = [80, 83, 84, 85, 86, 82, 81, 79, 83, 80, 82, 82, 83, 81, 80, 79]
plt.plot(years, weights, c="g", lw=10)
"""

# Bar Plot
"""
x = ["C++", "C#", "Python", "Java", "Go"]
y = [20, 50, 140, 1, 45]
plt.bar(x, y, color="r", align="edge", width=0.3, edgecolor="green", lw=6)
"""

# Histograms
"""
ages = np.random.normal(20, 7.5, 1000)
plt.hist(ages, bins=[ages.min(), 18, 21, ages.max()], cumulative=True)
"""

# Pie Chart
"""
langs = ["Python", "C++", "C#", "Java", "Go"]
votes = [50, 24, 6, 14, 17]
explodes = [0.3, 0, 0, 0, 0]

plt.pie(
    votes,
    labels=langs,
    explode=explodes,
    autopct="%.2f%%",
    pctdistance=1.5,
    startangle=90,
)
"""

# Box Plots
heights = np.random.normal(172, 8, 300)

plt.boxplot(heights)

plt.show()
