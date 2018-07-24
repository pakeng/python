# 测试面向对象编程
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
