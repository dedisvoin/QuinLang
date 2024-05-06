import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

function_names = [
    ['std_cls', 'none'],
    ['std_str_split', 'list'],
    ['std_str_join', 'str'],
    ['std_str_replace', 'str'],
    ['std_list_append', 'none'],
    ['std_count', 'int'],
    ['std_cut', 'any'],
    ['std_str_upper', 'str'],
    ['std_str_lower',' str'],
    ['std_str_format',' str']
]
version = '0.2'

from src.ml_parser.value_mchine import Values
from src.ml_parser.errors import Errors, test_type
import os

def std_cls(_stroke: int):
    os.system('cls')

def std_str_split(_data: Values.ValStr, _separ: Values.ValStr = Values.ValStr(' '), _stroke: int = 0):
    if test_type(_data, 'str', 'split', _stroke) and test_type(_separ, 'str', 'std_split', _stroke):
        data = _data.get_value().split(_separ.get_value())
        data = [Values.ValStr(d) for d in data]
        return Values.ValList(data)
    
def std_str_join(_data: Values.ValList, _separ: Values.ValStr = Values.ValStr(' '), _stroke: int = 0):
    if test_type(_data, 'list', 'join', _stroke) and test_type(_separ, 'str', 'std_split', _stroke):
        stroke = ''
        for i, d in enumerate(_data.get_value()):
            if i!=len(_data.get_value())-1:
                stroke += str(d.get_value())+_separ.get_value()
            else:
                stroke += str(d.get_value())
        return Values.ValStr(stroke)

def std_str_replace(_data: Values.ValStr, _before, _after, _stroke):
    if (
        test_type(_data, 'str', 'replace', _stroke) and 
        test_type(_before, 'str', 'replace', _stroke) and 
        test_type(_after, 'str', 'replace', _stroke)
    ):
        s = _data.get_value()
        s = s.replace(_before.get_value(), _after.get_value())
        return Values.ValStr(s)
    
def std_list_append(_list: Values.ValList, _value, _stroke: int = 0):
    if test_type(_list, 'list', 'append', _stroke):
        arr = _list.get_value().append(_value)

def std_count(_value, _obj, _stroke: int = 0):
    if test_type(_obj, ['str' ,'int', 'float', 'bool'], 'count', _stroke):
        if test_type(_value, ['str','list'], 'count', _stroke):
            value = _obj.get_value()
            if _value.get_type() == 'str':
                detect_str = _value.get_value()
                c = detect_str.count(value)
                return Values.ValInt(c)
            if _value.get_type() == 'list':
                c = 0
                for val in _value.get_value():
                    if val.get_value() == value:
                        c+=1
                return Values.ValInt(c)

def std_cut(_value: Values.ValList | Values.ValStr, _start: Values.ValInt, _stop: Values.ValInt, _stroke: int = 0):
    if (test_type(_value, ['str','list'], 'cut', _stroke) and 
        test_type(_start, ['int'], 'cut', _stroke) and
        test_type(_stop, ['int'], 'cut', _stroke)
        ):
        if _value.get_type() == 'str':
            data = _value.get_value()
            start = _start.get_value()
            stop = _stop.get_value()
            return Values.ValStr(data[start:stop])
        if _value.get_type() == 'list':
            data = _value.get_value()
            start = _start.get_value()
            stop = _stop.get_value()
            return Values.ValList(data[start:stop])
    
def std_str_upper(_value: Values.ValStr, _stroke):
    if test_type(_value, 'str', 'upper', _stroke):
        return Values.ValStr(_value.get_value().upper())
    
def std_str_lower(_value: Values.ValStr, _stroke):
    if test_type(_value, 'str', 'lower', _stroke):
        return Values.ValStr(_value.get_value().lower())
    
def std_str_format(_value: Values.ValStr, setup_elements = [], _stroke = 0):
    if test_type(_value, 'str', 'format', _stroke):
        value = _value.get_value()
        new_text = ''
        n = 0
        
        for i, sym in enumerate(value):
            if value[i] == '}' and value[i-1] == '{':
                
                new_text+=str(setup_elements.get_value()[n].get_value())
                n+=1
                
            elif value[i] == '{':
                ...
            else:
                new_text+=sym

        return Values.ValStr(new_text)

   