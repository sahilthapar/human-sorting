import re
import datetime

# Most of the regex have been sourced from stackoverflow

num_re = re.compile(r"^[+-.]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?$")
money_re = re.compile(r"^\$\d+[.]?\d+$")
date_re = re.compile(r"^\d{4}[-/]\d{2}[-/]\d{2}$")
phone_number_re = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
ip_address_re = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
file_path_re = re.compile(r"^[.]?(/[^/ ]*)+/?$")

def regex_chooser(str_a):

  ret_a = {'value': str_a}
  if file_path_re.match(str_a):
    ret_a['type'] = 'file_path'
    file_parts = str_a.split('/')
    ret_a['comp_value'] = (len(file_parts), ) + tuple(file_parts)

  elif date_re.match(str_a):
    ret_a['type'] = 'date'
    ret_a['comp_value'] = (datetime.datetime.strptime(str_a, '%Y-%m-%d') -
                           datetime.datetime.utcfromtimestamp(0)).total_seconds()

  elif phone_number_re.match(str_a):
    ret_a['type'] = 'phone_number'
    ret_a['comp_value'] = phone_number_re.match(str_a).groups()


  elif ip_address_re.match(str_a):
    ret_a['type'] = 'ip_address'
    ret_a['comp_value'] = tuple([int(x) for x in str_a.split('.')])

  elif money_re.match(str_a):
    ret_a['type'] = 'money'
    ret_a['comp_value'] = float(str_a.replace('$', ''))

  elif num_re.match(str_a):
    ret_a['type'] = 'number'
    ret_a['comp_value'] = float(str_a)

  else:
    ret_a['type'] = 'alphanum'
    convert = lambda s: float(s) if num_re.match(s) else s
    ret_a['comp_value'] = tuple([convert(c) for c in re.split('([0-9]+)', str_a.lower())])
    print ret_a

  return ret_a

def sortStrings(strings):
  typed_strings = [regex_chooser(i) for i in strings]
  print typed_strings
  sorted_strings = sorted(typed_strings, key=lambda x: (x['type'], x['comp_value']))
  return [x['value'] for x in sorted_strings]