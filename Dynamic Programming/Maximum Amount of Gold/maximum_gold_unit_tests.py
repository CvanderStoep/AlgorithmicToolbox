import unittest
from maximum_gold import maximum_gold_greedy
from maximum_gold import maximum_gold_permutations
from maximum_gold import Knapsack


class MaximumGold(unittest.TestCase):
    def test(self):
        for capacity, weights, answer in (
                (10, (1, 4, 8), 9),
                (20, (5, 7, 12, 18), 19),
                (20, (5, 7, 11, 18, 4, 8), 20),
                (10, (3, 5, 3, 3, 5), 10),
                (6, (2, 2, 2, 5), 6)
        ):
            self.assertEqual(maximum_gold_permutations(capacity, list(weights)), answer)
            self.assertEqual(Knapsack(capacity, list(weights)), answer)


if __name__ == '__main__':
    unittest.main()
