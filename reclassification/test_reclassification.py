import pandas as pd
from reclassification import calculate_idi, calculate_nri

def test_idi():
    assert calculate_idi([0,1,1,0],[0.2,0.6,0.3,0.1],[0.1,0.5,0.4,0.001]) == -0.09950000000000009

def test_nri():
    assert calculate_nri([0,1,1,0],[0.2,0.6,0.3,0.1],[0.1,0.5,0.4,0.001],0) == -1.0
