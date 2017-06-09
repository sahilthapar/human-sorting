import re
import datetime

num_re = re.compile(r"^[+-.]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?$")
money_re = re.compile(r"^\$\d+[.]?\d+$")
date_re = re.compile(r"^\d{4}[-/]\d{2}[-/]\d{2}$")
phone_number_re = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')

def regex_chooser(str_a):

  ret_a = {'value': str_a}

  if date_re.match(str_a):
    ret_a['type'] = 'date'
    ret_a['comp_value'] = (datetime.datetime.strptime(str_a, '%Y-%m-%d') - datetime.datetime.utcfromtimestamp(0)).total_seconds()

  elif phone_number_re.match(str_a):
    ret_a['type'] = 'phone_number'
    ret_a['comp_value'] = phone_number_re.match(str_a).groups()

  elif money_re.match(str_a):
    ret_a['type'] = 'money'
    ret_a['comp_value'] = float(str_a.replace('$', ''))

  elif num_re.match(str_a):
    ret_a['type'] = 'number'
    ret_a['comp_value'] = float(str_a)

  else:
    ret_a['type'] = 'letters'
    ret_a['comp_value'] = str_a.lower()

  return ret_a

def sortStrings(strings):
  typed_strings = [regex_chooser(i) for i in strings]
  sorted_strings = sorted(typed_strings, key=lambda x: (x['type'], x['comp_value']))
  return [x['value'] for x in sorted_strings]