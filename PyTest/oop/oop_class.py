# 测试面向对象编程
class People(object):

    def __init__(self, human_id=-1):
        self.__dna = None
        self.__id = human_id
        self.__type = 'HUMAN'

    def get_type(self):
        return self.__type

    def get_id(self):
        return self.__id

    def get_dna(self):
        return self.__dna

    def print_info(self):
        print('id = ', self.__id, 'type = ', self.__type, 'DNA = ', self.__dna)

    def set_DNA(self, param):
        self.__dna = param


class Student(object):

    def __init__(self):
        self.name = "小A"
        self.age = 0
        self.sex = '男'

    def set_name(self, name):
        self.name = name
        return self

    def set_sex(self, sex):
        self.sex = sex
        return self

    def get_info(self):
        print("name: ", self.name)
        print("age: ", self.age)
        print("sex: ", self.sex)


if __name__ == '__main__':
    student = Student()
    student.get_info()
    student.set_name("小B")
    student.get_info()
    human1 = People(999)
    human1.set_DNA("com.vito.python.people")
    human1.print_info()
