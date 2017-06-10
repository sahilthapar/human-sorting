import datetime
import re

num_re = re.compile(r"^[+-.]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?$")
money_re = re.compile(r"^\$\d+[.]?\d+$")
date_re = re.compile(r"^\d{4}[-/]\d{2}[-/]\d{2}$")
phone_number_re = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
ip_address_re = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
file_path_re = re.compile(r"^[.]?(/[^/ ]*)+/?$")
version_re = re.compile(r"(\d+\.)?(\d+\.)?(\*|\d+)")

def get_type(str_a):

  if file_path_re.match(str_a):
    return 'file_path'

  elif date_re.match(str_a):
    return 'date'

  elif phone_number_re.match(str_a):
    return 'phone_number'

  elif ip_address_re.match(str_a):
    return 'ip_address'

  elif money_re.match(str_a):
    return 'money'

  elif num_re.match(str_a):
    return 'number'

  elif version_re.match(str_a):
    return 'version'

  return 'alphanum'

def get_cmp_file_path(str):
  file_parts = str.split('/')
  return (len(file_parts),) + tuple(file_parts)

def get_cmp_date(str):
  return (datetime.datetime.strptime(str, '%Y-%m-%d') -
          datetime.datetime.utcfromtimestamp(0)).total_seconds()

def get_cmp_phone_number(str):
  return phone_number_re.match(str).groups()

def get_cmp_ipaddress(str):
  return tuple([int(x) for x in str.split('.')])

def get_cmp_money(str):
  return float(str.replace('$', ''))

def get_cmp_number(str):
  return float(str)

def get_cmp_version(str):
  return tuple([int(x) if re.compile(r'[0-9]+]').match(x) else x for x in str.split('.')])

def get_cmp_alphanum(str):
  convert = lambda s: float(s) if num_re.match(s) else s
  return tuple([convert(c) for c in re.split('([0-9]+)', str.lower())])

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
  return type_comp_value_func_mapping[type]