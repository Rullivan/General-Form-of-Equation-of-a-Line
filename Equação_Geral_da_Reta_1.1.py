# The "sympy" mode is used here to store a mathematical variable within a system variable;
from sympy import Symbol
    x = Symbol('x')
    y = Symbol('y')

# Definition of constants, as well as the rule of the general equation, and the variables of points A (x, y) and B (x, y);
a11 = x
a12 = y
a13 = 1
a21 = int(input("Enter the value of x from point A: "))
a22 = int(input("Enter the value of x from point A: "))
a23 = 1
a31 = int(input("Enter the value of x from point B: "))
a32 = int(input("Enter the value of x from point B: "))
a33 = 1

# Sarrus's rule for solving a 3x3 matrix.
sarrus = (a11 * a22 * a33) + (a12 * a23 * a31) + (a13 * a21 * a32) - (a13 * a22 * a31) - (a21 * a12 * a33) - (a32 * a23 * a11)
    print("The general form of equation of a line formed by the points is: {} = 0".format(sarrus))
