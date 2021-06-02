#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from ops.charm import CharmBase, PebbleReadyEvent
from ops.framework import StoredState
from ops.main import main
from ops.model import ActiveStatus, MaintenanceStatus
from ops.pebble import ServiceStatus, Layer, ServiceInfo

logger = logging.getLogger(__name__)

SERVICE = "kafka"
KAFKA_BASE_DIR = "/opt/bitnami/kafka"


class KafkaOperator(CharmBase):
    """Charm to run Kafka on Kubernetes."""

    _stored = StoredState()

    def __init__(self, *args):
        super().__init__(*args)

        self.framework.observe(self.on.kafka_pebble_ready, self._on_kafka_pebble_ready)

    def _restart_kafka(self):
        logger.info("Restarting kafka ...")

        container = self.unit.get_container(SERVICE)

        container.get_plan().to_yaml()
        status = container.get_service(SERVICE)
        if status.current == ServiceStatus.ACTIVE:
            container.stop(SERVICE)

        self.unit.status = MaintenanceStatus("kafka maintenance")
        container.start(SERVICE)
        self.unit.status = ActiveStatus("kafka restarted")

    def _on_kafka_pebble_ready(self, event: PebbleReadyEvent) -> None:
        container = self.unit.get_container(SERVICE)
        logger.info("_on_kafka_pebble_ready")

        logger.info("_start_kafka")
        layer = Layer(raw=self._kafka_layer())
        container.add_layer(SERVICE, layer, combine=True)
        container.autostart()
        self.unit.status = ActiveStatus("kafka started")

    def _kafka_layer(self) -> dict:
        config = self.model.config
        cluster_id = config["cluster_id"]
        layer = {
            "summary": "kafka layer",
            "description": "kafka layer",
            "services": {
                "kafka-setup": {
                    "override": "replace",
                    "summary": "kafka setup step - initialize & format storage",
                    "command": f"{KAFKA_BASE_DIR}/bin/kafka-storage.sh format -t {cluster_id} -c {KAFKA_BASE_DIR}/config/kraft/server.properties",
                    "startup": "enabled",
                },
                "kafka": {
                    "override": "replace",
                    "summary": "kafka service",
                    "command": f"{KAFKA_BASE_DIR}/bin/kafka-server-start.sh {KAFKA_BASE_DIR}/config/kraft/server.properties",
                    "startup": "enabled",
                    "requires": ["kafka-setup"],
                },
            },
        }

        return layer


if __name__ == "__main__":
    main(KafkaOperator)
