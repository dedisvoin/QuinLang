from time import sleep, time
from typing import Any

from colorama import Fore, Style
from src.ml_tokenizer import tokenizer_debugs
from src.ml_tokenizer.tokens import (
    Token, TokenTypes, Lexems
)
from src.ml_tokenizer.tokens_files_manager import (save_tokens, load_tokens)
from src.ml_parser.errors import set_file
from tqdm import tqdm


def open_code_file(_file_name: str) -> list[str]:
    file = open(_file_name, 'r', encoding='UTF-8')
    data = file.readlines()
    return data

def open_tokens_file(_file_name: str) -> list[Token]:
    tokens = load_tokens(_file_name)
    return tokens

def convert_tokens_to_code(_tokens: list[Token]) -> list[str]:
    code = []
    
    sorted_tokens = {}
    for token in _tokens:
        if token.get_line() not in sorted_tokens:
            sorted_tokens[token.get_line()] = [token]
        else:
            sorted_tokens[token.get_line()].append(token)

    for key in sorted_tokens:
        s = ''
        for token in sorted_tokens[key]:
            if token.get_type() == TokenTypes.Basic.TEXT:
                s += "'"+str(token.get_data())+"'"+' '
            else:
                s += str(token.get_data())+' '
        code.append(s)

    return code

        

