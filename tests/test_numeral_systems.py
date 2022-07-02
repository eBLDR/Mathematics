import unittest

from maths.numeral_systems import NumeralSystem


class SetsTest(unittest.TestCase):

    def setUp(self):
        self.base_2_system = NumeralSystem(2)
        self.base_3_system = NumeralSystem(3)
        self.base_5_system = NumeralSystem(5)
        self.base_8_system = NumeralSystem(8)
        self.base_10_system = NumeralSystem(10)
        self.base_12_system = NumeralSystem(12)
        self.base_16_system = NumeralSystem(16)

    def tearDown(self):
        del self.base_2_system
        del self.base_3_system
        del self.base_5_system
        del self.base_8_system
        del self.base_10_system
        del self.base_12_system
        del self.base_16_system

    def test_base_2_to_base_2(self):
        x_str = "1011"
        self.assertEqual(x_str, self.base_2_system.to_base(x_str, base=2))

    def test_base_2_to_base_10(self):
        x = 0b1011
        x_str = "1011"
        self.assertEqual(str(int(x)), self.base_2_system.to_base(x_str, base=10))

    def test_base_3_to_base_10(self):
        x_str = "1210"
        self.assertEqual("48", self.base_3_system.to_base(x_str, base=10))

    def test_base_5_to_base_10(self):
        x_str = "0413"
        self.assertEqual("108", self.base_5_system.to_base(x_str, base=10))

    def test_base_8_to_base_10(self):
        x = 0o5031
        x_str = "5031"
        self.assertEqual(str(int(x)), self.base_8_system.to_base(x_str, base=10))

    def test_base_10_to_base_2(self):
        x_str = "3179"
        self.assertEqual("110001101011", self.base_10_system.to_base(x_str, base=2))

    def test_base_10_to_base_3(self):
        x_str = "3179"
        self.assertEqual("11100202", self.base_10_system.to_base(x_str, base=3))

    def test_base_10_to_base_5(self):
        x_str = "3179"
        self.assertEqual("100204", self.base_10_system.to_base(x_str, base=5))

    def test_base_10_to_base_8(self):
        x_str = "3179"
        self.assertEqual("6153", self.base_10_system.to_base(x_str, base=8))

    def test_base_10_to_base_10(self):
        x_str = "3179"
        self.assertEqual(x_str, self.base_10_system.to_base(x_str, base=10))

    def test_base_10_to_base_12(self):
        x_str = "3179"
        self.assertEqual("1A0B", self.base_10_system.to_base(x_str, base=12))

    def test_base_10_to_base_16(self):
        x_str = "3179"
        self.assertEqual("C6B", self.base_10_system.to_base(x_str, base=16))

    def test_base_12_to_base_10(self):
        x_str = "90A5"
        self.assertEqual("15677", self.base_12_system.to_base(x_str, base=10))

    def test_base_16_to_base_10(self):
        x = 0x10F6
        x_str = "10F6"
        self.assertEqual(str(int(x)), self.base_16_system.to_base(x_str, base=10))


if __name__ == '__main__':
    unittest.main()
