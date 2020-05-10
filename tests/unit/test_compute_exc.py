"""
 File: test_calculator_excptions.py
 Description: Testing methods for exception handling of INVALID calculator input
"""

import pytest
from calculator import Calculator, CalculatorError 

## list of (invalid-problem,) tuples to be used in parameterization input
PARAM_TUPS = [ 
 ('b',),          ## strin 
 ('+',),          ## operator only 
 ('1/2)',),       ## single paren 
 ('()',),         ## parens with no numbers 
 ('((2+2)',),     ## mis-matched parens
 ('(2,3+2)',),    ## comma 
 ('[2+2]',),      ## square-brackets 
 ('5(2+2)',),     ## missing operator: 5(2+2) must be witten as 5*(2+2) 
]

##------------------------------------------------------------------------
@pytest.mark.parametrize("invalid_problem", PARAM_TUPS)
def test_exception_on_invalid_problem(invalid_problem):
    """ 
     Verify that we raise an CalculatorError() exception as expected with invalid problem input 
    """ 
    invalid_problem = 'b'
    with pytest.raises(CalculatorError):
        calc = Calculator({})
        answer = calc.compute(invalid_problem)

