import time as t
import matplotlib.pyplot as plt

word_list = []
start = []
end = []
counted = []

def count():
    while len(list) < 5:
        starting = t.perf_counter()
        msg = input('Type a word: ')
        ending = t.perf_counter()
        word_list.append(msg)
        start.append(starting)
        end.append(ending)
        time_list = (ending - starting)
        count_time.append(time_list)

