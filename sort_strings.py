import datetime
from utils import *

def normalize(str):
  # Strip trailing and leading white spaces
  # Replace multiple spaces with a single space
  # convert to lowercase

  return re.sub('\s+', ' ', str).strip().lower()

def add_type_compare_value(str):
  type = get_type(normalize(str))
  return {
    'value': str,
    'type': type,
    'comp_value': get_compare_value_getter(type)(str)
  }

def sortStrings(strings):
  typed_strings = [add_type_compare_value(i) for i in strings]
  sorted_strings = sorted(typed_strings, key=lambda x: (x['type'], x['comp_value']))
  return [x['value'] for x in sorted_strings]