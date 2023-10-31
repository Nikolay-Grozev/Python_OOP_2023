def logged(func):
    def wrapper(*args):
        result = f"you called {func.__name__}({', '.join(str(arg) for arg in args)})\n" \
                 f"it returned {func(*args)}"

        return result

    return wrapper


a = 7


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
