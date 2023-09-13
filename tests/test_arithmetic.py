import unittest

from maths.arithmetic import AbsoluteValue, Addition, Division, Exponentiation, Multiplication, Subtraction, Successor, \
    Predecessor


class TestAbsoluteValue(unittest.TestCase):

    def test_positive_1(self):
        operand = 1
        self.assertEqual(
            AbsoluteValue.perform(operand),
            1,
        )

    def test_negative_1(self):
        operand = -1
        self.assertEqual(
            AbsoluteValue.perform(operand),
            1,
        )


class TestSuccessor(unittest.TestCase):

    def test_successor_1(self):
        seed = 1
        self.assertEqual(
            Successor.perform(seed),
            2,
        )

    def test_successor_0(self):
        seed = 0
        self.assertEqual(
            Successor.perform(seed),
            1,
        )

    def test_successor_negative1(self):
        seed = -1
        self.assertEqual(
            Successor.perform(seed),
            0,
        )


class TestPredecessor(unittest.TestCase):

    def test_predecessor_0(self):
        seed = 0
        self.assertEqual(
            Predecessor.perform(seed),
            -1,
        )

    def test_predecessor_1(self):
        seed = 1
        self.assertEqual(
            Predecessor.perform(seed),
            0,
        )

    def test_predecessor_2(self):
        seed = 2
        self.assertEqual(
            Predecessor.perform(seed),
            1,
        )


class TestAddition(unittest.TestCase):

    def test_1_plus_1(self):
        addend_1 = 1
        addend_2 = 1
        self.assertEqual(
            Addition.perform(addend_1, addend_2),
            2,
        )

    def test_identity(self):
        addend_1 = 1
        addend_2 = Addition.identity
        self.assertEqual(
            Addition.perform(addend_1, addend_2),
            addend_1,
        )

    def test_commutativity(self):
        addend_1 = 3
        addend_2 = 2
        self.assertEqual(
            Addition.perform(addend_1, addend_2),
            Addition.perform(addend_2, addend_1),
        )

    def test_associativity(self):
        addend_1 = 3
        addend_2 = 2
        addend_3 = 1
        self.assertEqual(
            Addition.perform(Addition.perform(addend_1, addend_2), addend_3),
            Addition.perform(Addition.perform(addend_2, addend_3), addend_1),
        )


class TestSubtraction(unittest.TestCase):

    def test_2_minus_1(self):
        minuend = 2
        subtrahend = 1
        self.assertEqual(
            Subtraction.perform(minuend, subtrahend),
            1,
        )

    def test_2_minus_0(self):
        minuend = 2
        subtrahend = 0
        self.assertEqual(
            Subtraction.perform(minuend, subtrahend),
            2,
        )

    def test_1_minus_1(self):
        minuend = 1
        subtrahend = 1
        self.assertEqual(
            Subtraction.perform(minuend, subtrahend),
            0,
        )

    def test_1_minus_2(self):
        minuend = 1
        subtrahend = 2
        self.assertEqual(
            Subtraction.perform(minuend, subtrahend),
            -1,
        )

    def test_0_minus_1(self):
        minuend = 0
        subtrahend = 1
        self.assertEqual(
            Subtraction.perform(minuend, subtrahend),
            -1,
        )


class TestMultiplication(unittest.TestCase):

    def test_2_times_2(self):
        multiplier = 2
        multiplicand = 2
        self.assertEqual(
            Multiplication.perform(multiplier, multiplicand),
            4,
        )

    def test_identity(self):
        multiplier = 2
        multiplicand = Multiplication.identity
        self.assertEqual(
            Multiplication.perform(multiplier, multiplicand),
            multiplier,
        )

    def test_2_times_0(self):
        multiplier = 2
        multiplicand = 0
        self.assertEqual(
            Multiplication.perform(multiplier, multiplicand),
            0,
        )

    def test_0_times_2(self):
        multiplier = 0
        multiplicand = 2
        self.assertEqual(
            Multiplication.perform(multiplier, multiplicand),
            0,
        )

    def test_0_times_0(self):
        multiplier = 0
        multiplicand = 0
        self.assertEqual(
            Multiplication.perform(multiplier, multiplicand),
            0,
        )

    def test_2_times_negative_2(self):
        multiplier = 2
        multiplicand = -2
        self.assertEqual(
            Multiplication.perform(multiplier, multiplicand),
            -4,
        )

    def test_negative_2_times_negative_2(self):
        multiplier = -2
        multiplicand = -2
        self.assertEqual(
            Multiplication.perform(multiplier, multiplicand),
            4,
        )

    def test_commutativity(self):
        multiplier = 3
        multiplicand = 2
        self.assertEqual(
            Multiplication.perform(multiplier, multiplicand),
            Multiplication.perform(multiplicand, multiplier),
        )

    def test_associativity(self):
        factor_1 = 3
        factor_2 = 2
        factor_3 = 1
        self.assertEqual(
            Multiplication.perform(Multiplication.perform(factor_1, factor_2), factor_3),
            Multiplication.perform(Multiplication.perform(factor_2, factor_3), factor_1),
        )


class TestDivision(unittest.TestCase):

    def test_1_by_1(self):
        dividend = 1
        divisor = 1
        self.assertEqual(
            Division.perform(dividend, divisor),
            (1, 0),
        )

    def test_1_by_2(self):
        dividend = 1
        divisor = 2
        self.assertEqual(
            Division.perform(dividend, divisor),
            (0, 1),
        )

    def test_6_by_2(self):
        dividend = 6
        divisor = 2
        self.assertEqual(
            Division.perform(dividend, divisor),
            (3, 0),
        )

    def test_5_by_2(self):
        dividend = 5
        divisor = 2
        self.assertEqual(
            Division.perform(dividend, divisor),
            (2, 1),
        )

    def test_6_by_negative_2(self):
        dividend = 6
        divisor = -2
        self.assertEqual(
            Division.perform(dividend, divisor),
            (-3, 0),
        )

    def test_5_by_negative_2(self):
        dividend = 5
        divisor = -2
        self.assertEqual(
            Division.perform(dividend, divisor),
            (-2, 1),
        )

    def test_negative_5_by_negative_2(self):
        dividend = -5
        divisor = -2
        self.assertEqual(
            Division.perform(dividend, divisor),
            (2, 1),
        )

    def test_0_by_1(self):
        dividend = 0
        divisor = 1
        self.assertEqual(
            Division.perform(dividend, divisor),
            (0, 0),
        )

    def test_division_by_0(self):
        dividend = 1
        divisor = 0
        with self.assertRaises(ZeroDivisionError):
            Division.perform(dividend, divisor)


class TestExponentiation(unittest.TestCase):

    def test_2_to_the_power_of_2(self):
        base = 2
        exponent = 2
        self.assertEqual(
            Exponentiation.perform(base, exponent),
            4,
        )

    def test_2_to_the_power_of_3(self):
        base = 2
        exponent = 3
        self.assertEqual(
            Exponentiation.perform(base, exponent),
            8,
        )

    def test_to_the_power_of_0(self):
        base = 2
        exponent = 0
        self.assertEqual(
            Exponentiation.perform(base, exponent),
            1,
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
