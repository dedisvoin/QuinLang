from copy import copy
from typing import Any


class Variables:
    __variables = {}
    __buffer_vaariables = {}

    @classmethod
    def in_buffer(self):
        self.__buffer_vaariables = copy(self.__variables)

    @classmethod
    def out_buffer(self):
        self.__variables = copy(self.__buffer_vaariables)
        self.__buffer_vaariables = {}

    @classmethod
    def out_variables(self):
        for name in self.__variables:
            try:
                print(f'{name} = {self.__variables[name][0].get_value()} {self.__variables[name][1]} {self.__variables[name][2]}')
            except:
                print(f'{name} = {self.__variables[name][0]} {self.__variables[name][1]} {self.__variables[name][2]}')

    @classmethod
    def is_in(self, _name: str) -> bool:
        if _name in self.__variables: return True
        return False
    
    @classmethod
    def get(self, _name: str):
        return self.__variables[_name]

    @classmethod
    def set(self, _name: str, _value: Any, _is_chaingable: bool = False, _type: str = 'NONE') -> None:
        if not self.is_in(_name):
            self.__variables[_name] = [_value, _is_chaingable, _type]
        else:
            variable = self.__variables[_name]
            if variable[1] == True:
                self.__variables[_name] = [_value, _is_chaingable, _type]
            else:
                raise 'Variable is not chaingable'