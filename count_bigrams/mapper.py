#!/usr/bin/python3

import sys 
import string
import re
from nltk import word_tokenize
from nltk.util import ngrams

goodbye = string.punctuation + string.digits

def remove_punctuation(s):
  return s.translate(str.maketrans("","", goodbye))

for line in sys.stdin:
  line = remove_punctuation(line.strip().lower())
  token = word_tokenize(line) 
  bigrams = list(ngrams(token, 2))  
  for bigram in bigrams:
    print("%s %s\t%s" % (bigram[0], bigram[1], 1))

