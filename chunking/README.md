# Problem 2: Count words with letters 

Used RegEx: ^[A-Za-z]+$

### Sort and merge parts
```
sort -k 2nr part-0000* > combined-sorted
```

### Total number of unique terms
```
cat combined-sorted | wc -l
6670
```

### Fifth to last term and number of occurences 
```
yards	1
```

### First term and number of occurences 
```
the	4509
```
