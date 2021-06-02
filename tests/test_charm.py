#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import yaml
from ops.testing import Harness
from charm import KafkaOperator

BASE_CONFIG = {
    "cluster_id": "test-id",
}


class KafkaCharmTest(unittest.TestCase):
    def setUp(self) -> None:
        self.harness = Harness(KafkaOperator)
        self.addCleanup(self.harness.cleanup)
        self.harness.begin()
        self.harness.add_oci_resource("kafka-image")
        self.harness.update_config(BASE_CONFIG)

    def test_kafka_layer(self):

        expected = {
            "summary": "kafka layer",
            "description": "kafka layer",
            "services": {
                "kafka-setup": {
                    "override": "replace",
                    "summary": "kafka setup step - initialize & format storage",
                    "command": "/opt/bitnami/kafka/bin/kafka-storage.sh format -t test-id -c /opt/bitnami/kafka/config/kraft/server.properties",
                    "startup": "enabled",
                },
                "kafka": {
                    "override": "replace",
                    "summary": "kafka service",
                    "command": "/opt/bitnami/kafka/bin/kafka-server-start.sh /opt/bitnami/kafka/config/kraft/server.properties",
                    "startup": "enabled",
                    "requires": ["kafka-setup"],
                },
            },
        }

        assert self.harness.charm._kafka_layer() == expected
