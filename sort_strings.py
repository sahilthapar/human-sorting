import re

def compare_strings(str_a, str_b):
  print str_a
  # Normalized strings
  nrm_a = str_a.lower()
  nrm_b = str_b.lower()
  EQUAL = 0
  SMALLER = -1
  GREATER = 1

  # Check if the strings are numbers
  num_re = r"[+-.]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?"
  chk_a = float(nrm_a) if re.compile(num_re).match(nrm_a) else nrm_a
  chk_b = float(nrm_b) if re.compile(num_re).match(nrm_b) else nrm_b
  return EQUAL if chk_a == chk_b else (SMALLER if chk_a < chk_b else GREATER)


def sortStrings(strings):
  return sorted(strings, cmp=compare_strings)