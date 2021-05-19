#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import yaml
from ops.testing import Harness
from charm import KafkaOperator


class KafkaCharmTest(unittest.TestCase):
    def setUp(self) -> None:
        self.harness = Harness(KafkaOperator)
        self.addCleanup(self.harness.cleanup)
        self.harness.begin()
        self.harness.add_oci_resource("kafka-image")

    def test_kafka_layer(self):

        expected = {
            "summary": "kafka layer",
            "description": "kafka layer",
            "services": {
                "kafka": {
                    "override": "replace",
                    "summary": "kafka service",
                    "command": "kafka",
                    "startup": "enabled",
                    "environment": {},
                }
            },
        }

        self.assertEqual(set(self.harness.charm._kafka_layer()), set(expected))
