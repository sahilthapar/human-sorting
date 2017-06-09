import unittest
import sort_strings


class TestSortStrings(unittest.TestCase):
  def test_numbers(self):
    numbers = ['1', '13', '2', '-13', '-1.1', '+1', '.2', '-21']
    sorted_numbers = ['-21', '-13', '-1.1', '.2', '1', '+1', '2', '13']
    self.assertEqual(sort_strings.sortStrings(numbers), sorted_numbers)

if __name__ == '__main__':
  unittest.main()

