# Problem 2: Count words with letters 

Used RegEx: ^[A-Za-z]+$

```
cat part-0000* | sort > sm-part

# Total number of unique terms
cat sm-part | wc -l
6670

# Fifth to last term and number of occurences 
your	464

# First term and number of occurences 
a	1995

```
