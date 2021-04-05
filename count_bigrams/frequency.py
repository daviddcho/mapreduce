#!/usr/bin/python3

import sys

def total_count(text):
  total = 0
  for line in text:
    bigram, count = line.split("\t") 
    total += int(count)
  return total

def top_ten_count(text):
  total = 0
  i = 0
  for line in text:
    if i >= 10: 
      break
    bigram, count = line.split("\t") 
    total += int(count)
    i += 1
  return total

text = open("output/combined-sorted", "r")
total = total_count(text)
text = open("output/combined-sorted", "r")
tt_total = top_ten_count(text)

freq = (tt_total/total)*100
print("%d out of %d" % (tt_total, total))

print("%.2f percent" % freq)
