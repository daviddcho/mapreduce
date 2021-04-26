# Time your chunks 

time cat ~/mapreduce/input/biginput.txt | ./mapper.py | sort | ./reducer.py
2.925s

# cool graph
```
# After you create your chunks
./timechunks.sh

python3 plot.py
```
![graph](graph.png)



