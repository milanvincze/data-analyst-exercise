import unittest
import VinczeMilan as df

class Test_test_numbers(unittest.TestCase):
    def test_cookies_got(self):
        self.assertEqual(df.cookies_got(16, 2, 2), 15)
        self.assertEqual(df.cookies_got(15, 2, 2), 11)
        self.assertEqual(df.cookies_got(31, 5, 2), 10)

    def test_queen(self):
        self.assertEqual(df.queen(10, 4, 4, [[3, 5]]), 30)
        self.assertEqual(df.queen(18, 4, 4, [[3, 5]]), 54)
        self.assertEqual(df.queen(10, 4, 4, [[2, 2]]), 31)

    def test_euclidean_norm(self):
        self.assertEqual(df.euclidean_norm([1,2], [3,4]), 2.8284)
        self.assertEqual(df.euclidean_norm([1,1], [4,4]), 4.2426)
        self.assertEqual(df.euclidean_norm([5,2], [1,4]), 4.4721)

    def test_cubes(self):
        self.assertEqual(14, df.cubes([2, 1]))
        self.assertEqual(26, df.cubes([3, 1, 2]))
        self.assertEqual(6, df.cubes([1]))

if __name__ == '__main__':
    unittest.main()
