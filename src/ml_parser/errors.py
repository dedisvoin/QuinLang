from colorama import (
    Fore, Style, Back
)
import os
from src.ml_tokenizer.tokenizer_debugs import out_pretty_file
import time



compile_error = ' Compile error '
help_message = f'{Fore.CYAN}[ help ]{Fore.RESET}'
example_message = f'{Fore.BLACK}[ example ] ->{Fore.RESET}'

def get_time():
    t = time.localtime()
    return f'[{Fore.MAGENTA}{t.tm_hour}:{t.tm_min}:{t.tm_sec}{Fore.RESET}]'

class Errors:
    
    @classmethod
    def ERROR_ASIGNET_TYPE(self, _var_name: str, _type: str, _var_type: str, _stroke: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   Variable [{Fore.GREEN}{_var_name}{Fore.RESET}] wait {Fore.MAGENTA}<{_type}>{Fore.RESET}. You get {Fore.MAGENTA}<{_var_type}>{Fore.RESET} typed value.
    |   {help_message} Use the ({Fore.YELLOW}auto{Fore.RESET}) type hint so that the parser determines the type itself.
''')
        os._exit(-1)

    @classmethod
    def ERROR_VARIABLE_NOT_FOUND(self, _var_name: str, _stroke: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   Variable [{Fore.GREEN}{_var_name}{Fore.RESET}] not found.
    |   {help_message} Check if you wrote the variable name correctly.
''')
        os._exit(-1)

    @classmethod
    def ERROR_VARIABLE_NOT_CHAINGABLE(self, _var_name: str, _stroke: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   Variable [{Fore.GREEN}{_var_name}{Fore.RESET}] not chaingable.
    |   {help_message} Use the ({Fore.YELLOW}let{Fore.RESET}) keyword to make the variable chaingable.
''')
        os._exit(-1)

    @classmethod
    def ERROR_VARIABLE_TYPE(self, _var_name: str, _type: str, _var_type: str, _stroke: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   Variable [{Fore.GREEN}{_var_name}{Fore.RESET}] expects type {Fore.MAGENTA}<{_type}>{Fore.RESET} and you passed an argument of type {Fore.MAGENTA}<{_var_type}>{Fore.RESET}.
    |   {help_message} Try to convert the type of expression.
''')
        os._exit(-1)
    
    @classmethod
    def ERROR_VARIABLE_NAME_IS_NOT_SET(self, _type: str, _stroke: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   Variable {Fore.MAGENTA}<{_type}>{Fore.RESET} type, name is not set.
    |   {help_message} Enter the name of the variable between the type and the equals sign.
''')
        os._exit(-1)

    @classmethod
    def ERROR_BINARY_OPERATION(self, _type_1: str, _type_2: str, _operation: str, _stroke: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   Binary operation [{Fore.MAGENTA}{_operation}{Fore.RESET}] is not defined for types [{Fore.MAGENTA}{_type_1}{Fore.RESET}] and [{Fore.MAGENTA}{_type_2}{Fore.RESET}]
    |   {help_message} Try to convert the type of expression.
''')
        os._exit(-1)

    @classmethod
    def ERROR_CONVERT_TO_INT(self, _value: str, _stroke: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   Value [{Fore.MAGENTA}{_value}{Fore.RESET}] don't converted to {Fore.MAGENTA}<int>{Fore.RESET} type.
    |   {help_message} Try to replace [{Fore.MAGENTA}{_value}{Fore.RESET}] value to any {Fore.MAGENTA}<int>{Fore.RESET} or {Fore.MAGENTA}<float>{Fore.RESET} string value.
''')
        os._exit(-1)

    @classmethod
    def ERROR_CONVERT_TO_FLOAT(self, _value: str, _stroke: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   Value [{Fore.MAGENTA}{_value}{Fore.RESET}] don't converted to {Fore.MAGENTA}<float>{Fore.RESET} type.
    |   {help_message} Try to replace [{Fore.MAGENTA}{_value}{Fore.RESET}] value to any {Fore.MAGENTA}<int>{Fore.RESET} or {Fore.MAGENTA}<float>{Fore.RESET} string value.
''')
        os._exit(-1)

    @classmethod
    def ERROR_CONVERT_TO_BOOL(self, _value: str, _stroke: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   Value [{Fore.MAGENTA}{_value}{Fore.RESET}] don't converted to {Fore.MAGENTA}<bool>{Fore.RESET} type.
    |   {help_message} Try to replace [{Fore.MAGENTA}{_value}{Fore.RESET}] value to any {Fore.MAGENTA}<int>{Fore.RESET} or {Fore.MAGENTA}<str>{Fore.RESET} value.
''')
        os._exit(-1)

    @classmethod
    def ERROR_TYPE(self, _value: str, _stroke: int = 0, _expected_type: str = 'str'):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   Expected {Fore.MAGENTA}<{_expected_type}>{Fore.RESET} typed value, not {Fore.MAGENTA}<{_value}>{Fore.RESET}.
    |   {help_message} Use convert method [{Fore.YELLOW}str{Fore.RESET}] to fix.
''')
        os._exit(-1)

    @classmethod
    def ERROR_FORIN_WAIT_TYPE(self, _type: str, _stroke: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   The forin construct expects an iterable types [{Fore.MAGENTA}<str>{Fore.RESET} or {Fore.MAGENTA}<list>{Fore.RESET}], not {Fore.MAGENTA}<{_type}>{Fore.RESET}.
    |   {help_message} Use a different value in this field.''')
        pf = out_pretty_file(''' 
    let (auto) arr = [1,2,3]
    forin (arr -> val){
        print(val)
    }                       
'''.split('\n'))
        print(f'{example_message}')
        for string in pf:
            print(string)
        print(f'{example_message}')
        os._exit(-1)

    @classmethod
    def ERROR_LIST_INDEX_OUT(self, _index: int, _range:int, _stroke: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   List index [{Fore.MAGENTA}{_index}{Fore.RESET}] out of range [{Fore.MAGENTA}0-{_range-1}{Fore.RESET}].
''')
        os._exit(-1)

    @classmethod
    def ERROR_ARGUMENT_TYPE(self, _function_name: str, _arg_name: str, _wait_arg_type: str, _arg_type: str, _stroke: int = 0, _pos: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   Function [{Fore.GREEN}{_function_name}(){Fore.RESET}] in [{Fore.YELLOW}arg ({_arg_name}), pos ({_pos+1}){Fore.RESET}] waited {Fore.MAGENTA}<{_wait_arg_type}>{Fore.RESET} type argument. You taked {Fore.MAGENTA}<{_arg_type}>{Fore.RESET} argument type.
    |   {help_message} Try converting the types of arguments you are entering.
    ''')
        os._exit(-1)

    @classmethod
    def ERROR_OUT_ARGUMENT_TYPE(self, _function_name:str, _wait_arg_type: str, _arg_type: str, _stroke: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   By definition, a function [{Fore.GREEN}{_function_name}(){Fore.RESET}] must return an argument of type {Fore.MAGENTA}<{_wait_arg_type}>{Fore.RESET}, and it returns an argument of type {Fore.MAGENTA}<{_arg_type}>{Fore.RESET}.
    |   {help_message} Try changing the body of the function so that it returns an argument of the correct type.''')
        print(example_message)
        pf = out_pretty_file(f''' 
    fn ({_arg_type}) {_function_name}(arg1, arg2, ...)
        ...        
'''.split('\n'))
        for string in pf:
            print(string)
        print(example_message)
        os._exit(-1)

    @classmethod
    def ERROR_VOID_FUNCTION_NOT_BE_RETURN(self, _function_name: str, _arg_type: str, _stroke: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   The function [{Fore.GREEN}{_function_name}(){Fore.RESET}] cannot return an argument of type {Fore.MAGENTA}<{_arg_type}>{Fore.RESET} because the function is defined with type {Fore.MAGENTA}<void>{Fore.RESET}
    |   {help_message} Try changing the function type.''')

        os._exit(-1)

    @classmethod
    def ERROR_MATCH_WAIT_CASE(self, _stroke: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   The match construction waited at least one case.
    |   {help_message} Try adding additional cases.
    ''')
        os._exit(-1)
    
    @classmethod
    def ERROR_INVALID_MATCH_CONSTRUCTION(self, _stroke: int = 0):
        print(f'''{get_time()} -> [{Fore.RED}{compile_error}{Fore.RESET}] [{Fore.BLUE}line {_stroke+1}{Fore.RESET}]
    |   Invalid match construction.
    |   {help_message} Try adding additional cases.
    ''')
        print(example_message)
        pf = out_pretty_file(''' 
    match <expr> -> {
        case <expr> -> <state>
        case <expr> -> <state>   
        ...               
    }      
'''.split('\n'))
        for string in pf:
            print(string)
        print(example_message)
        os._exit(-1)
        os._exit(-1)