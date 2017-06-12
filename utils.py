from dateutil.parser import parse as date_parse
import re
import calendar

# List of regex for detecting different types of strings

num_re = re.compile(r"^[+-.]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?$")
money_re = re.compile(r"^\$\d+[.]?\d+$")
date_re = re.compile(r"(\d{4}[-/]\d{1,2}[-/]\d{1,2})|(\d{1,2}[-/]\d{1,2}[-/]\d{4})")
phone_number_re = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
ip_address_re = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
file_path_re = re.compile(r"^[.]?(/[^/ ]*)+/?$")
version_re = re.compile(r"(\d+\.)?(\d+\.)?(\*|\d+)\b")

def is_digit(str):
  """
  :param str: str to be checked
  :return: bool if string is digit only
  """
  return re.compile(num_re).match(str)

def validate_date(str):
  """
  :param str: string to be checked
  :return: bool if string is valid date
  """
  parts = filter(None, re.split(date_re, str))
  for p in parts:
    if date_re.match(p):
      try:
        date_parse(p)
      except ValueError:
        return False
  return True

def get_type(str):
  """
  :param str: string whose type is needed
  :return: type of the string 
  """
  if file_path_re.match(str):
    return 'file_path'

  elif date_re.findall(str) and validate_date(str):
    return 'date'

  elif phone_number_re.match(str):
    return 'phone_number'

  elif ip_address_re.match(str):
    return 'ip_address'

  elif money_re.match(str):
    return 'money'

  elif num_re.match(str):
    return 'number'

  elif version_re.match(str):
    return 'version'

  return 'alphanum'


"""
:param str: string whose compare value is needed
:return: compare value
"""

def get_cmp_file_path(str):
  file_parts = [int(x) if is_digit(x) else x for x in filter(None, re.split(r'/|(\d+)', str))]
  return (len(str.split('/')),) + tuple(file_parts)

def get_cmp_date(str):
  parts = filter(None, re.split(date_re, str))
  comp_value = tuple([calendar.timegm(date_parse(p).timetuple()) if date_re.match(p) else p for p in parts])
  return comp_value

def get_cmp_phone_number(str):
  return phone_number_re.match(str).groups()

def get_cmp_ipaddress(str):
  return tuple([int(x) for x in str.split('.')])

def get_cmp_money(str):
  return float(str.replace('$', ''))

def get_cmp_number(str):
  return float(str)

def get_cmp_version(str):
  return tuple([int(x) if re.compile(r'^[0-9]+$').match(x) else x for x in str.split('.')])

def get_cmp_alphanum(str):
  convert = lambda s: float(s) if num_re.match(s) else s
  return tuple([convert(c) for c in re.split('([0-9]+)', str.lower())])

# Mapping between type and compare function

type_comp_value_func_mapping = {
  'file_path': get_cmp_file_path,
  'date': get_cmp_date,
  'phone_number': get_cmp_phone_number,
  'ip_address': get_cmp_ipaddress,
  'money': get_cmp_money,
  'number': get_cmp_number,
  'version': get_cmp_version,
  'alphanum': get_cmp_alphanum
}

def get_compare_value_getter(type):
  """
  Getter function to get the comparing value getter function
  :param type: type of the string 
  :return: function to get the compare value 
  """
  return type_comp_value_func_mapping[type]