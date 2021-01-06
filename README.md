# SF-Crime-Statistics-With-Spark-Streaming

## Step 1

Steps to run the application and test it on Udacity Workspace.

1. Run Zookeeper.

  `/usr/bin/zookeeper-server-start config/zookeeper.properties`

2. Run Kafka.

  `/usr/bin/kafka-server-start config/server.properties`

3. Run the producer that inputs data from a file and produces into the topic.

  `python kafka_server.py`

4. Consumer to test whether the data is produced correctly.

  `kafka-console-consumer --topic <YOUR-TOPIC-NAME> --from-beginning --bootstrap-server localhost:9092`

### Kafka Consumer Output

![kafka consumer output 1](Screenshots/consumer-sc1.png)
![kafka consumer output 1](Screenshots/consumer-sc2.png)
