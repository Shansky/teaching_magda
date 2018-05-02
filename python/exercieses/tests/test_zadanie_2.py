#!/bin/env python3

import pytest
import sys
sys.path.insert(0, '..')
from zadanie_2 import simpleArraySum

@pytest.mark.parametrize("arr,result", [
    ([1,2], 3),
    ([-1,2], 1),
    ([1,2,3,4,5], 15),
    ([1,2,3,4,5,6,7,8,9,0], 45),
])
def test_simpleArraySum(arr, result):
    assert  simpleArraySum(arr) == result
