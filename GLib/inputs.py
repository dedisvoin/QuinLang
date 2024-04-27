from GLib.special_methods import *
import keyboard
import pygame
from GLib.window import *
import typing

EventId: typing.TypeAlias = str


class Mouse:
    bt_left = 'bt_left'
    bt_right = 'bt_right'
    bt_middle = 'bt_middle'
    
    press_event = 'press_event'
    click_event = 'click_event'
    
    def __init__(self, button: str, event_type: str, id = None) -> None:
        self.__button = button
        self.__event_type = event_type
        self.__id = generate_id(self, id)
        print(self.__id)
        
        self.__pressed = False
        
    def compare_id(self, id):
        return compare_id_and_number(self.__id, id)
    
    def id_type(self):
        return get_type_from_id(self.__id)
    
    def press(self, button: str = bt_left):
        if button == Mouse.bt_left:
            return pygame.mouse.get_pressed()[0]
        if button == Mouse.bt_middle:
            return pygame.mouse.get_pressed()[1]
        if button == Mouse.bt_right:
            return pygame.mouse.get_pressed()[2]

    def click(self, button: str = bt_left):
        p = self.press(button)
        if p:
            if not self.__pressed:
                self.__pressed = True
                return True
            else:
                return False
        if not self.press(button):
            self.__pressed = False
            return False
        
    @classmethod
    @property
    def pos(self) -> list[int, int]:
        return [*pygame.mouse.get_pos()]
    
    @classmethod
    @property
    def speed(self) -> list[int, int]:
        return pygame.mouse.get_rel()
    
    @classmethod
    def set_hide(self):
        pygame.mouse.set_visible(False)

    @classmethod
    def set_show(self):
        pygame.mouse.set_visible(True)
        
    @property
    def event_type(self):
        return self.__event_type
    
    @property
    def button(self):
        return self.__button
    
    @property
    def id(self):
        return self.__id
    
    @classmethod
    @property
    def whell(self):
        return Window.whell
        
    
class Keyboard:
    press_event = 'press_event'
    click_event = 'click_event'
    
    def __init__(self, key: str = '0', event_type: str = press_event, id = None) -> None:
        self.__id = generate_id(self, id)
        self.__key = key
        self.__event_type = event_type
        
        self.__pressed = False
        
        print(self.__id, f'{self.__key=}')
        
    def is_pressed(self, key: str):
        return keyboard.is_pressed(key)
    
    def compare_id(self, id):
        return compare_id_and_number(self.__id, id)
    
    def id_type(self):
        return get_type_from_id(self.__id)
        
    def click(self):
        p = keyboard.is_pressed(self.__key)
        if p:
            if not self.__pressed:
                self.__pressed = True
                return True
            else:
                return False
        if not self.is_pressed(self.__key):
            self.__pressed = False
            return False
        
    def press(self):
        return self.is_pressed(self.__key)
    
    @property
    def event_type(self):
        return self.__event_type
    
    @property
    def key(self):
        return self.__key
    
    @property
    def id(self):
        return self.__id


class Events:
    def __init__(self) -> None:
        self.__all_events = []
        self.__events_outputs = []
        
    def add(self, event_any: Mouse | Keyboard):
        if type(event_any) == list:
            self.__all_events+=event_any
        else:
            self.__all_events.append(event_any)

    def add_key_event(cls, key: str, id: EventId, event_type):
        cls.__all_events.append(Keyboard(key, event_type, id))
        return cls

    def add_mouse_event(cls, button: str, id: EventId, event_type):
        cls.__all_events.append(Mouse(button, event_type, id))
        return cls
        
    def get(self, id: str | int) -> bool:
        for event in self.__events_outputs: 
            if compare_id_and_number(event[1], id):
                return event[0]
            
    def update(self):
        self.__events_outputs = []
        for event in self.__all_events:
            
            if event.id_type() == Mouse.__name__:
                if event.event_type == Mouse.click_event:
                    self.__events_outputs.append([event.click(event.button), event.id])
                if event.event_type == Mouse.press_event:
                    self.__events_outputs.append([event.press(event.button), event.id])

            if event.id_type() == Keyboard.__name__:
                if pygame.mouse.get_focused():
                    if event.event_type == Keyboard.click_event:
                        self.__events_outputs.append([event.click(), event.id])
                    if event.event_type == Keyboard.press_event:
                        self.__events_outputs.append([event.press(), event.id])
                else:
                    if event.event_type == Keyboard.click_event:
                        self.__events_outputs.append([False, event.id])
                    if event.event_type == Keyboard.press_event:
                        self.__events_outputs.append([False, event.id])

    def get_all(self) -> dict[EventId, bool]:
        events_dict = {}
        for event in self.__events_outputs:
            id = get_number_from_id( event[1] )
            events_dict[ id ] = event[0]

        return events_dict