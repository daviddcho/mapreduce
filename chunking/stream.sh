#!/bin/bash
mapred streaming -fs hdfs://localhost:9000 -input input/ -output output -mapper ./mapper.py -reducer ./reducer.py -numReduceTasks 5
