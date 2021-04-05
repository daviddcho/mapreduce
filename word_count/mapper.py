#!/usr/bin/python3

import sys 
import string
import fileinput

def remove_punctuation(s):
  return s.translate(str.maketrans("","", string.punctuation))

for line in sys.stdin:
  for word in remove_punctuation(line.strip().lower()).split():
    print("%s\t%s" % (word, 1))
