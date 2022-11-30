import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [1200, 1300, 5000, 900, 4000, 2500]
plt.plot(x, y)

legend = ['january', 'february', 'march', 'april', 'may', 'june']
plt.xticks(x, legend)
plt.show()