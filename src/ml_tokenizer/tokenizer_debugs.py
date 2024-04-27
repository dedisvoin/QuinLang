from copy import copy
from colorama import (
    Fore, Back, Style
)
from src.ml_tokenizer.tokens import Token, Lexems, TokenTypes
from src.ml_tokenizer import keywords
import os

def out_cls():
    #os.system('cls')
    ...

def out_file(_data) -> None:
    max_len = len(str(len(_data)))
    print()
    print(Fore.YELLOW+'loaded file debug ----------------------------------------------------------'+Fore.RESET)
    print(f'{Fore.LIGHTBLUE_EX}line {Fore.YELLOW}| {Fore.LIGHTBLUE_EX}code{Fore.RESET}')

    for i, stroke in enumerate(out_pretty_file(_data)):
        print(f' [{Fore.MAGENTA}{i+1}{" "*(max_len-len(str(i+1)))}{Fore.RESET}]','', stroke.replace('\n',''))
    print(Fore.YELLOW+'loaded file debug ----------------------------------------------------------'+Fore.RESET)

def out_basic_tokens(_tokens: list[Token]):
    print()
    print(Fore.YELLOW+'basic tokens debug ---------------------------------------------------------'+Fore.RESET)

    tokens_in_line = {}
    for token in _tokens:
        if token.get_line()+1 not in tokens_in_line:
            tokens_in_line[token.get_line()+1] = [token]
        else:
            tokens_in_line[token.get_line()+1].append(token)
    print(f'{Fore.LIGHTBLUE_EX}line {Fore.YELLOW}| {Fore.LIGHTBLUE_EX}tokens{Fore.RESET}')
    if len(tokens_in_line)>0:
        max_len = len(str(list(tokens_in_line.keys())[-1]))
        
        for line in tokens_in_line:
            print(f' [{Fore.MAGENTA}{line}{" "*(max_len-len(str(line)))}{Fore.RESET}]', end = '  ')
            line_tokens = tokens_in_line[line]
            for i, token in enumerate(line_tokens):

                print(f'{Style.BRIGHT}{Fore.MAGENTA}{token.get_type()}{Fore.RESET}{Style.RESET_ALL}[{Fore.GREEN}{token.get_data()}{Fore.RESET}]', end=' ')
                if i!=len(line_tokens)-1:
                    #print(Fore.YELLOW+'|'+Fore.RESET, end = ' ')
                    ...
            print()

    print(Fore.YELLOW+'basic tokens debug ---------------------------------------------------------'+Fore.RESET)

def out_tokens(_tokens: list[Token]):
    print()
    print(Fore.YELLOW+'tokens debug ---------------------------------------------------------------'+Fore.RESET)

    tokens_in_line = {}
    for token in _tokens:
        if token.get_line()+1 not in tokens_in_line:
            tokens_in_line[token.get_line()+1] = [token]
        else:
            tokens_in_line[token.get_line()+1].append(token)

    print(f'{Fore.LIGHTBLUE_EX}line {Fore.YELLOW}| {Fore.LIGHTBLUE_EX}tokens{Fore.RESET}')
    if len(tokens_in_line)>0:
        max_len = len(str(list(tokens_in_line.keys())[-1]))
        
        for line in tokens_in_line:
            print(f' [{Fore.MAGENTA}{line}{" "*(max_len-len(str(line)))}{Fore.RESET}]', end = '  ')
            line_tokens = tokens_in_line[line]
            for i, token in enumerate(line_tokens):
                if token.get_type() not in TokenTypes.__dict__:
                    print(f'{Style.BRIGHT}{Fore.MAGENTA}{token.get_type()}{Fore.RESET}{Style.RESET_ALL}[{Fore.GREEN}{token.get_data()}{Fore.RESET}]', end=' ')
                else:
                    print(f'{Style.BRIGHT}{Fore.YELLOW}{token.get_type()}{Fore.RESET}{Style.RESET_ALL}', end=' ')
                if i!=len(line_tokens)-1:
                    #print(Fore.YELLOW+'|'+Fore.RESET, end = ' ')
                    ...
            print()

    print(Fore.YELLOW+'tokens debug ---------------------------------------------------------------'+Fore.RESET)

def out_tokenize_time(_start_time: float, _end_time: float):
    print(f'tokenize time [{Fore.BLUE}{round(_end_time-_start_time,4)}s{Fore.RESET}]')

def out_pretty_file(_data):
    pretty_strokes = []

    for stroke in _data:
        p_s = parse_stroke(stroke)
        pretty_strokes.append(p_s)
    return pretty_strokes

def parse_stroke(stroke):
    pos = 0
    p_s = ''
    at_word = ''
    stroke+=' '

    while pos<len(stroke):
        
        if stroke[pos] in Lexems.alphabet:
            at_word = ''

            while True:
                at_word += stroke[pos]
                
                pos+=1
                

                if stroke[pos] not in Lexems.alphabet and stroke[pos] != '_':
                    if stroke[pos] in Lexems.numbers:
                        if len(at_word)>0:
                            ...
                        else:
                            break
                    else:
                        break  

            if at_word in keywords.keywords:
                p_s+=Fore.MAGENTA+at_word+Fore.RESET
            elif at_word in keywords.keywords_types:
                p_s+=Style.BRIGHT+Fore.LIGHTYELLOW_EX+at_word+Fore.RESET+Style.RESET_ALL
            elif at_word in keywords.keywords_functs:
                p_s+=Fore.CYAN+at_word+Fore.RESET
            else:
                p_s+=Fore.BLUE+at_word+Fore.RESET
        
        elif stroke[pos] in Lexems.numbers:
            at_word = ''

            while True:
                at_word += stroke[pos]
                
                pos+=1
                if stroke[pos] not in Lexems.numbers and stroke[pos] != '.':
                    break  

            
            p_s+=Fore.WHITE+at_word+Fore.RESET
            
        elif stroke[pos] in Lexems.symvols or stroke[pos] in Lexems.brackets:

            at_word = ''
            at_word+=stroke[pos]

            while True:
                pos+=1
                if stroke[pos] not in Lexems.symvols and stroke[pos] not in Lexems.brackets:
                    break  
                at_word += stroke[pos]
                
                
                
            
            
            p_s+=Style.BRIGHT+Fore.GREEN+at_word+Fore.RESET+Style.RESET_ALL
                     
        elif stroke[pos] in "'":

            at_word = ''

            while True:
                
                at_word += stroke[pos]
                pos+=1
                
                if stroke[pos] == "'":
                    break  

            
            p_s+=Fore.GREEN+at_word+"'"+Fore.RESET
            pos+=1
        
        else:
            p_s+=stroke[pos]
            pos+=1
        
    return p_s