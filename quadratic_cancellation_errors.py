#!/usr/bin/python
"""
The Quadratic Equation ax^2 + bx + c = has two solutions.
the solutiosn can be written as either:
    x1,2 = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
    x'1,2 = \frac{-2c}{-b \pm \sqrt{b^2 - 4ac}}
"""

VERSION = '$Id: $'
from cmath import sqrt

def quadratic_traditional(a,b,c):
    """
    Provides the two solutions in the normal form,
    x1,2 = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
    Inputs: a, b, and c are reals; they are the coefficients of the equation.
    Outputs: x1 and x2 are the two solutions. They are complex numbers.
    """
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return x1, x2
    
def quadratic_inverted(a,b,c):
    """
    Provides the two solutions in the inverted form,
    x1,2 = \frac{-2c}{-b \pm \sqrt{b^2 - 4ac}}
    Inputs: a, b, and c are reals; they are the coefficients of the equation.
    Outputs: x1 and x2 are the two solutions. They are complex numbers.
    """
    x1 = (-2*c)/(-b + sqrt(b**2 - 4*a*c))
    x2 = (-2*c)/(-b - sqrt(b**2 - 4*a*c))
    return x1, x2
