#!/bin/bash

nsize=5
input=biginput.txt
dir=chunks

# Create your chunks
# Then put your chunks in hdfs
for i in {1..8}; do 
 n=$(($i*$nsize))
 echo "Starting chunk $n"
 mkdir chunks${n}
 split -n $n $input
 mv x* chunks${n}
 hdfs dfs -mkdir chunks${n} 
 hdfs dfs -put chunks${n}/* chunks${n}
 rm -r chunks${n}
 echo "Finished chunk $n"
done
