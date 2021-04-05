# Problem 1: Word count

### Sort and merge parts
```
sort -k 2nr part-0000* > combined-sorted
```

### Total number of unique terms
```
cat combined-sorted | wc -l
7121
```

### Fifth to last term and its number of occurences
```
youths	1
```

### First term and its number of occurences
```
the	4509
```
