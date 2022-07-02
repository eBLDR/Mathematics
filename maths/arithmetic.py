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
