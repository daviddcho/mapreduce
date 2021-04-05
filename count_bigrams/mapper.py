#!/usr/bin/python3

import sys 
import string
import re

def remove_punctuation(s):
  return s.translate(str.maketrans("","", string.punctuation))

for line in sys.stdin:
  for word in re.split('^[A-Za-z]+$', line.strip().lower()).split():
    print("%s\t%s" % (word, 1))

"""
  for word in line.strip().lower().split():
    # Match only strings that have letters
    if re.match('^[A-Za-z]+$', word):
      print("%s\t%s" % (word, 1))
"""
