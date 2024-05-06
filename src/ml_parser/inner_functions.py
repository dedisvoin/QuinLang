from copy import copy
from typing import Any
import random

from src.ml_parser.value_mchine import (
    ValueTypes, Values
)
from src.ml_parser.errors import Errors, test_type, test_instance
from src.ml_parser.expressions import LambdaExpr
from src.ml_parser.variables import Variables

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

def println_value(*_values: list[Values.ValBool | Values.ValInt | Values.ValList | Values.ValFloat | Values.ValStr], _stroke = 0):
    c_values = convert_values(_values)
    print(*c_values, end=' ')


def len_list_or_str(_value: Values.ValList | Values.ValStr, _stroke = 0):
    if isinstance(_value, (Values.ValList, Values.ValStr)):
        return Values.ValInt(len(_value.get_value()))
    else:
        raise 'error'
    
def get_random_number(*_values: list[Values.ValInt, Values.ValInt], _stroke = 0):
    n1 = _values[0]
    n2 = _values[1]
    if test_type(n1, 'int', 'randint', _stroke) and test_type(n2, 'int', 'randint', _stroke):
        return Values.ValInt(random.randint(n1.get_value(), n2.get_value()))

def get_radnom_choise(_value: Values.ValList, _stroke = 0):
    if test_type(_value, ('list','str'), 'choise', _stroke):
        index = random.randint(0, len(_value.get_value())-1)
        if _value.get_type() == 'list':
            return copy(_value.get_value()[index])
        elif _value.get_type() == 'str':
            return Values.ValStr(copy(_value.get_value()[index]))
    
def fn_filter(_arr_intr: Values.ValList, _lambda, _stroke):
    arr = []
    if test_type(_arr_intr, 'list', 'filter', _stroke) and test_instance(_lambda, LambdaExpr, _stroke, 'filter'):
        for elem in _arr_intr.get_value():
            if _lambda.eval([elem]).get_value() == True:
                arr.append(elem)
        return Values.ValList(arr)
    
def fn_map(_arr_intr: Values.ValList, _lambda, _stroke):
    from src.ml_parser.statements import Statemets
    arr = []
    
    if test_type(_arr_intr, ['list','str'], 'map', _stroke):
        if isinstance(_lambda, list):
            args = _lambda[3]
            state = _lambda[0]
            ret_type = _lambda[2]

           
            if _arr_intr.get_type() == 'list':
                for elem in _arr_intr.get_value():
                    
                    if elem.get_type() in args[0][1]:
                        Variables.set(args[0][0], elem, True, elem.get_type())
                    else:
                        Errors.ERROR_ARGUMENT_TYPE('callback', args[0][0], args[0][1], elem.get_type(), _stroke, 0)
                    try:
                        state.exec()
                    except Statemets.ReturnState as exp:
                        
                        val = exp.get_result()
                        
                        if not (val.get_type() in ret_type):
                            Errors.ERROR_OUT_ARGUMENT_TYPE('callback', ret_type, val.get_type(), _stroke)
                        arr.append(val)
            elif _arr_intr.get_type() == 'str':

                for elem in _arr_intr.get_value():
                    elem = Values.ValStr(elem)
                    if elem.get_type() == args[0][1]:
                        Variables.set(args[0][0], elem, True, elem.get_type())
                    else:
                        Errors.ERROR_ARGUMENT_TYPE('callback', args[0][0], args[0][1], elem.get_type(), _stroke, 0)
                    try:
                        state.exec()
                    except Statemets.ReturnState as exp:
                        
                        val = exp.get_result()
                        
                        if not (val.get_type() in ret_type):
                            Errors.ERROR_OUT_ARGUMENT_TYPE('callback', ret_type, val.get_type(), _stroke)
                        arr.append(val)


            
            return Values.ValList(arr)
                
        elif test_instance(_lambda, LambdaExpr, _stroke, 'map'):
            dummy = []
            
            for elem in _arr_intr.get_value():
                if isinstance(elem, str):
                    dummy.append(Values.ValStr(elem))
                else:
                    dummy.append(copy(elem))
            _arr_intr = Values.ValList(dummy)

            if _arr_intr.get_type() == 'list':
                for elem in _arr_intr.get_value():
                    arr.append(_lambda.eval([copy(elem)]))
                
                
                return Values.ValList(arr)
            
        
def fn_bin(_int_or_float_value: Values.ValInt | Values.ValFloat, _stroke):
    if test_type(_int_or_float_value, ['int'], 'bin', _stroke):
        data = bin(_int_or_float_value.get_value())[2:]
        return Values.ValStr(data)
    
def fn_number(_str_value: Values.ValStr, _osn_number: Values.ValInt = Values.ValInt(2), _stroke: int = 0):
    if test_type(_str_value, ['str'], 'number', _stroke) and test_type(_osn_number, ['int'], 'number', _stroke):
        return Values.ValInt(int(_str_value.get_value(), _osn_number.get_value()))
