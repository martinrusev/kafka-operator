deploy:
  charmcraft build
	juju deploy ./kafka.charm --resource kafka-image=confluentinc/cp-kafka:6.1.1
