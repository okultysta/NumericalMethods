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