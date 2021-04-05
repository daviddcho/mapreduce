#!/usr/bin/python3

import sys

current_bigram = None
current_count = 0 
bigram = None

for line in sys.stdin:
  line = line.strip("\t") 
  bigram, count = line.split("\t", 1) 

  # Convert count to int 
  try:
    count = int(count) 
  except ValueError:
    continue
  
  if current_bigram == bigram:
    current_count += count
  else:
    if current_bigram:
      print("%s\t%s" % (current_bigram, current_count))
    current_count = count 
    current_bigram = bigram

# Output the last word if needed 
if current_bigram == bigram:
  print("%s\t%s" % (current_bigram, current_count))
