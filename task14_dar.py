def singleton(class_obj):
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = class_obj(*args, **kwargs)

        return instance[0]  # returns either the newly created instance or the already existing one

    return wrapper


@singleton
class testClass:
    def __init__(self):
        self.var = 2

    def counter(self):
        self.var= self.var+2
        print(self.var)


def main():
    o1 = testClass()
    o1.counter()
    o1.counter()

    o2 = testClass()
    o2.counter()

    o3 = testClass()
    o3.counter()

    o1.counter()

    # they all point to the same instance which is created when we create o1


if __name__ == "__main__":
    main()


