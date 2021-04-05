#!/bin/bash

mapred streaming -fs hdfs://localhost:9000 -input input/input.txt -output output -mapper ./mapper.py -reducer ./reducer.py -numReduceTasks 5




#mapred streaming -input pnp/input.txt -output output -mapper ./mapper.py -reducer ./reducer.py -numReduceTasks 5
