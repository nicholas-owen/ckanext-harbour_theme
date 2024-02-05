"""Tests for helpers.py."""

import ckanext.harbour_theme.helpers as helpers


def test_harbour_theme_hello():
    assert helpers.harbour_theme_hello() == "Hello, harbour_theme!"
