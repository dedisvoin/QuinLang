from colorama import Fore
from source.TokenTypes import TokenTypes

"""
This class defines various character sets used for tokenizing text, including the alphabet (both lowercase and uppercase), numbers, symbols, parentheses/brackets, and special characters like the single quote and newline.
"""
class Lexems:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'+'abcdefghijklmnopqrstuvwxyz'.upper()
    numbers = '1234567890'
    syms = '-%+*/:;,='
    scobs = '()[]{}'
    text = "'"
    new_line = '\n'
    

"""
This class represents a token, which is a fundamental unit of text in a programming language. Each token has a type, which indicates what kind of language construct it represents (e.g. a word, a number, a symbol, etc.), and the text of the token itself.
"""
class Token:
    def __init__(self, type, text) -> None:
        self.type = type
        self.text = text

"""
The `Tokenize` class is responsible for tokenizing the contents of a text file. It reads the file, splits it into tokens, and provides methods to access and output the tokenized data.

The class has the following main methods:

- `tokenize()`: Performs the tokenization process, splitting the file contents into individual tokens.
- `out_tokens()`: Prints the tokenized data in a formatted way, displaying the token type and text.
- `out_base_tokens()`: Prints the base tokens, which are the initial tokens extracted from the file contents.

The tokenization process involves identifying different types of tokens, such as words, symbols, numbers, and text. The class maintains a list of base tokens and a list of processed tokens, which can be accessed and manipulated as needed.
"""
class Tokenize:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.file = open(file_name, 'r', encoding='utf-8')
        self.data = self.file.readlines()
        self.code = ''.join(self.data)
        self.pos = 0
        self.at_sym = ''
        self.base_tokens = []
        self.tokens = []

    def code_len(self):
        return len(self.code)

    def get_sym(self, sum_pos = 0):
        return self.code[self.pos+sum_pos]
    
    def continue_sym(self):
        self.pos += 1

    def remove_sym(self):
        self.pos -= 1

    def out_code(self):
        print(self.code)

    def out_tokens(self):
        print('-'*50)
        for token in self.tokens:
            if token.type == TokenTypes.NEW_LINE:
                print()
            else:
                print(f'{token.type}[{Fore.MAGENTA}{token.text}{Fore.RESET}]', end=' ')
        print()
        print('-'*50)

    def out_base_tokens(self):
        print('-'*50)
        for token in self.base_tokens:
            if token.type == TokenTypes.NEW_LINE:
                print()
            else:
                print(f'{token.type}[{Fore.MAGENTA}{token.text}{Fore.RESET}]', end=' ')
        print()
        print('-'*50)

    """
    Tokenizes a word from the input code. Extracts the characters that make up a word, including letters and numbers, and adds a new `Token` object with the `WORD` type and the extracted text to the `base_tokens` list.
    """
    def tokenize_word(self):
            text = ''
            text+=self.at_sym
            while True:
                self.continue_sym()
                try:
                    self.at_sym = self.get_sym()
                    if self.at_sym not in Lexems.alphabet and self.at_sym not in Lexems.numbers:
                        break
                    text+=self.at_sym
                except: break

            self.base_tokens.append(Token(TokenTypes.WORD, text))

    """
    Tokenizes a sequence of symbols from the input code. Extracts the characters that make up a sequence of symbols and adds a new `Token` object with the `SYM` type and the extracted text to the `base_tokens` list.
    """
    def tokenize_syms(self):
            text = ''
            text+=self.at_sym
            while True:
                self.continue_sym()
                try:
                    self.at_sym = self.get_sym()
                    if self.at_sym not in Lexems.syms:
                        break
                    text+=self.at_sym
                except: break

            self.base_tokens.append(Token(TokenTypes.SYM, text))

    """
    Tokenizes a sequence of numbers from the input code. Extracts the characters that make up a sequence of numbers and adds a new `Token` object with the `NUMBER` type and the extracted text to the `base_tokens` list.
    """
    def tokenize_nums(self):
            text = ''
            text+=self.at_sym
            while True:
                self.continue_sym()
                try:
                    self.at_sym = self.get_sym()
                    if self.at_sym not in Lexems.numbers:
                        break
                    text+=self.at_sym
                except: break

            self.base_tokens.append(Token(TokenTypes.NUMBER, text))

    """
    Tokenizes a sequence of text characters from the input code. Extracts the characters that make up a sequence of text and adds a new `Token` object with the `TEXT` type and the extracted text to the `base_tokens` list.
    """
    def tokenize_text(self):
            text = ''
            while True:
                self.continue_sym()
                try:
                    self.at_sym = self.get_sym()
                    if self.at_sym == Lexems.text:
                        break
                    text+=self.at_sym
                except: break

            self.base_tokens.append(Token(TokenTypes.TEXT, text))

    """
    Tokenizes a sequence of scope brackets (e.g. '(', ')', '[', ']', '{', '}') from the input code. Extracts the scope bracket character and adds a new `Token` object with the `SYM` type and the extracted text to the `base_tokens` list.
    """
    def tokenize_scobs(self):
            self.base_tokens.append(Token(TokenTypes.SYM, self.at_sym))

    """
    Tokenizes the input code by iterating through the characters and identifying different types of tokens, such as words, symbols, numbers, and scope brackets. Adds the identified tokens to the `base_tokens` list.
    """
    def tokenize_base(self):
        while self.pos<self.code_len():
            self.at_sym = self.get_sym()        

            if self.at_sym in Lexems.alphabet:
                self.tokenize_word()
                self.remove_sym()
            elif self.at_sym in Lexems.syms:
                self.tokenize_syms()
                self.remove_sym()
            elif self.at_sym in Lexems.numbers:
                self.tokenize_nums()
                self.remove_sym()
            elif self.at_sym in Lexems.text:
                self.tokenize_text()
            #elif self.at_sym in Lexems.equal:
            #    self.base_tokens.append(Token(TokenTypes.SYM,Lexems.equal)) 
            #elif self.at_sym in Lexems.new_line:
            #    self.base_tokens.append(Token(TokenTypes.NEW_LINE,'\\n'))
            elif self.at_sym in Lexems.scobs:
                self.tokenize_scobs()
            
            self.continue_sym()

    def add_token(self, type, text):
        self.tokens.append(Token(type, text))

    """
    Tokenizes the input code by iterating through the characters and identifying different types of tokens, such as words, symbols, numbers, and scope brackets. Adds the identified tokens to the `tokens` list.
        
    This function processes the base tokens generated by `tokenize_base()` and creates more specific token types, such as `FUNCTION`, `SCOB_L`, `SCOB_R`, etc. It handles various token types and maps them to the appropriate token types.
    """
    def tokenize(self):
        self.tokenize_base()
        for base_token in self.base_tokens:

            if base_token.type == TokenTypes.NEW_LINE:
                self.add_token(TokenTypes.NEW_LINE, '\\n')


            if base_token.type == TokenTypes.WORD:
                if base_token.text == 'fn':
                    self.add_token(TokenTypes.FUNCTION, 'fn')
                elif base_token.text == 'or':
                    self.add_token(TokenTypes.OR, 'or')
                else:
                    self.add_token(TokenTypes.WORD, base_token.text)


            if base_token.type == TokenTypes.SYM:
                if base_token.text == '(':
                    self.add_token(TokenTypes.SCOB_L, '(')

                if base_token.text == ')':
                    self.add_token(TokenTypes.SCOB_R, ')')

                if base_token.text == '[':
                    self.add_token(TokenTypes.KVSCOB_L, '[')

                if base_token.text == ']':
                    self.add_token(TokenTypes.KVSCOB_R, ']')

                if base_token.text == '{':
                    self.add_token(TokenTypes.BL_SCOB_L, '{')

                if base_token.text == '}':
                    self.add_token(TokenTypes.BL_SCOB_R, '}')

                if base_token.text == '+':
                    self.add_token(TokenTypes.PLUS, '+')

                if base_token.text == '-':
                    self.add_token(TokenTypes.MINUS, '-')

                if base_token.text == '/':
                    self.add_token(TokenTypes.DELENIE, '/')

                if base_token.text == '*':
                    self.add_token(TokenTypes.UMNATHENIE, '*')

                if base_token.text == '%':
                    self.add_token(TokenTypes.PROCENT, '%')

                if base_token.text == ',':
                    self.add_token(TokenTypes.ZAPYT, ',')

                if base_token.text == '=':
                    self.add_token(TokenTypes.EQUAL, '=')

                if base_token.text == '||':
                    self.add_token(TokenTypes.OR, 'or')
                    
            
            if base_token.type == TokenTypes.NUMBER:
                self.add_token(TokenTypes.NUMBER, base_token.text)


            if base_token.type == TokenTypes.TEXT:
                self.add_token(TokenTypes.TEXT, base_token.text)

        self.add_token(TokenTypes.EOF, 'EOF')

if __name__ == '__main__':
    tokenize = Tokenize('test.txt')

    tokenize.tokenize()
    tokenize.out_tokens()
