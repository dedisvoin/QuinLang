from copy import copy


"""
Defines the value types and corresponding value classes used in the application.

The `ValueTypes` class defines the available value types, which are `NUMBER` and `STRING`.

The `NumberValue` and `StringValue` classes represent values of the corresponding types, and each hold the actual value and the type.
"""
class ValueTypes:
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    BOOL = 'BOOL'
    NONE = 'NONE'

    class NumberValue:
        def __init__(self, value) -> None:
            self.value = value
            self.type = ValueTypes.NUMBER

    class StringValue:
        def __init__(self, value) -> None:
            self.value = value
            self.type = ValueTypes.STRING

    class BoolValue:
        def __init__(self, value) -> None:
            self.value = value
            self.type = ValueTypes.BOOl

    class NoneValue:
        def __init__(self) -> None:
            self.value = None
            self.type = ValueTypes.NONE



"""
Provides a set of utility functions for managing variables in the application.

The `Variables` class serves as a global namespace for variable management, including:
- Storing and retrieving variable values
- Pushing and popping variable states to/from a stack
- Checking if a variable exists
- Getting the value of a variable
- Setting the value of a variable

The `zero` attribute holds a `NumberValue` instance representing the value 0, which is used as a default value when a variable does not exist.
"""
class Variables:
    vars_map = {}
    zero = ValueTypes.NumberValue(0)
    stack = {}

    @classmethod
    def print_vars(self):
        for name in self.vars_map:
            print(name,':', self.vars_map[name][0].value,'changed:', self.vars_map[name][1])

    @classmethod
    def push(self):
        self.stack = {}
        for var in self.vars_map:
            self.stack[var] = copy(self.vars_map[var])

    @classmethod
    def pop(self):
        self.vars_map = {}
        for var in self.stack:
            self.vars_map[var] = self.stack[var]

    @classmethod
    def is_exists(self, key):
        return key in self.vars_map.keys()
    
    @classmethod
    def get(self, key):
        if not self.is_exists(key):  return self.zero
        else:                       return self.vars_map[key]

    @classmethod
    def get_type(self, key):
        if not self.is_exists(key):  return self.zero
        else:                       return self.vars_map[key][1]

    @classmethod
    def set(self, name: str, val, changed=True):
        self.vars_map[name] = (val, copy(changed))