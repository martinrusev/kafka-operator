deploy:
	charmcraft build
	juju deploy ./kafka.charm --resource kafka-image=confluentinc/cp-kafka:6.1.1


remove:
	juju remove-application kafka --force


juju_reset:
	juju destroy-controller kafka --destroy-all-models --destroy-storage

juju_setup:
	uju bootstrap microk8s kafka
