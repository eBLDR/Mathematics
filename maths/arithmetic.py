class Operation:
    identity = NotImplemented

    @staticmethod
    def perform(*args):
        raise NotImplementedError


class UnaryOperation(Operation):

    @staticmethod
    def perform(operand_1: int):
        raise NotImplementedError


class BinaryOperation(Operation):
    sign_change_mapper = {
        (1, 1): 1,
        (1, -1): -1,
        (-1, 1): -1,
        (-1, -1): 1,
    }

    @staticmethod
    def sign_change(multiplier: int, multiplicand: int) -> int:
        key = (
            1 if multiplier >= 0 else -1,
            1 if multiplicand >= 0 else -1,
        )

        return BinaryOperation.sign_change_mapper.get(key)

    @staticmethod
    def perform(operand_1: int, operand_2: int):
        raise NotImplementedError


class Successor(UnaryOperation):
    metric = 1

    @staticmethod
    def perform(operand_1: int) -> int:
        return operand_1 + Successor.metric


class Predecessor(UnaryOperation):
    metric = 1

    @staticmethod
    def perform(operand_1: int) -> int:
        return operand_1 - Predecessor.metric


class AbsoluteValue(UnaryOperation):

    @staticmethod
    def perform(operand_1: int) -> int:
        return operand_1 if operand_1 >= 0 else -operand_1


class MultiplicativeInverse(UnaryOperation):

    @staticmethod
    def perform(operand_1: int) -> float:
        return 1 / operand_1


class Addition(BinaryOperation):
    identity = 0

    @staticmethod
    def perform(addend_1: int, addend_2: int) -> int:
        result = addend_1

        if addend_2 >= 0:
            for _ in range(addend_2):
                result = Successor.perform(result)

        else:
            for _ in range(-addend_2):
                result = Predecessor.perform(result)

        return result
        # return addend_1 + addend_2


class Subtraction(BinaryOperation):
    identity = 0

    @staticmethod
    def perform(minuend: int, subtrahend: int) -> int:
        return Addition.perform(minuend, -subtrahend)


class Multiplication(BinaryOperation):
    identity = 1

    @staticmethod
    def perform(multiplier: int, multiplicand: int) -> int:
        multiplier_abs = AbsoluteValue.perform(multiplier)
        multiplicand_abs = AbsoluteValue.perform(multiplicand)

        result = 0
        for _ in range(multiplicand_abs):
            result = Addition.perform(result, multiplier_abs)

        result *= BinaryOperation.sign_change(multiplier, multiplicand)

        return result


class Division(BinaryOperation):

    @staticmethod
    def perform(dividend: int, divisor: int) -> tuple:
        if divisor == 0:
            raise ZeroDivisionError

        dividend_abs = AbsoluteValue.perform(dividend)
        divisor_abs = AbsoluteValue.perform(divisor)
        quotient = 0

        while dividend_abs >= divisor_abs:
            quotient += 1
            dividend_abs -= divisor_abs
        else:
            quotient *= BinaryOperation.sign_change(dividend, divisor)
            remainder = dividend_abs

        return quotient, remainder

        # multiplier = numerator
        # multiplicand = MultiplicativeInverse.perform(dividend)
        #
        # return Multiplication.perform(multiplier, multiplicand)


class Exponentiation(BinaryOperation):

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
