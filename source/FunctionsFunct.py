import math
from source.VariablesFunct import *
from source.Errors import *


"""
Provides a set of mathematical functions that can be applied to values in the application.

funct_sin(num: NumberValue) -> NumberValue
    Calculates the sine of the given number value.

funct_cos(num: NumberValue) -> NumberValue
    Calculates the cosine of the given number value.

funct_int(num: Value) -> NumberValue
    Converts the given value to an integer. If the value is a number, it will return the integer part. If the value is a boolean, it will return 1 for True and 0 for False.

funct_float(num: NumberValue) -> NumberValue
    Converts the given number value to a float.

funct_str(val: Value) -> StringValue
    Converts the given value to a string.

funct_round(val: NumberValue, digits: NumberValue) -> NumberValue
    Rounds the given number value to the specified number of digits.

funct_print(*values: Value)
    Prints the given values to the console.
"""
def funct_sin(num):
    if isinstance(num, ValueTypes.NumberValue):
        n = ValueTypes.NumberValue( math.sin(num.value) )
        return n

def funct_cos(num):
    if isinstance(num, ValueTypes.NumberValue):
        n = ValueTypes.NumberValue( math.cos(num.value) )
        return n

def funct_int(num):
    if num.type == ValueTypes.NUMBER:
        num = str(num.value)
        if num.count('.')==1:
            return ValueTypes.NumberValue(int(num.split('.')[0]))
        else:
            return ValueTypes.NumberValue(int(num))
    elif num.type == ValueTypes.BOOL:
        return ValueTypes.NumberValue(int(num.value))
    elif num.type == ValueTypes.STRING:
        return ValueTypes.NumberValue(int(num.value))
        
def funct_float(num):
    if isinstance(num, ValueTypes.NumberValue):
        n = ValueTypes.NumberValue(float(num.value))
        return n
    
def funct_str(val):
    n = ValueTypes.StringValue(str(val.value))
    return n

def funct_round(val, digits):
    if isinstance(val, ValueTypes.NumberValue) and isinstance(digits, ValueTypes.NumberValue):
        return ValueTypes.NumberValue(round(val.value, int(digits.value)))

def funct_type(val):
    return ValueTypes.StringValue(val.type)

def recursion_array(value, cl):
    nc = []
    for n in value:
        cl = []
        if isinstance(n, ValueTypes.ArrayValue):
            nc.append(recursion_array(n.value, cl)[0])     
        else:
            nc.append(n.value)
    cl.append(nc)
    return cl
    
def funct_print(*values):
    values = [value.value for value in values]
    converted_values = []
    for value in values:
        cl = []
        if isinstance(value, list):
            converted_values.append(recursion_array(value, cl)[0])
        else:
            converted_values.append(value)
    print(*converted_values)

def funct_input(*values):
    if len(values)==1:
        return ValueTypes.StringValue(input(values[0].value))
    elif len(values) == 0:
        return ValueTypes.StringValue(input())
    else:
        raise 'error'

def funct_len(value):
    if isinstance(value, (ValueTypes.ArrayValue, ValueTypes.StringValue)):
        return ValueTypes.NumberValue(len(value.value))
        

"""
Represents a base function that can be executed with a list of values.

Args:
    funct (callable): The function to be executed.
    returned (bool, optional): Indicates whether the function should return a value. Defaults to True.

Attributes:
    returned (bool): Indicates whether the function should return a value.
    funct (callable): The function to be executed.

Methods:
    exec(values: list): Executes the function with the provided values. If `returned` is True, the function's return value is returned. Otherwise, the function is executed without returning a value.
"""
class BaseFunction:
    def __init__(self, funct, returned = True) -> None:
        self.returned = returned
        self.funct = funct
    
    def exec(self, values):
        
        if self.returned:
            val = self.funct(*values)
            return val
        else:
            self.funct(*values)


"""
Provides a mapping of function names to `BaseFunction` instances, allowing for the execution of various functions.

The `Functions` class serves as a registry for different functions that can be executed within the application. It maintains a `fun_map` dictionary that maps function names to corresponding `BaseFunction` instances, which encapsulate the function implementation and execution logic.

The class provides the following functionality:

- `isExists(key)`: Checks if a function with the given `key` (name) exists in the `fun_map`.
- `get(key)`: Retrieves the `BaseFunction` instance associated with the given `key` (name). If the function is not found, it raises a `BaseError.FUNCTION_NOT_FOUND` error.
- `set(name, val)`: Adds or updates a `BaseFunction` instance in the `fun_map` with the given `name` and `val`.

This class serves as a centralized point of access for the various functions available in the application, providing a consistent and extensible way to manage and execute them.
"""
class Functions:
    fun_map = {
        'sin':  BaseFunction(funct_sin),
        'cos': BaseFunction(funct_cos),
        'int': BaseFunction(funct_int),
        'str': BaseFunction(funct_str),
        'print': BaseFunction(funct_print, False),
        'float': BaseFunction(funct_float),
        'round': BaseFunction(funct_round),
        'input': BaseFunction(funct_input),
        'len': BaseFunction(funct_len),
        'type':BaseFunction(funct_type)
    }

    @classmethod
    def isExists(self, key):
        return key in self.fun_map.keys()
    
    @classmethod
    def get(self, key):
        if not self.isExists(key): 
            BaseError.FUNCTION_NOT_FOUND(self.name)
        else:   return self.fun_map[key]

    @classmethod
    def set(self, name: str, val):
        self.fun_map[name] = val