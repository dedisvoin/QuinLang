from src.ml_tokenizer import tokenizer_api
from src.ml_parser import parser_api
from src.ml_parser import variables

class Compiler:
    def __init__(self, _file_name: str, _debug: bool = False) -> None:
        self.T = tokenizer_api.Tokenizer(_file_name, _debug)
        self.E = parser_api.Executer()
        
    def compile(self):
        self.T.run()
        self.E.send_tokens(self.T.get_tokens())
    
    def execute(self):
        self.E.parse()
        self.E.execute()

C = Compiler(r'test.cpp',1)

C.compile()
C.execute()


variables.Variables.out_variables()