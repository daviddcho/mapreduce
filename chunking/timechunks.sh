#!/bin/bash

nsize=5

# Create your chunks
# Then put your chunks in hdfs
for i in {1..5}; do 
 n=$(($i*$nsize))
 echo "Starting chunk $n"
 /usr/bin/time -a -o results -f "$n\t%e" ./stream.sh $n
 hdfs dfs -rm -r output
 echo "Finished chunk $n"
done
