def add(*args):
    result = 0
    for n in args:
        result+=n
    return result


print(add(5, 3, 5, 8, 7, 5, 4, 3))
