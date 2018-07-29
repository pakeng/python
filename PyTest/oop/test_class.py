from oop.unit_test_class import UnTest
import unittest


class UnitTest(unittest.TestCase):

    def test_set_age(self):
        un_test = UnTest()
        un_test.age = 10
        self.assertEqual(un_test.age, 10)


if __name__ == '__main__':
    test_case = UnitTest()
    test_case.test_set_age()
