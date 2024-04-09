from source.TokenizeFunct import (
    Tokenize, 
    Lexems
)
from source.ParserFunct import Parser
from source.VariablesFunct import (
    Variables
)

class Interpretator:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.tokenizor = Tokenize(file_name)
        self.parser = Parser()
        self.parser.set_tokens_map(self.tokenizor.tokens)
    

    def view_tokens_map(cls):
        cls.tokenizor.out_tokens()
        return cls

    def run_tokenize(cls):
        cls.tokenizor.tokenize()
    
    def run_parse(cls):
        cls.parser.parse()
        cls.parser.exec_code()
        return cls


interpretator = Interpretator('test.qn')
interpretator.run_tokenize()
interpretator.view_tokens_map()
interpretator.run_parse()



Variables.print_vars()