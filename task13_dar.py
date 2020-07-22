from functools import wraps


def timee (orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        r = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} Function. Answer {r}. Time: {t2}")
        return r

    return wrapper


# function 1
@timee
def addition(x, y):
    return x+y


# function 2
@timee
def square(x):
    return x*x


# function 3
@timee
def power(x, y):
    tmp = x
    for i in range(1, y):
        x = x*tmp

    return x


def main():
    addition(30, 51)
    square(12)
    power(4, 5)


if __name__ == "__main__":
    main()


