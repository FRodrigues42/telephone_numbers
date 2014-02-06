import telephone_numbers
import unittest

class TelephoneNumbersTest(unittest.TestCase):
    def test_00(self):
        self.assertEqual((), telephone_numbers.get_telephone_numbers(""))
    def test_01(self):
        self.assertEqual(("20","123","456"), telephone_numbers.get_telephone_numbers("20123456"))
    def test_02(self):
        self.assertEqual(("200","123","456"), telephone_numbers.get_telephone_numbers("200123456"))
    def test_03(self):
        self.assertEqual(("20","123","456"), telephone_numbers.get_telephone_numbers(" 20123456"))
    def test_04(self):
        self.assertEqual(("20","123","456"), telephone_numbers.get_telephone_numbers("20123456 "))
    def test_05(self):
        self.assertEqual(("20","123","456"), telephone_numbers.get_telephone_numbers("(20123456)"))
    def test_06(self):
        self.assertEqual(("20","123","456"), telephone_numbers.get_telephone_numbers("casa 20123456"))
    def test_07(self):
        self.assertEqual(("20","123","456"), telephone_numbers.get_telephone_numbers("20123456 casa"))
    def test_08(self):
        self.assertEqual(("20","123","456"), telephone_numbers.get_telephone_numbers("20 123 456"))
    def test_09(self):
        self.assertEqual(("20","123","456"), telephone_numbers.get_telephone_numbers("20-123-456"))
    def test_10(self):
        self.assertEqual(("20","123","456"), telephone_numbers.get_telephone_numbers("20 - 123 - 456"))
    def test_11(self):
        self.assertEqual(("20","123","456"), telephone_numbers.get_telephone_numbers("20 12-34-56"))
    def test_12(self):
        self.assertEqual((), telephone_numbers.get_telephone_numbers("20 12-34-567"))
    def test_13(self):
        self.assertEqual((), telephone_numbers.get_telephone_numbers("20 12-34-56 7"))
    def test_14(self):
        self.assertEqual((), telephone_numbers.get_telephone_numbers("1120 12-34-56"))
    def test_15(self):
        self.assertEqual((), telephone_numbers.get_telephone_numbers("20123456 casa 1"))
        
if __name__ == '__main__':
    unittest.main()