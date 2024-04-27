import json
from colorama import Fore
from src.ml_tokenizer.tokens import *


def save_tokens(_tokens: list[Token], _file_name: str) -> None:
    file = open(_file_name, 'w')
    write_data = []
    for token in _tokens:
        write_data.append([token.get_type(), token.get_data(), token.get_line()])
    json.dump(write_data, file)

    print(f'tokens file [{Fore.YELLOW}{_file_name}{Fore.RESET}] created ')
    print(f'[{Fore.YELLOW}{len(write_data)}{Fore.RESET}] tokens saved')

def load_tokens(_file_name: str) -> list[Token]:
    file = open(_file_name, 'r')

    tokens = []
    datas = json.load(file)

    for data in datas:
        tokens.append(Token(data[0], data[2], data[1]))

    return tokens
    
