import time as t
import matplotlib.pyplot as plt

duration_list = [] # here will be Y axle
vez = 1
repeat = 9
legend = [] # this will be the X axle

print('Esse programa contará o intervalo entre as digitações das palavras por', repeat, 'vezes')
while len(duration_list) < repeat:
    start = t.perf_counter()
    input('Type something: ')
    end = t.perf_counter()
    duration = round(end - start, 2)
    duration_list.append(duration)
    legend_str = str(vez) + ' tentativa'
    legend.append(legend_str)
    vez += 1

print(duration_list)
print(legend)

plt.plot(legend, duration_list)
plt.show()
