import pytest
import json
import requests
from config import KEYS

import os


@pytest.mark.usefixtures("test_setup")
class TestAddApp:

    def add(self, a, b):
        result = a + b
        print(f"The sum of {a} and {b} is: {result}")

    # Create an instance of the class


calc = TestAddApp()

# Call the add function
calc.add(5, 3)
