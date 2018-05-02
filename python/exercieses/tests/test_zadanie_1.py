#!/bin/env python3

import pytest
import sys
sys.path.insert(0, '..')
from zadanie_1 import solveMeFirst

@pytest.mark.parametrize("x,y,result", [
    (2, 3, 5),
    (30, 10, 40),
    (20, 2, 22),
    (20, -2, 18),
    (10000, -10000, 0),
])
def test_solveMeFirst(x, y, result):
    assert  solveMeFirst(x, y) == result
