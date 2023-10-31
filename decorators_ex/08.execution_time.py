from time import time


def exec_time(func_ref):
    def wrapper(*args):
        # start time
        start = time()
        # exec func
        func_ref(*args)
        # stop time
        end = time()
        # return elapsed time
        return end - start

    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))
