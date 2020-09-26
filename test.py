import unittest
from ddt import file_data, ddt


@ddt()
class MainTest(unittest.TestCase):
    @file_data('a.yml')
    def test_2(self, **kwargs):
        name = kwargs.get('name')
        self.assertEqual(name, 'xuzhu', 'buxiangdeng')
        print('**********')

    def test_1(self):
        print(1)

    @unittest.skipIf(1 < 2, 'ssss')
    def test_2(self):
        print(2)

    def test_3(self):
        print(3)

    @unittest.skip('不想')
    def test_4(self):
        print(4)

    def test_5(self):
        print(5)


if __name__ == '__main__':
    unittest.main()
