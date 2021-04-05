# Problem 1: Word count

```
# Sort and merge parts
sort -k 2nr part-0000* > combined-sorted

# Total number of unique terms
> sorted-merged-parts | wc -l
7121

# Fifth to last term and its number of occurences
you—how	1

# First term and its number of occurences
1 4
```
