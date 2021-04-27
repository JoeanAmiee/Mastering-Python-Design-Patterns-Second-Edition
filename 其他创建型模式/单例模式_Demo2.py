def singleton(cls, *args, **kw):
    instances = {}

    def wrapper():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return wrapper


@singleton
class Animal:
    def __init__(self):
        pass


animal1 = Animal()
animal2 = Animal()
print(id(animal1))
print(id(animal2))
