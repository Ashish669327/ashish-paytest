import pytest

class TestAddApp:

    def add(self, a, b):
        return a + b

    def test_addition(self):  # Function name must start with 'test_'
        assert self.add(5, 3) == 8  # Simple test case
