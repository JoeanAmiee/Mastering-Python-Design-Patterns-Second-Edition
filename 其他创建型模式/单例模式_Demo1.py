class Singleton:
    """创建实例(instance)时首先判断是否已经存在，如果已经存在则返回，否则创建。"""

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls)
        return cls._instance


class Books(Singleton):
    def __init__(self):
        pass


book1 = Books()
book2 = Books()
print(id(book1))
print(id(book2))
