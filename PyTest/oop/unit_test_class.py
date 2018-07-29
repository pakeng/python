# 待测试的类
class UnTest(object):

    def __init__(self):
        self.name = "UnTest"
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, _age):
        self.__age = _age


# 测试可知 方法名称和属性名称不能一样，就算是定义的属性的getter或者setter方法也是
