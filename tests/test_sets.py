import unittest

from maths import sets


class SetsTest(unittest.TestCase):

    def setUp(self):
        self.sample_set_a = {2, 3, 5, 7, 9, 12, 28}
        self.sample_set_b = {0, 1, 5, 9, 21}

    def tearDown(self):
        del self.sample_set_a
        del self.sample_set_b

    def test_cardinality(self):
        self.assertEqual(
            sets.cardinality(self.sample_set_a),
            len(self.sample_set_a),
        )

    def test_membership(self):
        elements = [-1, 2]

        for element in elements:
            with self.subTest(element=element):
                self.assertEqual(
                    sets.membership(element, self.sample_set_a),
                    element in self.sample_set_a,
                )

    def test_equality(self):
        self.assertEqual(
            sets.are_equal(self.sample_set_a, self.sample_set_a),
            self.sample_set_a == self.sample_set_a,
        )

    def test_non_equality(self):
        self.assertEqual(
            sets.are_equal(self.sample_set_a, self.sample_set_b),
            self.sample_set_a == self.sample_set_b,
        )


if __name__ == '__main__':
    unittest.main()
