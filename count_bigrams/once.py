#!/usr/bin/python3

text = open("output/combined-sorted", "r")

total = 0
for line in text:
  bigram, count = line.split("\t") 
  if int(count) == 1:
    total += 1 

print(total)
