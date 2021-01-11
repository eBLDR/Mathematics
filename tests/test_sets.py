import unittest

from maths import sets


class SetsTest(unittest.TestCase):

    def setUp(self):
        self.sample_set_a = {2, 3, 5, 7, 9, 12, 28}
        self.sample_set_b = {0, 1, 5, 9, 21}
        self.sample_set_c = {2, 5}
        self.sample_set_d = {-1}

    def tearDown(self):
        del self.sample_set_a
        del self.sample_set_b
        del self.sample_set_c
        del self.sample_set_d

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

    def test_subset(self):
        self.assertEqual(
            sets.is_subset(self.sample_set_c, self.sample_set_a),
            self.sample_set_c.issubset(self.sample_set_a),
        )

    def test_disjoint(self):
        self.assertEqual(
            sets.are_disjoint(self.sample_set_d, self.sample_set_a),
            self.sample_set_d.isdisjoint(self.sample_set_a),
        )

    def test_disjoint_true(self):
        self.assertTrue(
            sets.are_disjoint(self.sample_set_d, self.sample_set_a),
        )

    def test_disjoint_false(self):
        self.assertFalse(
            sets.are_disjoint(self.sample_set_c, self.sample_set_a),
        )

    def test_union(self):
        self.assertEqual(
            sets.union(self.sample_set_a, self.sample_set_b),
            self.sample_set_a.union(self.sample_set_b),
        )

    def test_intersection(self):
        self.assertEqual(
            sets.intersection(self.sample_set_a, self.sample_set_b),
            self.sample_set_a.intersection(self.sample_set_b),
        )

    def test_difference(self):
        self.assertEqual(
            sets.difference(self.sample_set_a, self.sample_set_b),
            self.sample_set_a.difference(self.sample_set_b),
        )

    def test_symmetric_difference(self):
        self.assertEqual(
            sets.symmetric_difference(self.sample_set_a, self.sample_set_b),
            self.sample_set_a.symmetric_difference(self.sample_set_b),
        )


if __name__ == '__main__':
    unittest.main()
