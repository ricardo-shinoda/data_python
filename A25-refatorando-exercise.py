import time as t
import matplotlib.pyplot as plt

duration_list = [] # here will be Y axle
x = [] # here will be X axle
vez = 0

while len(duration_list) < 5:
    start = t.perf_counter()
    input('Type something: ')
    end = t.perf_counter()
    duration = round(end - start, 2)
    duration_list.append(duration)
    x.append(vez + 1)
    vez += 1

print(duration_list)
print(x)

legend = ['first','second', 'third', 'fourth', 'fifth']
plt.xticks(x, legend) # To change x value to legend

plt.plot(x, duration_list)
plt.show()
