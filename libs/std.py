import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

function_names = [
    ['std_cls', 'none'],
    ['std_split', 'list'],
    ['std_join', 'str'],
    ['std_replace', 'str'],
    ['std_append', 'none']
]
version = '0.2'

from src.ml_parser.value_mchine import Values
from src.ml_parser.errors import Errors, test_type
import os

def std_cls(_stroke: int):
    os.system('cls')

def std_split(_data: Values.ValStr, _separ: Values.ValStr = Values.ValStr(' '), _stroke: int = 0):
    if test_type(_data, 'str', 'split', _stroke) and test_type(_separ, 'str', 'std_split', _stroke):
        data = _data.get_value().split(_separ.get_value())
        data = [Values.ValStr(d) for d in data]
        return Values.ValList(data)
    
def std_join(_data: Values.ValList, _separ: Values.ValStr = Values.ValStr(' '), _stroke: int = 0):
    if test_type(_data, 'list', 'join', _stroke) and test_type(_separ, 'str', 'std_split', _stroke):
        stroke = ''
        for d in _data.get_value():
            stroke += str(d.get_value())+_separ.get_value()
        return Values.ValStr(stroke)

def std_replace(_data: Values.ValStr, _before, _after, _stroke):
    if (
        test_type(_data, 'str', 'replace', _stroke) and 
        test_type(_before, 'str', 'replace', _stroke) and 
        test_type(_after, 'str', 'replace', _stroke)
    ):
        s = _data.get_value()
        s = s.replace(_before.get_value(), _after.get_value())
        return Values.ValStr(s)
    
def std_append(_list: Values.ValList, _value, _stroke: int = 0):
    list = _list.get_value().append(_value)
    