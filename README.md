# MapReduce and Hadoop

This isn't a fully distributed operation but a single-node in a pseudo-distributed operation. Each Hadoop daemon runs in a serpate Java process.

We using Pride and Prejudice as our input.

```
# Format it
hdfs namenode -format

# Start NameNode daemon and DataNode daemon:
$HADOOP_HOME/sbin/start-dfs.sh

# Logs 
$HADOOP_HOME/logs

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

Resources: 
* https://www.shubhamdipt.com/blog/how-to-setup-hadoop-in-aws-ec2-instances/
** starting set up, also might be useful when full dis cluster
* https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/ClusterSetup.html
** to configure namenodes and datanodes
* https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html
** basic cluster setup
* https://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html
** hadoop streaming
* https://github.com/asmith26/python-mapreduce-examples/blob/master/word_frequencies/mapper.py
** python implementation
* https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html#User_Commands
** HDFS commands guide

