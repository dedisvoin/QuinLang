from typing import Any




class TokenTypes:
    class Basic:
        WORD = 'WORD'
        NUMBER = 'NUMBER'
        SYMVOL = 'SYMVOL'
        TEXT = 'TEXT'


    EQUAL = 'EQUAL'

    DOUBLE_EQUAL = 'DOUBLE_EQUAL'
    NOT_EQUAL = 'NOT_EQUAL'


    PERCENT = 'PERCENT'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    DIVISION = 'DIVISION'
    MULTIPLICATION = 'MULTIPLICATION'


    LEFT_BRACK = 'LEFT_BRACK'
    RIGHT_BRACK = 'RIGHT_BRACK'
    LEFT_CURLY_BRACK = 'LEFT_CURLY_BRACK'
    RIGHT_CURLY_BRACK = 'RIGHT_CURLY_BRACK'
    LEFT_RECT_BRACK = 'LEFT_RECT_BRACK'
    RIGHT_RECT_BRACK = 'RIGHT_RECT_BRACK'


    COMMA = 'COMMA'
    DOT_AND_COMMA = 'DOT_AND_COMMA'
    DOUBLE_DOT = 'DOUBLE_DOT'

    BIGGER = 'BIGGER'
    LESS = 'LESS'
    EQUAL_BIGGER = 'EQUAL_BIGGER'
    EQUAL_LESS = 'EQUAL_LESS'

    DOUBLE_PLUS = 'DOUBLE_PLUS'
    DOUBLE_MINUS = 'DOUBLE_MINUS'

    TRUE = 'TRUE'
    FALSE = 'FALSE'

    LET = 'LET'
    CONST = 'CONST'
    VOID = 'VOID'
    FN = 'FN'
    FOR = 'FOR'
    FORIN = 'FORIN'
    ELSE = 'ELSE'
    IF = 'IF'

    EOF = 'EOF'

    OR = 'OR'
    AND = 'AND'
    BREAK = 'BREAK'
    CONTINUE = 'CONTINUE'
    RETURN = 'RETURN'
    WHILE = 'WHILE'

    STRELA_RIGHT = 'STRELA_RIGHT'
    STRELA_LEFT = 'STRELA_LEFT'

    SNAKE = 'SNAKE'

    DOT_AND_DOT = 'DOT_AND_DOT'

    MATCH = 'MATCH'
    CASE = 'CASE'

    THUNDER = 'THUNDER'
    LAMBDA = 'LAMBDA'

    VOSCL = 'VOSCL'
    
    USING = 'USING'

    STRUCT = 'STRUCT'
    NEW = 'NEW'
    DOT = 'DOT'
    STRELA_RIGHT_AND_DOTS = 'STRELA_RIGHT_AND_DOTS'

    STOP_LINE = 'STOP_LINE'

    UKAZATEL = '&'


class Lexems:
    numbers = '0123456789'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'+'abcdefghijklmnopqrstuvwxyz'.upper()
    symvols = ':,+-/*=<>%;&|~_!.'
    brackets = '()[]{}'
    

class Token:
    def __init__(self, _type: TokenTypes, _line: int, _data: Any | None = None) -> 'Token':
        self.__type = _type
        self.__data = _data
        self.__line = _line

    def get_type(self) -> TokenTypes:
        return self.__type
    
    def get_data(self) -> any:
        return self.__data
    
    def get_line(self) -> int:
        return self.__line
    
    def data_is_exist(self) -> bool:
        if self.__data is None: return False
        return True
    