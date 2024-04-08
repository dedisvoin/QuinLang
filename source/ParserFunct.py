from source.TokenTypes import TokenTypes
from source.StatementsFunct import (
    Statements
)

class Parser:
    def __init__(self) -> None:
        self.tokens_map = []
        self.pos = 0
        self.result = []

    def set_tokens_map(self, tokens_map):
        self.tokens_map = tokens_map
        
    def parse(self):
        while self.pos<self.get_tokens_count():
            state = self.statement()
            self.result.append(state)
            self.next_token()

    def asignet_state(self):
        current_token = self.get_token()
        if current_token.type == TokenTypes.WORD:
            self.next_token()
            if self.match(TokenTypes.EQUAL):
                var_name = current_token.text
                self.next_token()
                var_value = self.expression()
                return Statements.Asignet(var_name, var_value)
            
    def expression(self):
        return self.logical_or()
    
    def logical_or(self):
        logical_end_result = self.logical_and()
        while True:
            ...
            
    def statement(self):
        return self.asignet_state()

    def match(self, token_type):
        if self.get_token().type == token_type:
            self.next_token()
            return True
        else:
            raise Exception(f'Expected {token_type} but got {self.get_token().type}')

    def get_token(self, pos=0):
        return self.tokens_map[self.pos+pos]

    def get_tokens_count(self):
        return len(self.tokens_map)      

    def next_token(self):
        self.pos+=1

    

    