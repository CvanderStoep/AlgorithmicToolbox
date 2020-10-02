import unittest
from partition_souvenirs import partition3


class PartitionSouvenirs(unittest.TestCase):
    def test(self):
        for values, answer in (
            ((20, ), 0),
            ((7, 7, 7), 1),
            ((3, 3, 3), 1),
            ((3, 3, 3, 3), 0),
            ((1, 12, 17, 29, 18, 16), 0),
            ((2, 2, 8, 1, 6, 5, 9, 12), 1),
            ((1, 12, 17, 29, 18, 13), 1)
        ):
            self.assertEqual(partition3(list(values)), answer)


if __name__ == '__main__':
    unittest.main()
