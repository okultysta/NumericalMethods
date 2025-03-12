import unittest
import functions

if __name__ == '__main__':
    unittest.main()

class TestAlgorithms(unittest.TestCase):

    def test_one_root(self):
        b = False
        if functions.one_root((1.0+3.0)/2) == 0:
            b = True
        self.assertEqual(b, True)
        self.assertEqual(0, functions.one_root((1.0+3.0)/2))

    def test_polynomial(self):
        result = functions.polynomial(2, 2, [2,3])
        self.assertEqual(7, result)

    def test_exponential(self):
        result = functions.exponential(0)
        self.assertEqual(-99, result)

        result = functions.exponential(3)
        self.assertEqual(-92, result)