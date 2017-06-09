import unittest
import sort_strings


class TestSortStrings(unittest.TestCase):
  def test_numbers(self):
    numbers = ['1', '13', '2', '-13', '-1.1', '+1', '.2', '-21']
    sorted_numbers = ['-21', '-13', '-1.1', '.2', '1', '+1', '2', '13']
    self.assertEqual(sort_strings.sortStrings(numbers), sorted_numbers)

  def test_scientific_notation_numbers(self):
    numbers = ['1', '11e99', '2e99' ,'2', '-2.23E+45', '-13', '0.1e-456', '+1', '.2', '-21']
    sorted_numbers = ['-2.23E+45', '-21', '-13', '0.1e-456', '.2', '1', '+1', '2', '2e99', '11e99']
    self.assertEqual(sort_strings.sortStrings(numbers), sorted_numbers)

if __name__ == '__main__':
  unittest.main()

