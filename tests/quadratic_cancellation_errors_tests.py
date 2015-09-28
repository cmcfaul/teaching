from nose.tools import *
import numpy as np
from computational import quadratic_cancellation_errors as quad
from cmath import sqrt

def setup():
	print "SETUP!"

def teardown():
	print "TEAR DOWN!"

def test_basic():
	print "I RAN!"

def test_quadratic_traditional():
    x1,x2 = quad.quadratic_traditional(2,0,-1)
    np.testing.assert_almost_equal(x1,0.5*sqrt(2))
    np.testing.assert_almost_equal(x2,-0.5*sqrt(2))
    
def test_quadratic_inverted():
    x1,x2 = quad.quadratic_inverted(2,0,-1)
    np.testing.assert_almost_equal(x1,0.5*sqrt(2))
    np.testing.assert_almost_equal(x2,-0.5*sqrt(2))