class Lexer:
    def __init__(self, _data: list[str], _debug) -> 'Lexer':
        self.__data = _data
        self.__pos = 0
        self.__stroke = 0
        self.__basic_tokens = []
        self.__tokens = []
        self.__debug = _debug
        self.normalize_data()


    @property
    def basic_tokens(self) -> list[Token]:
        return self.__basic_tokens
    
    def normalize_data(self):
        self.__data = [stroke.replace('|', ' | ') for stroke in self.__data]
        self.__data = [stroke.replace(',', ' , ') for stroke in self.__data]

    @property
    def tokens(self) -> list[Token]:
        return self.__tokens
    

    def get_tokens(self) -> list[Token]:
        return self.__tokens


    def next_pos(self):
        self.__pos += 1


    def next_stroke(self):
        self.__stroke += 1


    def begin_pos(self):
        self.__pos -= 1


    @property
    def pos(self) -> int:
        return self.__pos
    

    @property
    def stroke(self) -> int:
        return self.__stroke
    

    def get_symvol(self, i=0) -> str:
        return self.__data[self.__stroke][self.__pos+i]
    

    def get_lines_count(self) -> int:
        return len(self.__data)
    

    def get_syms_count(self) -> int:
        return len(self.__data[self.__stroke])
    

    def pos_reinit(self) -> None:
        self.__pos = 0


    def generate_base_tokens(self):
        while self.stroke < self.get_lines_count():
            self.pos_reinit()
            while self.pos < self.get_syms_count():
                self.create()
                self.next_pos()
            self.next_stroke()
    

    def generate_tokens(self):
        
        for token in tqdm(self.basic_tokens, desc=f'{Style.BRIGHT}{Fore.YELLOW}Tokenization process{Fore.RESET}',smoothing=0.3, colour='yellow') if self.__debug else self.basic_tokens:

            if token.get_type() == TokenTypes.Basic.WORD:
                if token.get_data() == 'fn':
                    self.add_token(TokenTypes.FN, token.get_line(), token.get_data())
                elif token.get_data() == 'for':
                    self.add_token(TokenTypes.FOR, token.get_line(), token.get_data())
                elif token.get_data() == 'let':
                    self.add_token(TokenTypes.LET, token.get_line(), token.get_data())
                elif token.get_data() == 'const':
                    self.add_token(TokenTypes.CONST, token.get_line(), token.get_data())
                elif token.get_data() == 'if':
                    self.add_token(TokenTypes.IF, token.get_line(), token.get_data())
                elif token.get_data() == 'else':
                    self.add_token(TokenTypes.ELSE, token.get_line(), token.get_data())
                elif token.get_data() == 'true':
                    self.add_token(TokenTypes.TRUE, token.get_line(), token.get_data())
                elif token.get_data() == 'false':
                    self.add_token(TokenTypes.FALSE, token.get_line(), token.get_data())
                elif token.get_data() == 'break':
                    self.add_token(TokenTypes.BREAK, token.get_line(), token.get_data())
                elif token.get_data() == 'continue':
                    self.add_token(TokenTypes.CONTINUE, token.get_line(), token.get_data())
                elif token.get_data() == 'forin':
                    self.add_token(TokenTypes.FORIN, token.get_line(), token.get_data())
                elif token.get_data() == 'while':
                    self.add_token(TokenTypes.WHILE, token.get_line(), token.get_data())
                elif token.get_data() == 'return':
                    self.add_token(TokenTypes.RETURN, token.get_line(), token.get_data())
                elif token.get_data() == 'match':
                    self.add_token(TokenTypes.MATCH, token.get_line(), token.get_data())
                elif token.get_data() == 'case':
                    self.add_token(TokenTypes.CASE, token.get_line(), token.get_data())
                elif token.get_data() == 'lambda':
                    self.add_token(TokenTypes.LAMBDA, token.get_line(), token.get_data())
                elif token.get_data() == 'using':
                    self.add_token(TokenTypes.USING, token.get_line(), token.get_data())
                elif token.get_data() == 'struct':
                    self.add_token(TokenTypes.STRUCT, token.get_line(), token.get_data())
                elif token.get_data() == 'new':
                    self.add_token(TokenTypes.NEW, token.get_line(), token.get_data())
                else:
                    self.add_token(TokenTypes.Basic.WORD, token.get_line(), token.get_data())

            if token.get_type() == TokenTypes.Basic.SYMVOL:
                if token.get_data() == '==':
                    self.add_token(TokenTypes.DOUBLE_EQUAL, token.get_line(), token.get_data())
                if token.get_data() == '||':
                    self.add_token(TokenTypes.OR, token.get_line(), token.get_data())
                if token.get_data() == '|':
                    self.add_token(TokenTypes.STOP_LINE, token.get_line(), token.get_data())
                if token.get_data() == '&&':
                    self.add_token(TokenTypes.AND, token.get_line(), token.get_data())
                if token.get_data() == '<':
                    self.add_token(TokenTypes.LESS, token.get_line(), token.get_data())
                if token.get_data() == '>':
                    self.add_token(TokenTypes.BIGGER, token.get_line(), token.get_data())
                if token.get_data() == '<=':
                    self.add_token(TokenTypes.EQUAL_LESS, token.get_line(), token.get_data())
                if token.get_data() == '>=':
                    self.add_token(TokenTypes.EQUAL_BIGGER, token.get_line(), token.get_data())
                if token.get_data() == '=':
                    self.add_token(TokenTypes.EQUAL, token.get_line(), token.get_data())
                if token.get_data() == '<>':
                    self.add_token(TokenTypes.NOT_EQUAL, token.get_line(), token.get_data())
                if token.get_data() == '+':
                    self.add_token(TokenTypes.PLUS, token.get_line(), token.get_data())
                if token.get_data() == '++':
                    self.add_token(TokenTypes.DOUBLE_PLUS, token.get_line(), token.get_data())
                if token.get_data() == '-':
                    self.add_token(TokenTypes.MINUS, token.get_line(), token.get_data())
                if token.get_data() == '--':
                    self.add_token(TokenTypes.DOUBLE_MINUS, token.get_line(), token.get_data())
                if token.get_data() == '*':
                    self.add_token(TokenTypes.MULTIPLICATION, token.get_line(), token.get_data())
                if token.get_data() == '%':
                    self.add_token(TokenTypes.PERCENT, token.get_line(), token.get_data())
                if token.get_data() == '/':
                    self.add_token(TokenTypes.DIVISION, token.get_line(), token.get_data())
                if token.get_data() == ':':
                    self.add_token(TokenTypes.DOUBLE_DOT, token.get_line(), token.get_data())
                if token.get_data() == '..':
                    self.add_token(TokenTypes.DOT_AND_DOT, token.get_line(), token.get_data())
                if token.get_data() == ';':
                    self.add_token(TokenTypes.DOT_AND_COMMA, token.get_line(), token.get_data())
                if token.get_data() == '(':
                    self.add_token(TokenTypes.LEFT_BRACK, token.get_line(), token.get_data())
                if token.get_data() == ')':
                    self.add_token(TokenTypes.RIGHT_BRACK, token.get_line(), token.get_data())
                if token.get_data() == '{':
                    self.add_token(TokenTypes.LEFT_CURLY_BRACK, token.get_line(), token.get_data())
                if token.get_data() == '}':
                    self.add_token(TokenTypes.RIGHT_CURLY_BRACK, token.get_line(), token.get_data())
                if token.get_data() == '[':
                    self.add_token(TokenTypes.LEFT_RECT_BRACK, token.get_line(), token.get_data())
                if token.get_data() == ']':
                    self.add_token(TokenTypes.RIGHT_RECT_BRACK, token.get_line(), token.get_data())
                if token.get_data() == '->':
                    self.add_token(TokenTypes.STRELA_RIGHT, token.get_line(), token.get_data())
                if token.get_data() == '<-':
                    self.add_token(TokenTypes.STRELA_LEFT, token.get_line(), token.get_data())
                if token.get_data() == ',':
                    self.add_token(TokenTypes.COMMA, token.get_line(), token.get_data())
                if token.get_data() == '.':
                    self.add_token(TokenTypes.DOT, token.get_line(), token.get_data())
                if token.get_data() == '~':
                    self.add_token(TokenTypes.SNAKE, token.get_line(), token.get_data())
                if token.get_data() == '_':
                    self.add_token(TokenTypes.THUNDER, token.get_line(), token.get_data())
                if token.get_data() == '!':
                    self.add_token(TokenTypes.VOSCL, token.get_line(), token.get_data())
                if token.get_data() == '&':
                    self.add_token(TokenTypes.UKAZATEL, token.get_line(), token.get_data())
                if token.get_data() == ':->':
                    self.add_token(TokenTypes.STRELA_RIGHT_AND_DOTS, token.get_line(), token.get_data())
            if token.get_type() == TokenTypes.Basic.NUMBER:
                self.add_token(TokenTypes.Basic.NUMBER, token.get_line(), token.get_data())
            if token.get_type() == TokenTypes.Basic.TEXT:
                self.add_token(TokenTypes.Basic.TEXT, token.get_line(), token.get_data())

        try:
            self.add_token(TokenTypes.EOF, token.get_line(), 'EOF')
        except:
            self.add_token(TokenTypes.EOF, 1, 'EOF')

    def run(self) -> None:
        self.generate_base_tokens()
        self.generate_tokens()
    
    def save_tokens(self) -> None:
        save_tokens(self.tokens, r'tokens.json')
        

    def add_token_basic(self, _type: TokenTypes, _line: int, _data: Any | None = None) -> Token:

        self.__basic_tokens.append(
            token := Token(_type, _line, _data)
        )
        return token


    def add_token(self, _type: TokenTypes, _line: int, _data: Any | None = None) -> Token:
        self.__tokens.append(
            token := Token(_type, _line, _data)
        )
        return token


    def create_base_word_token(self):
        data = ''
        while True:
            data += self.get_symvol()
            self.next_pos()
            
            if self.get_symvol() == '.':
                ...
            elif (self.get_symvol() not in Lexems.alphabet) and self.get_symvol() != '_':
                if self.get_symvol() in Lexems.numbers and len(data)>0:
                    ...
                else:
                    break
            else:
                ...
            
        
                
            
        self.add_token_basic(TokenTypes.Basic.WORD, self.stroke, data)


    def create_base_text_token(self):
        data = ''
        self.next_pos()
        while True:
            if self.get_symvol() == "'":
                break
            data += self.get_symvol()
            self.next_pos()
            
        self.add_token_basic(TokenTypes.Basic.TEXT, self.stroke, data)

    
    def create_base_number_token(self):
        data = ''
        while True:
            
            data += self.get_symvol()
            self.next_pos()

            if (self.get_symvol() not in Lexems.numbers) and self.get_symvol() != '.':
                break
            elif (self.get_symvol() not in Lexems.numbers) and self.get_symvol() == '.':
                if self.get_symvol(1) == '.':
                    break
                if self.get_symvol() == '.' and data.count('.')==1:
                    break
               
        self.add_token_basic(TokenTypes.Basic.NUMBER, self.stroke, data)
        

    def create_base_symvol_token(self):
        data = ''
        while True:
            data += self.get_symvol()
            self.next_pos()
            if (self.get_symvol() not in Lexems.symvols):
                break
        self.add_token_basic(TokenTypes.Basic.SYMVOL, self.stroke, data)
        self.begin_pos()


    def create_base_bracket_token(self):
        self.add_token_basic(TokenTypes.Basic.SYMVOL, self.stroke, self.get_symvol())


    def create(self):
        if self.get_symvol() in Lexems.alphabet:
            self.create_base_word_token()
        
        if self.get_symvol() in Lexems.numbers:
            self.create_base_number_token()
        if self.get_symvol() in Lexems.symvols:
            self.create_base_symvol_token()
        
        if self.get_symvol() in Lexems.brackets:
            self.create_base_bracket_token()
        if self.get_symvol() in "'":
            self.create_base_text_token()
        
            

