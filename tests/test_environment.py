"""Unit test for amulet.environment"""

import unittest

from amulet.environment import Environment
from mock import patch


class EnvironmentTests(unittest.TestCase):
    @patch('amulet.environment.JujuEnv')
    def test_init(self, mjujuenv):
        Environment('127.0.0.1', 'sosekret')
        mjujuenv.assert_called_with('ws://127.0.0.1:17070')
        mjujuenv.return_value.login.assert_called_with('sosekret')
