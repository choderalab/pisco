"""
Unit and regression test for the pisco package.
"""

# Import package, test suite, and other packages as needed
import pisco
import pytest
import sys

def test_pisco_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "pisco" in sys.modules
