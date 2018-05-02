#!/bin/env python3

import pytest
import sys
sys.path.insert(0, '..')
from zadanie_3 import factorial

@pytest.mark.parametrize("number,result", [
    (1, 1),
    (0, 1),
    (2, 2),
    (4, 24),
    (8, 40320),
    (45, 119622220865480194561963161495657715064383733760000000000),
    (-1, 1),
])
def test_factorial(number, result):
    assert  factorial(number) == result
