import numpy as np
import string
from sympy import *
import math
class CubicSpline:
    def __init__(self):
        self.functions = []
        self.functionsValues = []
        self.constants = []
        self.constantsUseds = []
        self.results = []
        self.px = []
        self.rows = []