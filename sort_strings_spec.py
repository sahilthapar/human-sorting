import unittest
import sort_strings

class TestSortStrings(unittest.TestCase):
  def test_numbers(self):
    numbers = ['1', '13', '2', '-13', '-1.1', '+1', '.2', '-21']
    sorted_numbers = ['-21', '-13', '-1.1', '.2', '1', '+1', '2', '13']
    self.assertEqual(sort_strings.sortStrings(numbers), sorted_numbers)

  def test_scientific_notation_numbers(self):
    numbers = ['1','11e99', '2e99','2', '-2.23E+45', '-13', '0.1e-456', '+1', '.2', '-21']
    sorted_numbers = ['-2.23E+45', '-21', '-13', '0.1e-456', '.2', '1', '+1', '2', '2e99', '11e99']
    self.assertEqual(sort_strings.sortStrings(numbers), sorted_numbers)

  def test_money(self):
    money = ['$5000', '$4000.10', '$400.10', '$0.99']
    sorted_money = ['$0.99', '$400.10', '$4000.10', '$5000']
    self.assertEqual(sort_strings.sortStrings(money), sorted_money)

  def test_dates(self):
    dates = ['2016-08-01', '2017-01-01', '2010-01-08', '1992-05-06']
    sorted_dates = ['1992-05-06', '2010-01-08', '2016-08-01', '2017-01-01']
    self.assertEqual(sort_strings.sortStrings(dates), sorted_dates)

  def test_dates_2(self):
    dates = ['2016-08-01', '2017-01-1', '2010-01-08', '1992-05-06', '2017-01-11', '2017-01-2']
    sorted_dates = ['1992-05-06', '2010-01-08', '2016-08-01', '2017-01-1', '2017-01-2', '2017-01-11']
    self.assertEqual(sort_strings.sortStrings(dates), sorted_dates)

  def test_dates_3(self):
    dates = ['10/31/2008', '31/8/2008', '01/01/1992', '01/01/1991', '11/01/1991', '2/01/1991']
    sorted_dates = ['01/01/1991', '2/01/1991', '11/01/1991', '01/01/1992', '31/8/2008', '10/31/2008']
    self.assertEqual(sort_strings.sortStrings(dates), sorted_dates)

  def test_invalid_as_alphanums(self):
    dates = ['10/31/2008', '31/8/2008', '01/01/1992', '01/01/1991', '11/01/1991', '2/01/1991', '31/31/1991']
    sorted_dates = ['01/01/1991', '2/01/1991', '11/01/1991', '01/01/1992', '31/8/2008', '10/31/2008', '31/31/1991']
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

  def test_file_paths_2(self):
    filepaths = ['./system/kernel/js/01_ui.core.js', './system/kernel/js/00_jquery-1.3.2.js',
                 './system/kernel/js/02_my.desktop.js', './system/kernel/my.desktop.js',
                 './system/kernel/1_my.desktop.js', './system/kernel/11_my.desktop.js',
                 './system/kernel/2_my.desktop.js',]
    sorted_filepaths = ['./system/kernel/1_my.desktop.js', './system/kernel/2_my.desktop.js',
                        './system/kernel/11_my.desktop.js', './system/kernel/my.desktop.js',
                        './system/kernel/js/00_jquery-1.3.2.js', './system/kernel/js/01_ui.core.js',
                        './system/kernel/js/02_my.desktop.js']
    self.assertEqual(sort_strings.sortStrings(filepaths), sorted_filepaths)

  def test_file_names(self):
    filenames = ['car.mov', '01alpha.sgi', '001alpha.sgi', 'my.string_41299.tif', 'organic2.0001.sgi']
    sorted_filenames = ['01alpha.sgi', '001alpha.sgi', 'car.mov', 'my.string_41299.tif', 'organic2.0001.sgi']
    self.assertEqual(sort_strings.sortStrings(filenames), sorted_filenames)

  def test_alphanumeric(self):
    alpha_nums = ['img12.png', 'img10.png', 'img2.png', 'img1.png']
    sorted_alpha_nums = ['img1.png', 'img2.png', 'img10.png', 'img12.png']
    self.assertEqual(sort_strings.sortStrings(alpha_nums), sorted_alpha_nums)

  def test_alphanumeric_with_dates(self):
    alpha_nums_date = ['img2014-10-10.png', 'img2014-02-02.png', 'img1992-06-05.png', 'img1992-01-10.png']
    sorted_alpha_nums_date = ['img1992-01-10.png', 'img1992-06-05.png', 'img2014-02-02.png', 'img2014-10-10.png']
    self.assertEqual(sort_strings.sortStrings(alpha_nums_date), sorted_alpha_nums_date)

  def test_version(self):
    versions = ['1.0.2','1.0.1','1.0.0','1.0.9']
    sorted_versions = ['1.0.0','1.0.1','1.0.2','1.0.9']
    self.assertEqual(sort_strings.sortStrings(versions), sorted_versions)

  def test_version_2(self):
    versions = ['1.1.100', '1.1.1', '1.1.10', '1.1.54']
    sorted_versions = ['1.1.1', '1.1.10', '1.1.54', '1.1.100']
    self.assertEqual(sort_strings.sortStrings(versions), sorted_versions)

  def test_version_with_text(self):
    version_with_text = ['myrelease-1.1.3', 'myrelease-1.2.3', 'myrelease-1.1.4',
                         'myrelease-1.1.1', 'myrelease-1.0.5']
    sorted_version_with_text = ['myrelease-1.0.5', 'myrelease-1.1.1', 'myrelease-1.1.3',
                                'myrelease-1.1.4', 'myrelease-1.2.3']
    self.assertEqual(sort_strings.sortStrings(version_with_text), sorted_version_with_text)

  def test_version_with_text_2(self):
    version_with_text = ['android2.2', 'android1.1', 'Android13.0', 'iOS1.0', 'ios11.1', 'iOS1.3']
    sorted_version_with_text = ['android1.1', 'android2.2', 'Android13.0', 'iOS1.0', 'iOS1.3', 'ios11.1']
    self.assertEqual(sort_strings.sortStrings(version_with_text), sorted_version_with_text)

  def test_version_with_text_3(self):
    version_with_text = ['1.1beta', '1.1.2alpha3', '1.0.2alpha3', '1.0.2alpha1', '1.0.1alpha4', '2.1.2', '2.1.1']
    sorted_version_with_text = ['1.0.1alpha4', '1.0.2alpha1', '1.0.2alpha3', '1.1.2alpha3', '1.1beta', '2.1.1', '2.1.2']
    self.assertEqual(sort_strings.sortStrings(version_with_text), sorted_version_with_text)

  def test_mixed_bag_1(self):
    mixed_bag = ['1', 'a', '3']
    sorted_mixed_bag = ['a', '1', '3']
    self.assertEqual(sort_strings.sortStrings(mixed_bag), sorted_mixed_bag)

  def test_mixed_bag_2(self):
    mixed_bag = ['02','3','2','01']
    sorted_mixed_bag = ['01','02','2','3']
    self.assertEqual(sort_strings.sortStrings(mixed_bag), sorted_mixed_bag)

  def test_mixed_bag_3(self):
    mixed_bag = ['alpha', ' 1', '  3', ' 2', '0']
    sorted_mixed_bag = ['alpha', '0', ' 1', ' 2', '  3']
    self.assertEqual(sort_strings.sortStrings(mixed_bag), sorted_mixed_bag)

if __name__ == '__main__':
  unittest.main()

