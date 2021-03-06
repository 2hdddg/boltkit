#!/usr/bin/env python
# coding: utf-8

# Copyright (c) 2002-2016 "Neo Technology,"
# Network Engine for Objects in Lund AB [http://neotechnology.com]
#
# This file is part of Neo4j.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from unittest import TestCase

from boltkit.client import Connection
from boltkit.server import Neo4jService


class ClientServerTestCase(TestCase):

    def test_connect_and_disconnect(self):
        with Neo4jService() as neo4j:
            with Connection.open(*neo4j.addresses, auth=neo4j.auth) as cx:
                self.assertEqual(cx.bolt_version, 3)
