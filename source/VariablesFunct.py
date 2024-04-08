from copy import copy


class ValueTypes:
    NUMBER = 'NUMBER'
    STRING = 'STRING'

    class NumberValue:
        def __init__(self, value) -> None:
            self.value = value
            self.type = ValueTypes.NUMBER

    class StringValue:
        def __init__(self, value) -> None:
            self.value = value
            self.type = ValueTypes.STRING



class Variables:
    vars_map = {}
    zero = 0
    stack = {}

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
        if not self.isExists(key):  return self.zero
        else:                       return self.vars_map[key]

    @classmethod
    def set(self, name: str, val):
        self.vars_map[name] = val