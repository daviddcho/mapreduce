# Problem 4: Count bigrams

```
# Without Hadoop
cat ~/mapreduce/input/input.txt | ./mapper.py | sort | ./reducer.py

# With Hadoop if you got it setup
./stream.sh
```

### Combine all the parts and sort
```
sort -k 3nr part-0000* > combined-sorted
```

### How many unique bigrams?
```
cat combined-sorted | wc -l 
50823
```

### Top ten most frequent bigrams and their counts
```
of the	465
to be	424
in the	375
i am	288
to the	250
of her	242
it was	230
of his	226
mr darcy	223
she was	199
```

### Cumulative frequency of the top ten bigrams
```
./frequency.py
2992 out of 112531, 2.60% 
```

### How many bigrams appear only once?
```
./once.py
37535

```
