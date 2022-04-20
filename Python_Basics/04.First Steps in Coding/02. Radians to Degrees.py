"""
Input1
3.1416

Output1
180.0004209182994

Input2
6.2832

Output2
360.0008418365988
"""

from math import pi
radians = float(input())
degrees = radians * 180 /pi
print(degrees)