class Tokenizer:
    def __init__(self, _file_name: str, _debug: bool = False, _fp: str = None) -> 'Tokenizer':
        
        self.__file_name = _file_name
        if self.__file_name!= 'None':
            self.__data = open_code_file(self.__file_name)
            self.__lexer = Lexer(self.__data, _debug)
            set_file(_file_name, self.__data)
        else:
            self.__data = _file_name
            self.__lexer = None
        self.__fp = _fp
        
        
        
        self.__debug = _debug


    def set_lexer(self, _lexer: Lexer) -> None:
        self.__lexer = _lexer

    def set_data(self, _data: str) -> None:
        self.__data = _data

    def get_data(self) -> list[str]:
        return self.__data
    
    def get_tokens(self) -> list[Token]:
        return self.__lexer.get_tokens()

    @classmethod
    def from_text(self, _text: list[str], _debug: bool = False) -> 'Tokenizer':
        T = Tokenizer('None', _debug)
        T.set_data(_text)
        T.set_lexer(Lexer(T.get_data(), False))
        return T
        
    

    def out_file(self) -> None:
        tokenizer_debugs.out_file(self.__data)


    def out_basic_tokens(self) -> None:
        tokenizer_debugs.out_basic_tokens(self.__lexer.basic_tokens)


    def out_tokens(self) -> None:
        tokenizer_debugs.out_tokens(self.__lexer.tokens)


    def out_cls(self) -> None:
        tokenizer_debugs.out_cls()

    def out_tokenize_time(self, _start_time, _end_time) -> None:
        tokenizer_debugs.out_tokenize_time(_start_time, _end_time)


    def run(self) -> None:
        self.out_cls()
        start_time = time()
        self.__lexer.run()
        end_time = time()
        
        
        if self.__debug:
            self.__lexer.save_tokens()
            self.out_tokenize_time(start_time, end_time)
            self.out_file()
            self.out_basic_tokens()
            self.out_tokens()

    

