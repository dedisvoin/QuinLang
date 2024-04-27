import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

function_names = [
    ['time_time', 'str'],
    ['time_sec', 'int'],
    ['time_min', 'int'],
    ['time_hour', 'int'],
    ['sleep', 'none']
]
version = '0.0.1'

from src.ml_parser.value_mchine import Values
from src.ml_parser.errors import Errors, test_type
import time

def time_time(_stroke: int):
    t = time.ctime(time.time())
    return Values.ValStr(t)

def time_sec(_stroke: int):
    t = time.localtime(time.time())
    return Values.ValInt(t.tm_sec)

def time_min(_stroke: int):
    t = time.localtime(time.time())
    return Values.ValInt(t.tm_min)

def time_hour(_stroke: int):
    t = time.localtime(time.time())
    return Values.ValInt(t.tm_hour)

def sleep(_mili_seconds, _stroke: int):
    if test_type(_mili_seconds, ['int', 'float'], 'sleep', _stroke):
        time.sleep(_mili_seconds.get_value())
