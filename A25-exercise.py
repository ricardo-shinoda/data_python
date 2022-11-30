# Type letter 5 times and use matplot to show a graphic

import time
import matplotlib.pyplot as plt

start_time = []
end_time = []
y = [] # here will be Y
x = [1, 2, 3, 4, 5]

def count():
    name_list = []
    while len(name_list) < 6:
        start = time.perf_counter()
        letter = input('Type a word: ')
        end = time.perf_counter()
        name_list.append(letter)
        start_time.append(start)
        end_time.append(end)
        tempo = round(end - start, 2)
        y.append(tempo)
count()
plt.plot(x, y)
# print(start_time)
# print(end_time)
# print(y)

legend = ['first','second', 'third', 'fourth', 'fifth']
plt.xticks(x, legend)
plt.show()