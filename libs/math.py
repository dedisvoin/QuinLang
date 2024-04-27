import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

const_names = [
    ['math_pi', 'float']
]

function_names = [
    ['math_cos', 'float'],
    ['math_sin', 'float'],
    ['math_tan', 'float'],
    ['math_degrees', 'float']
]
version = '0.1'

from src.ml_parser.value_mchine import Values
from src.ml_parser.errors import Errors, test_type
import os
import math


math_pi = Values.ValFloat( math.pi )


def math_cos(_value: Values.ValInt | Values.ValFloat  ,_stroke: int = 0):
    if test_type(_value, ['int', 'float'], 'cos', _stroke):
        return Values.ValFloat(math.cos(_value.get_value()))
    

def math_sin(_value: Values.ValInt | Values.ValFloat  ,_stroke: int = 0):
    if test_type(_value, ['int', 'float'], 'sin', _stroke):
        return Values.ValFloat(math.sin(_value.get_value()))


def math_tan(_value: Values.ValInt | Values.ValFloat  ,_stroke: int = 0):
    if test_type(_value, ['int', 'float'], 'tan', _stroke):
        return Values.ValFloat(math.tan(_value.get_value()))
    
def math_degrees(_value: Values.ValInt | Values.ValFloat  ,_stroke: int = 0):
    if test_type(_value, ['int', 'float'], 'degrees', _stroke):
        return Values.ValFloat(math.degrees(_value.get_value()))
    
