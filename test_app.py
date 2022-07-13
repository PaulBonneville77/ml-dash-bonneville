from app import get_prediction

import unittest
from unittest.mock import patch
from werkzeug import exceptions

# Check if prediction is positive
def test_prediction_is_positive():
    input = [[100,4,0],[120,5,1]]
    result = [get_prediction(setting[0], setting[1], setting[2]) for setting in input]
    assert all(price > 0 for price in result)