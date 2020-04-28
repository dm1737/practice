#This is the unit test for problem 1 the sum of multiples of 3 and 5 less than input x
#This program uses python 3.8 standard library

import unittest
import sumOfMultiples

class TestSumOf(unittest.TestCase):

    def test_sumOf(self):
        self.assertEqual(sumOfMultiples.sumOf(0), 0)
        self.assertEqual(sumOfMultiples.sumOf(3), 0)
        self.assertEqual(sumOfMultiples.sumOf(4), 3)
        self.assertEqual(sumOfMultiples.sumOf(5), 3)
        self.assertEqual(sumOfMultiples.sumOf(6), 8)
        self.assertEqual(sumOfMultiples.sumOf(10), 23)
        self.assertEqual(sumOfMultiples.sumOf(16), 75)

if __name__ == '__main__':
    unittest.main()