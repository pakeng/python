from types import MethodType


# 测试 __slots__ 和 @ property
class Student(object):
    __slots__ = ("name", '_age', 'score', 'print_score')

    def __init__(self, name, age=10):
        self.name = name
        self._age = age

    def print_info(self):
        print("name = ", self.name)
        print("age = ", self._age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError("age should be integer")
        if age not in range(1, 120):
            raise ValueError("age should [1,120)")
        self._age = age


def print_score(self):
    print("name = ", self.name, "score = ", self.score)


if __name__ == '__main__':
    student = Student('Xiao A', 12)
    student.score = 100
    student.print_score = MethodType(print_score, student)
    student.age = 10
    student.print_info()
    student.age = 119
    student.print_info()
    student.print_score()
