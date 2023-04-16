import math
from time import time

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


params = [math.cos, 0, math.pi / 2]


def function(args):
    i, f, a, step = args
    return f(a + i * step) * step


def concurrent_integrate(f, a, b, pool_executor, n_jobs=1, n_iter=1000000):
    step = (b - a) / n_iter
    with pool_executor(max_workers=n_jobs) as executor:
        return sum(list(executor.map(function, [[i, f, a, step] for i in range(n_iter)])))


def integrate_thread(f, a, b, *args, **kwargs):
    return concurrent_integrate(f, a, b, ThreadPoolExecutor, *args, **kwargs)


def integrate_process(f, a, b, *args, **kwargs):
    return concurrent_integrate(f, a, b, ProcessPoolExecutor, *args, **kwargs)


def integrate(f, a, b, n_jobs=1, n_iter=1000000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


if __name__ == '__main__':
    integrate_thread_time_by_jobs = {}
    process_thread_time_by_jobs = {}
    for n_jobs in range(1, 16):
        t = time()
        print(integrate_process(*params, n_jobs, 1000))
        process_thread_time = time() - t
        process_thread_time_by_jobs[n_jobs] = process_thread_time

        t = time()
        print(integrate_thread(*params, n_jobs, 1000))
        integrate_thread_time = time() - t
        integrate_thread_time_by_jobs[n_jobs] = integrate_thread_time

    with open('artifacts/medium_results.txt', 'w') as file:
        file.write('n_jobs       thread time         process time\n')
        for n_jobs in integrate_thread_time_by_jobs:
            file.write(
                f'{n_jobs}       {integrate_thread_time_by_jobs[n_jobs]}    {process_thread_time_by_jobs[n_jobs]}\n'
            )
