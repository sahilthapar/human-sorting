import re
import datetime

num_re = re.compile(r"[+-.]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?")
money_re = re.compile(r"^\$\d+[.]?\d+$")
date_re = re.compile(r"^\d{4}[-/]\d{2}[-/]\d{2}$")

def regex_chooser(str_a):

  ret_a = {'value': str_a}

  if date_re.match(str_a):
    ret_a['type'] = 'date'
    ret_a['comp_value'] = (datetime.datetime.strptime(str_a, '%Y-%m-%d') - datetime.datetime.utcfromtimestamp(0)).total_seconds()

  elif money_re.match(str_a):
    ret_a['type'] = 'money'
    ret_a['comp_value'] = float(str_a.replace('$', ''))

  elif num_re.match(str_a):
    ret_a['type'] = 'number'
    ret_a['comp_value'] = float(str_a)

  return ret_a


def compare_strings(str_a, str_b):
  print str_a
  # Normalized strings
  nrm_a = str_a.lower()
  nrm_b = str_b.lower()
  EQUAL = 0
  SMALLER = -1
  GREATER = 1

  # Check if the strings are numbers
  chk_a = float(nrm_a) if num_re.match(nrm_a) else nrm_a
  chk_b = float(nrm_b) if re.compile(num_re).match(nrm_b) else nrm_b
  return EQUAL if chk_a == chk_b else (SMALLER if chk_a < chk_b else GREATER)


def sortStrings(strings):
  typed_strings = [regex_chooser(i) for i in strings]
  sorted_strings = sorted(typed_strings, key=lambda x: (['type'], x['comp_value']))
  return [x['value'] for x in sorted_strings]