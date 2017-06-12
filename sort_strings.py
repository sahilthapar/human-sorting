from utils import *

def normalize(str):
  """
    Removes trailing and leading whitespaces,
    Converts to lowercase
    Substitutes multiple spaces with a single one
    :param str: string to be normalized 
    :return: normalized string
  """
  return re.sub('\s+', ' ', str).strip().lower()

def add_type_compare_value(str):
  """
    :param str: string whose type and compare value we need 
    :return: dict with type, compare value and original value
  """
  str = str.encode('ascii', 'ignore')
  type = get_type(normalize(str))
  return {
    'value': str,
    'type': type,
    'comp_value': get_compare_value_getter(type)(str)
  }

def sort_strings(strings):
  """
    Sorts a list of strings for human readable sorting
    :param strings: list of strings to be sorted 
    :return: sorted list of strings
  """
  if len(strings) == 0:
    return strings
  typed_strings = [add_type_compare_value(i) for i in strings]
  sorted_strings = sorted(typed_strings, key=lambda x: (x['type'], x['comp_value']))
  return [x['value'] for x in sorted_strings]