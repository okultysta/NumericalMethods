import unittest
import algorithms
import functions

if __name__ == '__main__':
    unittest.main()

class TestAlgorithms(unittest.TestCase):

    def test_bisection_iteration(self):
        with self.assertRaises(ValueError):
            algorithms.bisection_iteration(1, 5, functions.two_roots, 3)

        approx, accuracy = algorithms.bisection_iteration(1,5,functions.one_root,3)
        self.assertAlmostEqual(2.0, approx, delta=0.001)
        self.assertAlmostEqual(1.0, accuracy, delta=0.001)

        approx, accuracy = algorithms.bisection_iteration(1, 5, functions.one_root, 1)
        self.assertAlmostEqual(3.0, approx, delta=0.001)
        self.assertAlmostEqual(0, accuracy, delta=0.001)

        approx, accuracy = algorithms.bisection_iteration(1, 5, functions.one_root_2, 3)
        self.assertAlmostEqual(1.5, approx, delta=0.001)
        self.assertAlmostEqual(0.5, accuracy, delta=0.001)

        self.assertLess(functions.tree_roots(2.5), 0)
        self.assertLess( functions.tree_roots(1), 0)
        self.assertGreater(functions.tree_roots(2.5)*functions.tree_roots(1),0)

        approx, accuracy = algorithms.bisection_iteration(1, 4, functions.tree_roots, 10)
        self.assertAlmostEqual(3.9726334, approx, delta=0.001)


    def test_bisection_epsilon(self):
        with self.assertRaises(ValueError):
            algorithms.bisection_epsilon(1, 5, functions.two_roots, 3)

        approx, iter_num = algorithms.bisection_epsilon(1, 5, functions.one_root, 2)
        self.assertAlmostEqual(3.0, approx, delta=0.001)
        self.assertEqual(1, iter_num)

        approx, iter_num = algorithms.bisection_epsilon(1, 5, functions.one_root_2, 0.5)
        self.assertAlmostEqual(1.5, approx, delta=0.001)
        self.assertEqual(3, iter_num)