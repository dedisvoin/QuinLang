from source.TokenizeFunct import (
    Tokenize, 
    Lexems
)
from source.ParserFunct import Parser

class Interpretator:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.tokenizor = Tokenize(file_name)
        self.parser = Parser()
        self.parser.set_tokens_map(self.tokenizor.tokens)
    

    def view_tokens_map(cls):
        cls.tokenizor.out_tokens()
        return cls

    def run(cls):
        cls.tokenizor.tokenize()
        cls.parser.parse()
        return cls


interpretator = (
    Interpretator('test.qn')
    .run()
    .view_tokens_map()
)