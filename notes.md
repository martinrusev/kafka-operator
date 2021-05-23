##  Kafka docker image references

Kafka related binaries and docker config files are located in:


```
# /usr/bin
-rwxr-xr-x 1 root root  82K Aug  4  2020  kadmin
-rwxr-xr-x 1 root root  858 Mar 16 22:52  kafka-acls
-rwxr-xr-x 1 root root  870 Mar 16 22:52  kafka-broker-api-versions
-rwxr-xr-x 1 root root  861 Mar 16 22:52  kafka-configs
-rwxr-xr-x 1 root root  942 Mar 16 22:52  kafka-console-consumer
-rwxr-xr-x 1 root root  941 Mar 16 22:52  kafka-console-producer
-rwxr-xr-x 1 root root  868 Mar 16 22:52  kafka-consumer-groups
-rwxr-xr-x 1 root root  945 Mar 16 22:52  kafka-consumer-perf-test
-rwxr-xr-x 1 root root  868 Mar 16 22:52  kafka-delegation-tokens
-rwxr-xr-x 1 root root  866 Mar 16 22:52  kafka-delete-records
-rwxr-xr-x 1 root root  863 Mar 16 22:52  kafka-dump-log
-rwxr-xr-x 1 root root  860 Mar 16 22:52  kafka-features
-rwxr-xr-x 1 root root  867 Mar 16 22:52  kafka-leader-election
-rwxr-xr-x 1 root root  860 Mar 16 22:52  kafka-log-dirs
-rwxr-xr-x 1 root root  859 Mar 16 22:52  kafka-mirror-maker
-rwxr-xr-x 1 root root  883 Mar 16 22:52  kafka-preferred-replica-election
-rwxr-xr-x 1 root root  956 Mar 16 22:52  kafka-producer-perf-test
-rwxr-xr-x 1 root root  871 Mar 16 22:52  kafka-reassign-partitions
-rwxr-xr-x 1 root root  871 Mar 16 22:52  kafka-replica-verification
-rwxr-xr-x 1 root root  11K Mar 16 22:52  kafka-run-class
-rwxr-xr-x 1 root root 1.9K Mar 16 22:52  kafka-server-start
-rwxr-xr-x 1 root root 1.7K Mar 16 22:52  kafka-server-stop
-rwxr-xr-x 1 root root  942 Mar 16 22:52  kafka-streams-application-reset
-rwxr-xr-x 1 root root  860 Mar 16 22:52  kafka-topics
-rwxr-xr-x 1 root root  955 Mar 16 22:52  kafka-verifiable-consumer
-rwxr-xr-x 1 root root  955 Mar 16 22:52  kafka-verifiable-producer
-rwxr-xr-x 1 root root  864 Mar 16 22:52  zookeeper-security-migration
-rwxr-xr-x 1 root root 1.9K Mar 16 22:52  zookeeper-server-start
-rwxr-xr-x 1 root root 1.4K Mar 16 22:52  zookeeper-server-stop
-rwxr-xr-x 1 root root 1016 Mar 16 22:52  zookeeper-shell
```

```
ls -lh /etc/confluent/docker/
total 40K
-rw-r--r-- 1 appuser appuser  775 Apr 29 23:55 bash-config
-rwxr-xr-x 1 appuser appuser 4.3K Apr 30 00:05 configure
-rwxr-xr-x 1 appuser appuser 1.1K Apr 30 00:05 ensure
-rw-r--r-- 1 appuser appuser 1.2K Apr 30 00:05 kafka.properties.template
-rwxr-xr-x 1 appuser appuser 1.9K Apr 30 00:05 launch
-rw-r--r-- 1 appuser appuser  801 Apr 30 00:05 log4j.properties.template
-rw-r--r-- 1 appuser appuser 1.1K Apr 29 23:55 mesos-setup.sh
-rwxr-xr-x 1 appuser appuser 1.1K Apr 30 00:05 run
-rw-r--r-- 1 appuser appuser  305 Apr 30 00:05 tools-log4j.properties.template
```

- Docker image instructions:

https://docs.confluent.io/platform/current/installation/docker/config-reference.html


## Useful commands

- Get the confluent platform version

```
/usr/bin/kafka-broker-api-versions --bootstrap-server localhost:9092 --version
```

To check the corresponding kafka version:

https://docs.confluent.io/platform/current/release-notes/index.html


## Charm specifics

Relating with zookeeper:


```
juju deploy charmed-osm-zookeeper-k8s
```
