from source.TokenTypes import (
    TokenTypes,
)
from source.TokenizeFunct import (
    Token,
)
from source.StatementsFunct import (
    Statements
)
from source.ExpressionFunct import *


"""
The `Parser` class is responsible for parsing a sequence of tokens and generating an abstract syntax tree (AST) representation of the parsed code. It provides methods for setting the token map, executing the parsed code, and parsing statements, expressions, and primary expressions.

The `parse` method is the main entry point, which iterates through the tokens and generates a list of statements that can be executed later using the `exec_code` method.

The `statement` method is responsible for parsing a single statement, which in this case is an assignment statement. The `expression` method parses an expression, which can be an additive expression, a multiplicative expression, or a primary expression.

The `match` and `basic_match` methods are helper methods used to match the current token against a specified token type and advance the token position if the match is successful.

The `get_token` and `get_tokens_count` methods are used to access the token map and retrieve the current token or the total number of tokens, respectively.
"""
class Parser:
    def __init__(self) -> None:
        self.tokens_map = []
        self.pos = 0
        self.result = []

        self.EOF = Token(TokenTypes.EOF, 'EOF')


    def set_tokens_map(self, tokens_map):
        self.tokens_map = tokens_map


    def exec_code(self):
        for stroke in self.result:
            stroke.exec()
        

    def parse(self):
        while not self.match(TokenTypes.EOF):
            state = self.statement()
            self.result.append(state)


    def statement(self):
        return self.asignet_state()


    def asignet_state(self):
        current_token = self.get_token()
        if current_token.type == TokenTypes.WORD:
            self.next_token()
            if self.match(TokenTypes.EQUAL):
                var_name = current_token.text
                var_value = self.expression()
                return Statements.Asignet(var_name, var_value)  


    def expression(self):
        return self.additive()
    

    def additive(self):
        expr = self.multiplicative()

        while True:
            if self.match(TokenTypes.PLUS):
                expr = BinaryExp(expr, self.multiplicative(), '+')
                continue
            if self.match(TokenTypes.MINUS):
                expr = BinaryExp(expr, self.multiplicative(), '-')
                continue
            break
        return expr
    

    def multiplicative(self):
            expr = self.unary()

            while True:
                if self.match(TokenTypes.DELENIE):
                    expr = BinaryExp(expr, self.unary(), '/')
                    continue
                elif self.match(TokenTypes.UMNATHENIE):
                    expr = BinaryExp(expr, self.unary(), '*')
                    continue
                elif self.match(TokenTypes.PROCENT):
                    expr = BinaryExp(expr, self.unary(), '%')
                    continue
                break
            return expr
    
    
    def unary(self):
        if self.match(TokenTypes.MINUS):
            return UnaryExp( self.primary(), '-')
        if self.match(TokenTypes.PLUS):  
            return self.primary()
        return self.primary()
    

    def primary(self):
        current = self.get_token(0)  
        if self.match(TokenTypes.NUMBER):
            return NumberExp(int(current.text))
        if self.match(TokenTypes.WORD):
            return VariableExp(current.text)
        
        if self.match(TokenTypes.SCOB_L):
            expr = self.expression()
            self.match(TokenTypes.SCOB_R)
            return expr
        

    def match(self, token_type):
        if self.get_token().type != token_type: return False
        else:
            self.next_token()
            return True
        

    def basic_match(self, token_type):
        if self.get_token().type != token_type: return False
        self.next_token()
        return True
        

    def get_token(self, pos=0):
        pos = self.pos+pos
        if self.pos >= self.get_tokens_count()-1:
            return  self.EOF
        return self.tokens_map[pos]
        
        
    def get_tokens_count(self):
        return len(self.tokens_map)      

    def next_token(self):
        self.pos+=1

    

    