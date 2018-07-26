# 测试继承
class Animal(object):
    count = 0  # 定义一个数量标识类 创建了多少的实例

    def __init__(self):
        self.dna = ['animal']
        Animal.count += 1
        self.__private = 'private_msg'

    def print_info(self):
        print('DNA = ', self.dna,
              'private_info', self.__private)

    def print_private(self):
        print("private msg -- = ", self.__private)


class Dog(Animal):

    def __init__(self):
        super(Dog, self).__init__()
        self.dna.append('dog')


if __name__ == '__main__':
    dog = Dog()
    dog.print_info()
    print('Count = ', Animal.count)
    cat = Dog()
    print("cat count = ", cat.count)
    cat.print_private()
