class NumeralSystem:
    digits = "0123456789ABCDEF"

    def __init__(self, base):
        self.base = base

    def _to_decimal(self, number: str) -> int:
        return sum([
            int(self.base ** exponent * self.digits.find(digit))
            for exponent, digit in enumerate(number[::-1])
        ])

    def to_base(self, number: str, base: int = 10) -> str:
        if self.base == base:
            return number

        if base > len(self.digits):
            raise Exception(
                f"Not enough digit's symbols defined."
                f" Max is base {len(self.digits)}."
            )

        base_10_number = self._to_decimal(number)

        if base == 10:
            return str(base_10_number)

        powers = []

        while True:
            power = base ** len(powers)
            if base_10_number // power < 1:
                break

            powers.append(power)

        result = ""
        for power in powers[::-1]:
            result += self.digits[base_10_number // power]
            base_10_number %= power

        return result
