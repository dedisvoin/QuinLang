import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from GLib.window import *
from GLib.inputs import *
from GLib.drawing import *


function_names = [
    ['gl_window_create', 'none'],
    ['gl_window_set_maxfps', 'none'],
    ['gl_window_set_bgcolor', 'none'],
    ['gl_window_viewfps', 'none'],
    ['gl_loop', 'bool'],
    ['gl_events_update', 'none'],
    ['gl_mouse_pos', 'list'],
    ['gl_mouse_press_left', 'bool'],
    ['gl_mouse_press_right', 'bool'],
    ['gl_mouse_click_left', 'bool'],
    ['gl_mouse_click_right', 'bool'],
    ['gl_draw_circle', 'none'],
    ['gl_math_distance', 'float']
]
version = '0.5'

from src.ml_parser.value_mchine import Values
from src.ml_parser.errors import Errors, test_type
import os

window = None
window_events = None
window_bg_color = [255,255,255]
def gl_window_create(_size: Values.ValList, _title: Values.ValStr, _stroke):
    if test_type(_size, 'list', 'window_create', _stroke):
        global window, window_events
        size = [val.get_value() for val in _size.get_value()]
        window_events = WindowEvents()
        window = Window(
            size=size, title=_title.get_value(), events=window_events,
        )

def gl_window_viewfps(_stroke: int = 0):
    window.view_fps()

def gl_window_set_bgcolor(_value: Values.ValList, _stroke: int = 0):
    global window_bg_color
    window_bg_color = _value.get_value()

def gl_window_set_maxfps(_value: Values.ValInt, _stroke):
    window.fps = _value.get_value()

def gl_events_update(_stroke):
    global window_events, events
    window_events.update()
    events.update()

def gl_loop(_stroke: int = 0):
    return Values.ValBool(window())

events = Events()
events.add_mouse_event(Mouse.bt_left, 'left_click', Mouse.click_event)
events.add_mouse_event(Mouse.bt_right, 'right_click', Mouse.click_event)
events.add_mouse_event(Mouse.bt_left, 'left_press', Mouse.press_event)
events.add_mouse_event(Mouse.bt_left, 'right_press', Mouse.press_event)

def gl_mouse_pos(_stroke: int = 0):
    pos = [Values.ValInt(val) for val in Mouse.pos]
    return Values.ValList(pos)

def gl_mouse_press_left(_stroke: int = 0):
    return Values.ValBool(events.get('left_press'))

def gl_mouse_press_right(_stroke: int = 0):
    return Values.ValBool(events.get('right_press'))

def gl_mouse_click_left(_stroke: int = 0):
    return Values.ValBool(events.get('left_click'))

def gl_mouse_click_right(_stroke: int = 0):
    return Values.ValBool(events.get('right_click'))

def gl_draw_circle(_pos: Values.ValList, _radis: Values.ValInt | Values.ValFloat, _color: Values.ValList | Values.ValStr,_stroke: int = 0):
    pos = [val.get_value() for val in _pos.get_value()]
    if isinstance(_color, Values.ValList):
        color = [val.get_value() for val in _color.get_value()]
    else:
        color = _color.get_value()
    Draw.draw_circle(window.surf, pos, _radis.get_value(), color)

def gl_math_distance(_pos1, _pos2, _stroke: int = 0):
    if test_type(_pos1, 'list', 'distance', _stroke) and test_type(_pos2, 'list', 'distance', _stroke):
        return Values.ValFloat(distance([val.get_value() for val in _pos1.get_value()], [val.get_value() for val in _pos2.get_value()]))

