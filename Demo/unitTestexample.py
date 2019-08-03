import unittest
from example import example



class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will run once before all the methods")

    @classmethod
    def tearDownClass(cls):
        print("This will run once after all the methods")

    def setUp(self):
        print("This will run before every method")

    def tearDown(self):
        print("This will run after every method")


    def test_add(self):
        self.assertEqual(example.add(self, 10, 20), 30)
        print("T1")
        # self.assertEqual(example.add(self, 10, 40), 30)
        # self.assertEqual(example.add(self, 0, 0), 0)
        # self.assertEqual(example.add(self, 1, 2), 3)

    def test_sub(self):
        print("T2")
        result = example.sub(self, 30, 20)
        self.assertEqual(result, 10)







    # def test_something(self):
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
