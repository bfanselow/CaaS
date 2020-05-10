"""
 File: test_compute.py
 Description: pytest tests on the calaculate.py module 
 
"""
import pytest
import math
from calculator import Calculator  


## complex problem and answer
complx = '(((10.2*3)/(3+4))) + 66/(7*%s)' % math.pi
answer = 7.3726360697328825

## list of (problem, answer) tuples to be used in parameterization input
PARAM_TUPS =  [ 
 ('2+2', 4.0),          ## simple add
 ('(10-4)', 6.0),       ## simple subtract 
 ('22.6*2', 45.2),      ## simple mult 
 ('5/2', 2.5),          ## simple division 
 (complx, answer)       ## complicated 
]

##------------------------------------------------------------------------
@pytest.mark.parametrize("input_problem, exp_answer", PARAM_TUPS)
def test_compute(input_problem, exp_answer):
    """ 
      Test computuation of various math operations from parameterized input
    """ 
    calc = Calculator({})
    answer = calc.compute(input_problem)
    assert (answer == exp_answer) 
