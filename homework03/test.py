
from analyze_water import turbidity_calc, safe_threshold


import pytest


def test_turbidity():
        assert turbidity_calc( 0.947,1.26 ) == pytest.approx(1.19322)
        

def test_safe_threshold():
         assert safe_threshold(1.14 ) == pytest.approx(6.485678)

