# kafka-operator

## Description

This is the Kafka charm for Kubernetes using the Python Operator Framework.

## Usage


### Deploying

```
$ git clone https://github.com/martinrusev/kafka-operator
$ cd kafka-operator

$ sudo snap install charmcraft --beta
$ charmcraft build
Created 'kafka.charm'.


$ juju deploy ./kafka.charm --resource kafka-image=confluentinc/cp-kafka:5.4.4
```

## Developing

Create and activate a virtualenv with the development requirements:

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements-dev.txt
```


## Testing

The Python operator framework includes a very nice harness for testing
operator behaviour without full deployment. Just `run_tests`:

```
./run_tests
```

## Roadmap

The Kafka Charm is still a work in progress.
