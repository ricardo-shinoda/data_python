# Type letter 5 times and use matplot to show a graphic

import time
import matplotlib.pyplot as plt

start_time = []
end_time = []
counted_time = [] # here will be Y
x = [1, 2, 3, 4, 5]
repeat = 5

print('Digite vezes alguma palavra para contar o tempo entre as digitações')


def count():
    name_list = []
    while len(name_list) < 5: # Aqui estava o erro
        start = time.perf_counter()
        letter = input('Type a word: ')
        end = time.perf_counter()
        name_list.append(letter)
        start_time.append(start)
        end_time.append(end)
        tempo = round(end - start, 2)
        counted_time.append(tempo)
count()
# print(start_time)
# print(end_time)
# print(counted_time)
plt.plot(x, counted_time) # Alimentar o gráfico

legend = ['first','second', 'third', 'fourth', 'fifth']
plt.xticks(x, legend) # To change x value to legend
plt.show() # printar o gráfico