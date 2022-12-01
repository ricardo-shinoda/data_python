# Type letter 5 times and use matplot to show a graphic

import time
import matplotlib.pyplot as plt

start_time = []
end_time = []
counted_time = [] # here will be Y
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
        counted_time.append(tempo)
count()
# plt.plot(x, counted_time)
# print(start_time)
# print(end_time)
print(counted_time)

legend = ['first','second', 'third', 'fourth', 'fifth']
plt.xticks(x, legend)
plt.show()