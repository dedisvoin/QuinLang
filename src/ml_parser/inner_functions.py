from copy import copy
from typing import Any
from src.ml_parser.value_mchine import (
    ValueTypes, Values
)
from src.ml_parser.errors import Errors

def convert_int(_value: Values.ValInt | Values.ValStr | Values.ValFloat, _stroke = 0) -> Values.ValInt:
    try:
        return Values.ValInt(int(_value.get_value()))
    except:
        Errors.ERROR_CONVERT_TO_INT(_value.get_value(), _stroke)

def convert_float(_value: Values.ValInt | Values.ValStr | Values.ValFloat, _stroke = 0) -> Values.ValFloat:
    try:
        return Values.ValFloat(float(_value.get_value()))
    except:
        Errors.ERROR_CONVERT_TO_FLOAT(_value.get_value(), _stroke)

def convert_bool(_value: Values.ValInt | Values.ValStr, _stroke = 0) -> Values.ValBool:
    if _value.get_type() == ValueTypes.STR:
        if _value.get_value() in ('True', 'true','1'):
            return Values.ValBool(True)
        elif _value.get_value() in ('False', 'false','0'):
            return Values.ValBool(False)
        else:
            Errors.ERROR_CONVERT_TO_BOOL(_value.get_value(), _stroke)
    elif _value.get_type() == ValueTypes.INT or _value.get_type() == ValueTypes.FLOAT:
        if abs(_value.get_value()) >= 1:
            return Values.ValBool(True)
        elif _value.get_value() == 0:
            return Values.ValBool(False)
        else:
            Errors.ERROR_CONVERT_TO_BOOL(_value.get_value(), _stroke)
    else:
        Errors.ERROR_CONVERT_TO_BOOL(_value.get_value(), _stroke)

def convert_str(_value: Values.ValInt | Values.ValStr | Values.ValFloat, _stroke = 0) -> Values.ValStr:
    return Values.ValStr(str(_value.get_value()))

def print_value(*_values: list[Any], _stroke = 0):
    printed_values = [var.get_value() for var in _values]
    try:
        printed_values = [pv.replace('\\n','\n') for pv in printed_values]
    except:...
    print(*printed_values)

def println_value(*_values: list[Any], _stroke = 0):
    print(_values)

def input_value(_value: Values.ValStr = Values.ValStr(''), _stroke = 0):
    if _value.get_type() == ValueTypes.STR:
        value = input(_value.get_value())
        return Values.ValStr(value)
    else:
        Errors.ERROR_TYPE(_value.get_type(), _stroke, 'str')

def get_type(_value: Any, _stroke = 0):
    return Values.ValStr(_value.get_type())


# рекурсивно парсит массив и возвращает массив из простых элементов
def recursion_parse(_value: list, _inner: list) -> list[object]:
    new_inner = []
    for v in _value:
        cl = []
        if isinstance(v, Values.ValList):
            new_inner.append(recursion_parse(v.get_value(), cl))
        else:
            new_inner.append(v.get_value())
    _inner.append(new_inner)
    return _inner[0]


# функция конвертации
def convert_values(_value: list) -> list[object]:
    _c_values = []
    for _element in _value:
        _inner_list = []
        if isinstance(_element, Values.ValList):
            _c_values.append(recursion_parse(_element.get_value(), _inner_list))
        else:
            _c_values.append(_element.get_value())
    return _c_values


def print_value(*_values: list[Values.ValBool | Values.ValInt | Values.ValList | Values.ValFloat | Values.ValStr], _stroke = 0):
    c_values = convert_values(_values)
    print(*c_values)


def len_list_or_str(_value: Values.ValList | Values.ValStr, _stroke = 0):
    if isinstance(_value, (Values.ValList, Values.ValStr)):
        return Values.ValInt(len(_value.get_value()))
    else:
        raise 'error'