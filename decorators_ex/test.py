def repeat_n_times(n):
    def decorator(func):
        def wrapper(*args):
            for _ in range(n):
                func(*args)
        return wrapper
    return decorator


@repeat_n_times(4)
@repeat_n_times(2)
def hello(name):
    print(f"Hello, {name}")


hello("Alice")

