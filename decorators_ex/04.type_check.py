def type_check(expected_type):
    def decorator(func):
        def wrapper(argument):
            if not isinstance(argument, expected_type):
                return "Bad Type"
            return func(argument)

        return wrapper

    return decorator


@type_check(float)
def times2(num):
    return num * 2


print(times2(2.0))
print(times2('Not A Number'))


@type_check(list)
def first_letter(word):
    return word[2]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
