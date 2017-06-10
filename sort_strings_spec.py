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

  def test_money(self):
    money = ['$5000', '$4000.10', '$400.10', '$0.99']
    sorted_money = ['$0.99', '$400.10', '$4000.10', '$5000']
    self.assertEqual(sort_strings.sortStrings(money), sorted_money)

  def test_date(self):
    dates = ['2016-08-01', '2017-01-01', '2010-01-08', '1992-05-06']
    sorted_dates = ['1992-05-06', '2010-01-08', '2016-08-01', '2017-01-01']
    self.assertEqual(sort_strings.sortStrings(dates), sorted_dates)

  def test_strings(self):
    strings = ['zbc', 'AbA', 'abc', 'xyz', 'LMNoP']
    sorted_strings = ['AbA', 'abc', 'LMNoP', 'xyz', 'zbc']
    self.assertEqual(sort_strings.sortStrings(strings), sorted_strings)

  def test_phone_numbers(self):
    phone_numbers = ['512-513-4400', '512-512-4400', '512-513-3000']
    sorted_phone_numbers = ['512-512-4400', '512-513-3000', '512-513-4400']
    self.assertEqual(sort_strings.sortStrings(phone_numbers), sorted_phone_numbers)

  def test_ip_addresses(self):
    ip_addresses = ['192.168.0.100', '192.168.0.1', '192.168.1.1', '192.168.102.250',
                    '192.168.204.250', '192.168.2.123', '10.0.0.2', '10.0.0.1']
    sorted_ip_addresses = ['10.0.0.1', '10.0.0.2', '192.168.0.1', '192.168.0.100',
                            '192.168.1.1', '192.168.2.123', '192.168.102.250', '192.168.204.250']
    self.assertEqual(sort_strings.sortStrings(ip_addresses), sorted_ip_addresses)

  def test_file_paths(self):
    filepaths = ['./system/kernel/js/01_ui.core.js', './system/kernel/js/00_jquery-1.3.2.js',
                 './system/kernel/js/02_my.desktop.js', './system/kernel/my.desktop.js',
                 './system/kernel/1_my.desktop.js']
    sorted_filepaths = ['./system/kernel/1_my.desktop.js', './system/kernel/my.desktop.js',
                        './system/kernel/js/00_jquery-1.3.2.js', './system/kernel/js/01_ui.core.js',
                        './system/kernel/js/02_my.desktop.js']
    self.assertEqual(sort_strings.sortStrings(filepaths), sorted_filepaths)

if __name__ == '__main__':
  unittest.main()

