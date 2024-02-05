"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.harbour_theme.logic import validators


def test_harbour_theme_reauired_with_valid_value():
    assert validators.harbour_theme_required("value") == "value"


def test_harbour_theme_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.harbour_theme_required(None)
