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
        self.assertAlmostEqual(0, accuracy, delta=0.001)

        approx, accuracy = algorithms.bisection_iteration(1, 5, functions.one_root, 1)
        self.assertAlmostEqual(3.0, approx, delta=0.001)
        self.assertAlmostEqual(2.0, accuracy, delta=0.001)

        approx, accuracy = algorithms.bisection_iteration(1, 5, functions.one_root_2, 3)
        self.assertAlmostEqual(1.5, approx, delta=0.001)
        self.assertAlmostEqual(0.5, accuracy, delta=0.001)

        approx, accuracy = algorithms.bisection_iteration(1, 4, functions.tree_roots, 10)
        self.assertAlmostEqual(3.9726334, approx, delta=0.001)
        self.assertAlmostEqual(0.0029, accuracy, delta=0.001)


    def test_bisection_epsilon(self):
        with self.assertRaises(ValueError):
            algorithms.bisection_epsilon(1, 5, functions.two_roots, 3)

        approx, iter_num = algorithms.bisection_epsilon(1, 5, functions.one_root, 2.0001)
        self.assertAlmostEqual(3.0, approx, delta=0.001)
        self.assertEqual(1, iter_num)

        approx, iter_num = algorithms.bisection_epsilon(1, 5, functions.one_root, 2)
        self.assertAlmostEqual(2.0, approx, delta=0.001)
        self.assertEqual(2, iter_num)

        approx, iter_num = algorithms.bisection_epsilon(1, 5, functions.one_root_2, 0.5001)
        self.assertAlmostEqual(1.5, approx, delta=0.001)
        self.assertEqual(3, iter_num)

        approx, iter_num = algorithms.bisection_epsilon(1, 5, functions.tree_roots, 0.001)
        self.assertAlmostEqual(3.9726334, approx, delta=0.001)
        self.assertEqual(12, iter_num)

    def test_falsi_iteration(self):
        with self.assertRaises(ValueError):
            algorithms.falsi_iteration(1, 5, functions.two_roots, 3)

        approx, accuracy = algorithms.falsi_iteration(1, 5, functions.one_root, 2)
        self.assertAlmostEqual(2.0, approx, delta=0.001)
        self.assertAlmostEqual(0, accuracy, delta=0.001)

        approx, accuracy = algorithms.falsi_iteration(1, 10, functions.one_root_2, 1)
        self.assertAlmostEqual(1.432, approx, delta=0.001)
        self.assertAlmostEqual(0, accuracy, delta=0.001)

        approx, accuracy = algorithms.falsi_iteration(1, 4, functions.tree_roots, 10)
        self.assertAlmostEqual(3.9726334, approx, delta=0.001)
        self.assertAlmostEqual(0.0000000000001, accuracy, delta=0.00000000000001)

    def test_falsi_epsilon(self):
        with self.assertRaises(ValueError):
            algorithms.falsi_epsilon(1, 5, functions.two_roots, 3)

        approx, iter_num = algorithms.falsi_epsilon(1, 5, functions.one_root, 2)
        self.assertAlmostEqual(2.0, approx, delta=0.001)
        self.assertEqual(1, iter_num)

        approx, iter_num = algorithms.falsi_epsilon(1, 10, functions.one_root_2, 1)
        self.assertAlmostEqual(1.432, approx, delta=0.001)
        self.assertEqual(1, iter_num)

        approx, iter_num = algorithms.falsi_epsilon(1, 4, functions.tree_roots, 0.001)
        self.assertAlmostEqual(3.9726334, approx, delta=0.001)
        self.assertEqual(4, iter_num)