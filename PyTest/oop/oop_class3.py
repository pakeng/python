# 使用元类
class Test(object):

    def __init__(self):
        self.name = 'test_obj'

    def __str__(self):
        return "this class is named Test and this obj named %s" % self.name

    def __repr__(self):
        return " repr this class is named Test and this obj named %s" % self.name

    # __repr__ = __str__  repr 的快捷写法


if __name__ == '__main__':
    test = Test()
    print(test)
    print(type(test))
    print(test.__repr__())

# 然而并没有写元类的使用 哈哈哈……
