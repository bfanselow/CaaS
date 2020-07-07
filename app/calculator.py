
"""
  File: calculator.py
  Class: Calculator

  Description:
    Compute basic mathematical opertaions

  Credits:
    Calculator computations inspired by https://gist.github.com/technillogue/5887092


"""
import math
import json

## mathematical constants
constants = {
  'pi':  math.pi,
  'tau': math.tau,
  'e':   math.e
}

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "/": lambda x, y: x / y,
    "*": lambda x, y: x * y,
    "^": lambda x, y: x ** y
}
symbols = operations.keys()

##----------------------------------------------------------------------------
class CalculatorError(Exception):
  pass

##----------------------------------------------------------------------------
class Calculator(object):

  def __init__(self, d_init_args):
    """
      Placeholder - Currently not needed
    """
    pass 

  ##--------------------------------------------------------------------------
  def lex(self, expr):
    """
     Seperates numbers from symbols, recursively nests parens
    """
    tokens = []
    while expr:
        char, *expr = expr
        ## char is equal to the first charecter of the expression, expr is equal to the rest of it
        if char == "#": ## indicates comment line
            break
        if char == "(":
            try:
                ## expr is what's after the end of the paren - continue lexing after that
                paren, expr = self.lex(expr)
                tokens.append(paren)
            except ValueError:
                raise CalculatorError("Invalid expression - paren mismatch")
        elif char == ")":
            ## return the tokens leading up to the to the paren and the rest of the expression after it
            return tokens, expr
        elif char.isdigit() or char == ".":
            ## number or decimal
            try:
                if tokens[-1] in symbols:
                    tokens.append(char) ## start a new num
                elif type(tokens[-1]) is list:
                    raise CalculatorError("Invalid Expression - parens cannot be followed by numbers")
                    ## 5(3-2) must be written as 5*(3-2) 
                else:
                    tokens[-1] += char ## add to last num
            except IndexError: ## tokens is empty
                tokens.append(char) ## start first num
        elif char in symbols:
            tokens.append(char)
        elif char.isspace():
            pass
        else:
            raise CalculatorError("Invalid character in expression: [%s]" % char)
    return tokens

  ##--------------------------------------------------------------------------
  def evaluate(self, tokens):
    """
      Recursive evaluation of tokens
    """
    for symbol, func in operations.items():
        ## find an operation to eval in order
        try:
            pos = tokens.index(symbol)
            ## split the tokens by the operation and eval that
            leftTerm = self.evaluate(tokens[:pos])
            rightTerm = self.evaluate(tokens[pos + 1:])
            return func(leftTerm, rightTerm)
            ## return immediatly breaks all loops within the function
        except ValueError:
            pass ## index raises ValueError when it's not found
    if len(tokens) is 1:
        try:
            return float(tokens[0]) ## it must be a number
        except TypeError:
            return self.evaluate(tokens[0]) ## if it's not a number
    else:
        raise CalculatorError("Invalid expression: %s" % tokens)

  ##--------------------------------------------------------------------------
  def compute(self, problem_expression):
    """
      Compute the answer to the input problem_expression
      Return (float): answer
    """
    print("Computing problem...")
    lex_expr = self.lex(problem_expression)
    answer = self.evaluate(lex_expr)
    return(answer)
