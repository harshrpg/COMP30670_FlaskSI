#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `flask_system_info` package."""


import unittest
from click.testing import CliRunner

from flask_system_info import flask_system_info
from flask_system_info import cli


class TestFlask_system_info(unittest.TestCase):
    """Tests for `flask_system_info` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'flask_system_info.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
