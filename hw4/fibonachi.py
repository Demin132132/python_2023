from time import time
import threading, multiprocessing


def fibonachi(x: int):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fibonachi(x-1) + fibonachi(x-2)


t = time()
threads = [threading.Thread(target=fibonachi, args=(500,)) for _ in range(100)]
threads_time = time() - t

process = [multiprocessing.Process(target=fibonachi, args=(500,)) for _ in range(100)]
process_time = time() - t


with open('artifacts/easy_results.txt', 'w') as file:
    file.write(f'thread time {threads_time}, process time {process_time}')
