import unittest

from allthethings.iterables import dedup


class IterablesTestCase(unittest.TestCase):
    def test_dedup(self):
        result = [*dedup([1, 2, 3, 2, 1])]
        self.assertEqual([1, 2, 3], result)


if __name__ == '__main__':
    unittest.main()
