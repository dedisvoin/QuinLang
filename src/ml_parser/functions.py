from typing import Any
from src.ml_parser.inner_functions import (
    convert_int, convert_str, print_value, input_value, convert_float, convert_bool, println_value, get_type, len_list_or_str
)

class FunctionTypes:
    USER = 'user'
    INNER = 'inner'

class FunctionReturnType:
    INT = 'int'
    STR = 'str'
    LIST = 'list'
    BOOL = 'bool'
    FLOAT = 'float'
    VOID = 'void'

class ArgumentsConstructer:
    def __init__(self, args: list[list]) -> None:
        self.args = args

class Functions:
    __functions = {
        'int': [convert_int, FunctionTypes.INNER, FunctionReturnType.INT],
        'str': [convert_str, FunctionTypes.INNER, FunctionReturnType.STR],
        'out': [print_value, FunctionTypes.INNER, FunctionReturnType.VOID],
        'outln': [println_value, FunctionTypes.INNER, FunctionReturnType.VOID],
        'input': [input_value, FunctionTypes.INNER, FunctionReturnType.STR],
        'float': [convert_float, FunctionTypes.INNER, FunctionReturnType.FLOAT],
        'bool': [convert_bool, FunctionTypes.INNER, FunctionReturnType.BOOL],
        'type': [get_type, FunctionTypes.INNER, FunctionReturnType.STR],
        'len': [len_list_or_str, FunctionTypes.INNER, FunctionReturnType.INT]
    }

    @classmethod
    def set(self, _name: str, _function: Any, _type: str = FunctionTypes.INNER, _ret_type: str = FunctionReturnType.VOID, _args: list = []):
        self.__functions[_name] = [_function, _type, _ret_type, _args]

    @classmethod
    def get(self, _name: str):
        return self.__functions[_name]