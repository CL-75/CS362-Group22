import unittest
import task


class TestConvertIntegeralPart(unittest.TestCase):
    def test1(self):
        num = '6'
        self.assertEqual(task.convert_integral_part(num), 6)
        self.assertIsInstance(task.convert_integral_part(num), int)

    def test2(self):
        num = '72456'
        self.assertEqual(task.convert_integral_part(num), 72456)
        self.assertIsInstance(task.convert_integral_part(num), int)

    def test3(self):
        num = '0'
        self.assertEqual(task.convert_integral_part(num), 0)
        self.assertIsInstance(task.convert_integral_part(num), int)

    def test4(self):
        num = '10'
        self.assertEqual(task.convert_integral_part(num), 10)
        self.assertIsInstance(task.convert_integral_part(num), int)

    def test5(self):
        num = '10'
        self.assertEqual(task.convert_integral_part(num, base=16), 16)
        self.assertIsInstance(task.convert_integral_part(num), int)

    def test6(self):
        num = 'A'
        self.assertEqual(task.convert_integral_part(num, base=16), 10)
        self.assertIsInstance(task.convert_integral_part(num), int)

    def test7(self):
        num = '63b5e'
        self.assertEqual(task.convert_integral_part(num, base=16), 408414)
        self.assertIsInstance(task.convert_integral_part(num), int)


class TestConvertFractionalPart(unittest.TestCase):
    def test1(self):
        num = '945'
        self.assertEqual(task.convert_fractional_part(num), 0.945)
        self.assertIsInstance(task.convert_fractional_part(num), float)

    def test2(self):
        num = '078'
        self.assertEqual(task.convert_fractional_part(num), 0.078)
        self.assertIsInstance(task.convert_fractional_part(num), float)

    def test3(self):
        num = '400'
        self.assertEqual(task.convert_fractional_part(num), 0.4)
        self.assertIsInstance(task.convert_fractional_part(num), float)

    def test4(self):
        num = '0'
        self.assertEqual(task.convert_fractional_part(num), 0.0)
        self.assertIsInstance(task.convert_fractional_part(num), float)


class TestValidNumber(unittest.TestCase):
    def test1(self):
        num = ''
        self.assertEqual(task.valid_number(num), False)

    def test2(self):
        num = '61'
        self.assertEqual(task.valid_number(num), 'integer')

    def test3(self):
        num = '73.72'
        self.assertEqual(task.valid_number(num), 'decimal')

    def test4(self):
        num = '-0x5D8'
        self.assertEqual(task.valid_number(num), 'hexadecimal')

    def test5(self):
        num = '0x67.fa'
        self.assertEqual(task.valid_number(num), False)


class TestValidInteger(unittest.TestCase):
    def test1(self):
        num = ''
        self.assertEqual(task.valid_integer(num), False)

    def test2(self):
        num = '1'
        self.assertEqual(task.valid_integer(num), True)

    def test3(self):
        num = '2'
        self.assertEqual(task.valid_integer(num), True)

    def test4(self):
        num = 'T'
        self.assertEqual(task.valid_integer(num), False)

    def test5(self):
        num = '-15'
        self.assertEqual(task.valid_integer(num), True)

    def test6(self):
        num = '1643'
        self.assertEqual(task.valid_integer(num), True)

    def test7(self):
        num = '436-15'
        self.assertEqual(task.valid_integer(num), False)


class TestValidDecimal(unittest.TestCase):
    def test1(self):
        num = '.'
        self.assertEqual(task.valid_decimal(num), False)

    def test2(self):
        num = '56'
        self.assertEqual(task.valid_decimal(num), False)

    def test3(self):
        num = '127.54'
        self.assertEqual(task.valid_decimal(num), True)

    def test4(self):
        num = '-36.7'
        self.assertEqual(task.valid_decimal(num), True)

    def test5(self):
        num = '.98'
        self.assertEqual(task.valid_decimal(num), True)

    def test6(self):
        num = '17.'
        self.assertEqual(task.valid_decimal(num), True)

    def test7(self):
        num = '14.87.'
        self.assertEqual(task.valid_decimal(num), False)

    def test8(self):
        num = ''
        self.assertEqual(task.valid_decimal(num), False)


class TestValidHexadecimal(unittest.TestCase):
    def test1(self):
        num = ''
        self.assertEqual(task.valid_hexadecimal(num), False)

    def test2(self):
        num = '165'
        self.assertEqual(task.valid_hexadecimal(num), False)

    def test3(self):
        num = '0x61F'
        self.assertEqual(task.valid_hexadecimal(num), True)

    def test4(self):
        num = '0x61Y'
        self.assertEqual(task.valid_hexadecimal(num), False)

    def test5(self):
        num = '-0x2b'
        self.assertEqual(task.valid_hexadecimal(num), True)

    def test6(self):
        num = 'x62'
        self.assertEqual(task.valid_hexadecimal(num), False)

    def test7(self):
        num = '-0xFDE5'
        self.assertEqual(task.valid_hexadecimal(num), True)

    def test8(self):
        num = '-0X2b'
        self.assertEqual(task.valid_hexadecimal(num), True)


if __name__ == '__main__':
    unittest.main()
