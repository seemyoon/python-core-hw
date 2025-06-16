import multiprocessing
import time
import math


def time_decorator(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        time_end = time.time()
        print(time_end - time_start)

    return wrapper


def work(num):
    return str(math.sqrt(math.sqrt(math.sqrt(math.sqrt(num) / 2) / 20 ** 10))) + "I"


@time_decorator
def main_process():
    print('main_p')
    r = range(50_000_000)
    try:
        with open('file.txt', 'w') as f:
            for i in r:
                res = work(i)
                print(res, file=f)
    except Exception as e:
        print(e)


# main_process()

@time_decorator
def multipro():
    print('multi')
    count = multiprocessing.cpu_count()
    print(count, 'CPUs')

    with multiprocessing.Pool(count) as process:  # without 'with' specify: p.close() p.join()
        r = range(50_000_000)
        try:
            with open('test_file2.txt', 'w') as f:
                tasks = process.map(work,
                                    r)  # results = p.map(square, [1, 2, 3, 4]) => square(1), square(2), square(3), square(4)
                for res in tasks:
                    print(res, file=f)
        except Exception as e:
            print(e)


multipro()
