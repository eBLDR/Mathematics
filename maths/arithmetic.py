import unittest


class Operation:
    identity = NotImplemented

    @staticmethod
    def perform(operand_1: int, operand_2: int):
        raise NotImplementedError


class Addition(Operation):
    identity = 0

    @staticmethod
    def perform(addend_1: int, addend_2: int) -> int:
        return addend_1 + addend_2


class Subtraction(Operation):
    identity = 0

    @staticmethod
    def perform(minuend: int, subtrahend: int) -> int:
        return Addition.perform(minuend, -subtrahend)


class Multiplication(Operation):
    identity = 1

    @staticmethod
    def perform(multiplier: int, multiplicand: int) -> int:
        if multiplier < 0 or multiplicand < 0:
            raise ArithmeticError  # TODO

        result = 0
        for _ in range(multiplicand):
            result = Addition.perform(result, multiplier)

        return result


class Division(Operation):

    @staticmethod
    def perform(numerator: int, dividend: int) -> int:
        if dividend == 0:
            raise ZeroDivisionError

        raise NotImplementedError


class Exponentiation(Operation):

    @staticmethod
    def perform(base: int, exponent: int) -> int:
        if exponent < 0:
            raise ArithmeticError
        elif exponent == 0:
            return 1

        result = 1
        for _ in range(exponent):
            result = Multiplication.perform(result, base)

        return result


class TestAddition(unittest.TestCase):

    def test_1_plus_1(self):
        addend_1 = 1
        addend_2 = 1
        self.assertEqual(
            Addition.perform(addend_1, addend_2),
            addend_1 + addend_2,
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
            minuend - subtrahend,
        )

    def test_2_minus_0(self):
        minuend = 2
        subtrahend = 0
        self.assertEqual(
            Subtraction.perform(minuend, subtrahend),
            minuend - subtrahend,
        )

    def test_1_minus_1(self):
        minuend = 1
        subtrahend = 1
        self.assertEqual(
            Subtraction.perform(minuend, subtrahend),
            minuend - subtrahend,
        )

    def test_1_minus_2(self):
        minuend = 1
        subtrahend = 2
        self.assertEqual(
            Subtraction.perform(minuend, subtrahend),
            minuend - subtrahend,
        )

    def test_0_minus_1(self):
        minuend = 0
        subtrahend = 1
        self.assertEqual(
            Subtraction.perform(minuend, subtrahend),
            minuend - subtrahend,
        )


class TestMultiplication(unittest.TestCase):

    def test_2_times_2(self):
        multiplier = 2
        multiplicand = 2
        self.assertEqual(
            Multiplication.perform(multiplier, multiplicand),
            multiplier * multiplicand,
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
            multiplier * multiplicand,
        )

    def test_0_times_2(self):
        multiplier = 0
        multiplicand = 2
        self.assertEqual(
            Multiplication.perform(multiplier, multiplicand),
            multiplier * multiplicand,
        )

    def test_0_times_0(self):
        multiplier = 0
        multiplicand = 0
        self.assertEqual(
            Multiplication.perform(multiplier, multiplicand),
            multiplier * multiplicand,
        )

    def test_2_times_minus_2(self):
        multiplier = 2
        multiplicand = -2
        self.assertEqual(
            Multiplication.perform(multiplier, multiplicand),
            multiplier * multiplicand,
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

    def test_6_by_2(self):
        numerator = 6
        dividend = 2
        self.assertEqual(
            Division.perform(numerator, dividend),
            numerator / dividend,
        )

    def test_by_0(self):
        numerator = 1
        dividend = 0
        self.assertRaises(
            ZeroDivisionError,
            Division.perform(numerator, dividend),
        )


class TestExponentiation(unittest.TestCase):

    def test_2_to_the_power_of_2(self):
        base = 2
        exponent = 2
        self.assertEqual(
            Exponentiation.perform(base, exponent),
            base ** exponent,
        )

    def test_2_to_the_power_of_3(self):
        base = 2
        exponent = 3
        self.assertEqual(
            Exponentiation.perform(base, exponent),
            base ** exponent,
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
