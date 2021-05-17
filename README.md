# MapReduce and Hadoop
Implemented some Map-reduce jobs for counting words and bigrams in big text files. Also, testing if feeding chunks into the Map-reduce model makes things faster or not.

This isn't a fully distributed operation but a single-node in a pseudo-distributed operation. 

We're using Pride and Prejudice as our input data: `/input/input.txt`.

## Useful commands 
```
# Format it
hdfs namenode -format

# Start NameNode daemon and DataNode daemon:
$HADOOP_HOME/sbin/start-dfs.sh

# Then create your user and such
# Run MapReduce with hadoop streaming
./stream.sh

# Copy input files to dfs
hdfs dfs -mkdir input
hdfs dfs -put input.txt input/

# Copy output to local system
hdfs dfs -get output output
cat output/

# or output files in dfs
hdfs dfs -cat output/*

# Stop the daemons
$HADOOP_HOME/sbin/stop-dfs.sh
```

This is where you overrode the defaultfs to hdfs://localhost:9000

$HADOOP_HOME/etc/hadoop/core-site.xml

## Resources
* Setting up (might be useful for full dis. cluster): https://www.shubhamdipt.com/blog/how-to-setup-hadoop-in-aws-ec2-instances/ 
* To configure namenodes and datanodes: https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/ClusterSetup.html 
* Basic cluster setup: https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html 
* Hadoop stream: https://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html  
* Map-reduce Python implementation: https://github.com/asmith26/python-mapreduce-examples/blob/master/word_frequencies/mapper.py
* HDFS commands: https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html#User_Commands
* HDFS architecture: https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html

In conclusion, just use pipes or something
