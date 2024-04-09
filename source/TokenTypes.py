"""
This class defines the various token types that can be identified in the tokenization process. These include basic types like WORD, NUMBER, SYM, TEXT, and NEW_LINE, as well as more specific types for common programming language constructs like PLUS, MINUS, RAVNO, EQUAL, UMNATHENIE, DELENIE, and various types of parentheses and brackets.
"""
class TokenTypes:
    WORD = 'WORD'
    NUMBER = 'NUMBER'
    SYM = 'SYM'
    TEXT = 'TEXT'
    NEW_LINE = 'NEW_LINE'

    PLUS = 'PLUS'
    MINUS = 'MINUS'
    RAVNO = 'RAVNO'
    EQUAL = 'EQUAl'
    UMNATHENIE = 'UMNATHENIE'
    DELENIE = 'DELENIE'
    PROCENT = 'PROCENT'

    SCOB_R = 'SCOB_R'
    SCOB_L = 'SCOB_L'
    KVSCOB_R = 'KVSCOB_R'
    KVSCOB_L = 'KVSCOB_L'
    BL_SCOB_R = 'BL_SCOB_R'
    BL_SCOB_L = 'BL_SCOB_L'

    ZAPYT = 'ZAPYT'

    FUNCTION = 'FUNCTION'

    OR = 'OR'

    EOF = 'EOF'