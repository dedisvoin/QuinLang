from colorama import (
    Fore, Style, Back
)
import os
from src.ml_tokenizer.tokenizer_debugs import out_pretty_file
import time



compile_error = ' Compile error '
call_error = ' Call error '

help_message = f'{Fore.CYAN}[ help ]{Fore.RESET}'
example_message = f'{Fore.BLACK}[ example ] ->{Fore.RESET}'

def test_type(value, type, fname, stroke):
    if isinstance(type, (list, tuple)):
        if value.get_type() in type:
            return True
        else:
            Errors.ERROR_FUNCT_TYPE(fname, type, value.get_type(), stroke)
    else:
        if value.get_type() == type:
            return True
        else:
            Errors.ERROR_FUNCT_TYPE(fname, type, value.get_type(), stroke)

def test_instance(value, instanse, stroke, fname):
    if isinstance(value, instanse):
        return True
    else:
        Errors.ERROR_FUNCT_TYPE(fname, instanse.__name__, value.get_type(), stroke)

file = 'not include'
code = []

def set_file(name, code_arr):
    global file, code
    file = name
    code = code_arr

def get_time():
    t = time.localtime()
    return f'[{Fore.MAGENTA}{t.tm_hour}:{t.tm_min}:{t.tm_sec}{Fore.RESET}]'

def debug(error_type, line, trace_back = 'undefined error'):
    return f'{get_time()} -> [{Fore.RED}{Style.BRIGHT}{error_type}{Fore.RESET}{Style.RESET_ALL}] [ {Fore.LIGHTYELLOW_EX}{Style.BRIGHT}{trace_back}{Fore.RESET}{Style.RESET_ALL} ] [ {Fore.BLUE}line {line+1}{Fore.RESET} ] [ {Fore.CYAN}{file}{Fore.RESET} ]'

def out_error_stroke(_stroke):
    s = code[_stroke].replace("\n"," ")
    ns = ' '*(len(str(_stroke))+3)
    print('    |   ')
    print(f"    |   [{Fore.YELLOW}{_stroke+1}{Fore.RESET}] {s}")
    print(f'    |   {ns}{Fore.RED}{"^"*(len(code[_stroke])-1)}{Fore.RESET}')

class Errors:
    @classmethod
    def ERROR_FUNCT_TYPE(self, _function_name, _wait_type, _type , _stroke):
        print(f'''{debug(call_error, _stroke, 'ERROR_FUNCT_TYPE')}
    |   Function [{Fore.GREEN}{_function_name}{Fore.RESET}] expected {Fore.MAGENTA}<{_wait_type}>{Fore.RESET} typed value, not {Fore.MAGENTA}<{_type}>{Fore.RESET} type.
    |   {help_message} Use convert method to fix.''')
        out_error_stroke(_stroke)
        os._exit(-1)
    
    @classmethod
    def ERROR_ASIGNET_TYPE(self, _var_name: str, _type: str, _var_type: str, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_ASIGNET_TYPE')}
    |   Variable [{Fore.GREEN}{_var_name}{Fore.RESET}] wait {Fore.MAGENTA}<{_type}>{Fore.RESET}. You get {Fore.MAGENTA}<{_var_type}>{Fore.RESET} typed value.
    |   {help_message} Use the ({Fore.YELLOW}auto{Fore.RESET}) type hint so that the parser determines the type itself.''')
        out_error_stroke(_stroke)
        os._exit(-1)

    @classmethod
    def ERROR_LAMBDA_ASIGNET_TYPE(self, _var_name: str, _type: str, _var_type: str, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_LAMBDA_ASIGNET_TYPE')}
    |   The variable [{Fore.GREEN}{_var_name}{Fore.RESET}] gets the object type being called {Fore.MAGENTA}<{_type}>{Fore.RESET}, the variable type {Fore.MAGENTA}<{_var_type}>{Fore.RESET} does not match the object type.
    |   {help_message} Use the ({Fore.YELLOW}auto{Fore.RESET} or {Fore.YELLOW}call{Fore.RESET}) type hint so that the parser determines the type itself.''')
        out_error_stroke(_stroke)
        os._exit(-1)

    @classmethod
    def ERROR_LAMBDA_ARGUMENT_COUNT(self, _count: str, _wait_count: str, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_LAMBDA_ARGUMENT_COUNT')}
    |   This lambda expression expects {Fore.CYAN}{_wait_count}{Fore.RESET} arguments, was passed {Fore.CYAN}{_count}{Fore.RESET} arguments.
    |   {help_message} Pass the required number of arguments.''')
        out_error_stroke(_stroke)
        os._exit(-1)

    @classmethod
    def ERROR_LAMBDA_ARGUMENT(self, _type, _waited_types, _pos, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_LAMBDA_ARGUMENT_COUNT')}
    |   This lambda expression expects {Fore.MAGENTA}<{_waited_types}>{Fore.RESET} typed arguments, was passed {Fore.MAGENTA}<{_type}>{Fore.RESET} type argument in pos {Fore.YELLOW}{_pos+1}{Fore.RESET}.
    |   {help_message} Pass the required number of arguments.''')
        out_error_stroke(_stroke)
        os._exit(-1)

    @classmethod
    def ERROR_VARIABLE_NOT_FOUND(self, _var_name: str, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_VARIABLE_NOT_FOUND')}
    |   Variable [{Fore.GREEN}{_var_name}{Fore.RESET}] not found.
    |   {help_message} Check if you wrote the variable name correctly.''')
        out_error_stroke(_stroke)
        os._exit(-1)

    @classmethod
    def ERROR_LABMDA_NOT_FOUND(self, _lambda_name: str, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_LABMDA_NOT_FOUND')}
    |   Lambda expression [{Fore.GREEN}{_lambda_name}{Fore.RESET}] not found.
    |   {help_message} Try to create a lambda expression with this name.''')
        out_error_stroke(_stroke)
        os._exit(-1)


    @classmethod
    def ERROR_VARIABLE_NOT_CHAINGABLE(self, _var_name: str, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_VARIABLE_NOT_CHAINGABLE')}
    |   Variable [{Fore.GREEN}{_var_name}{Fore.RESET}] not chaingable.
    |   {help_message} Use the ({Fore.YELLOW}let{Fore.RESET}) keyword to make the variable chaingable.''')
        out_error_stroke(_stroke)
        os._exit(-1)

    @classmethod
    def ERROR_VARIABLE_TYPE(self, _var_name: str, _type: str, _var_type: str, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_VARIABLE_TYPE')}
    |   Variable [{Fore.GREEN}{_var_name}{Fore.RESET}] expects type {Fore.MAGENTA}<{_type}>{Fore.RESET} and you passed an argument of type {Fore.MAGENTA}<{_var_type}>{Fore.RESET}.
    |   {help_message} Try to convert the type of expression.''')
        out_error_stroke(_stroke)
        os._exit(-1)
    
    @classmethod
    def ERROR_VARIABLE_NAME_IS_NOT_SET(self, _type: str, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_VARIABLE_NAME_IS_NOT_SET')}
    |   Variable {Fore.MAGENTA}<{_type}>{Fore.RESET} type, name is not set.
    |   {help_message} Enter the name of the variable between the type and the equals sign.''')
        out_error_stroke(_stroke)
        os._exit(-1)

    @classmethod
    def ERROR_BINARY_OPERATION(self, _type_1: str, _type_2: str, _operation: str, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_BINARY_OPERATION')}
    |   Binary operation [{Fore.MAGENTA}{_operation}{Fore.RESET}] is not defined for types [{Fore.MAGENTA}{_type_1}{Fore.RESET}] and [{Fore.MAGENTA}{_type_2}{Fore.RESET}]
    |   {help_message} Try to convert the type of expression.''')
        out_error_stroke(_stroke)
        os._exit(-1)

    @classmethod
    def ERROR_CONVERT_TO_INT(self, _value: str, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_CONVERT_TO_INT')}
    |   Value [{Fore.MAGENTA}{_value}{Fore.RESET}] don't converted to {Fore.MAGENTA}<int>{Fore.RESET} type.
    |   {help_message} Try to replace [{Fore.MAGENTA}{_value}{Fore.RESET}] value to any {Fore.MAGENTA}<int>{Fore.RESET} or {Fore.MAGENTA}<float>{Fore.RESET} string value.''')
        out_error_stroke(_stroke)
        os._exit(-1)

    @classmethod
    def ERROR_CONVERT_TO_FLOAT(self, _value: str, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_CONVERT_TO_FLOAT')}
    |   Value [{Fore.MAGENTA}{_value}{Fore.RESET}] don't converted to {Fore.MAGENTA}<float>{Fore.RESET} type.
    |   {help_message} Try to replace [{Fore.MAGENTA}{_value}{Fore.RESET}] value to any {Fore.MAGENTA}<int>{Fore.RESET} or {Fore.MAGENTA}<float>{Fore.RESET} string value.''')
        out_error_stroke(_stroke)
        os._exit(-1)

    @classmethod
    def ERROR_CONVERT_TO_BOOL(self, _value: str, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_CONVERT_TO_BOOL')}
    |   Value [{Fore.MAGENTA}{_value}{Fore.RESET}] don't converted to {Fore.MAGENTA}<bool>{Fore.RESET} type.
    |   {help_message} Try to replace [{Fore.MAGENTA}{_value}{Fore.RESET}] value to any {Fore.MAGENTA}<int>{Fore.RESET} or {Fore.MAGENTA}<str>{Fore.RESET} value.''')
        out_error_stroke(_stroke)
        os._exit(-1)

    @classmethod
    def ERROR_TYPE(self, _value: str, _stroke: int = 0, _expected_type: str = 'str'):
        print(f'''{debug(compile_error, _stroke, 'ERROR_TYPE')}
    |   Expected {Fore.MAGENTA}<{_expected_type}>{Fore.RESET} typed value, not {Fore.MAGENTA}<{_value}>{Fore.RESET}.
    |   {help_message} Use convert method [{Fore.YELLOW}str{Fore.RESET}] to fix.
''')
        out_error_stroke(_stroke)
        os._exit(-1)

    @classmethod
    def ERROR_FORIN_WAIT_TYPE(self, _type: str, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_FORIN_WAIT_TYPE')}
    |   The forin construct expects an iterable types [{Fore.MAGENTA}<str>{Fore.RESET} or {Fore.MAGENTA}<list>{Fore.RESET}], not {Fore.MAGENTA}<{_type}>{Fore.RESET}.
    |   {help_message} Use a different value in this field.''')
        pf = out_pretty_file(''' 
    let (auto) arr = [1,2,3]
    forin (arr -> val){
        print(val)
    }                       
'''.split('\n'))
        out_error_stroke(_stroke)
        print(f'{example_message}')
        for string in pf:
            print(string)
        print(f'{example_message}')
        os._exit(-1)

    @classmethod
    def ERROR_LIST_INDEX_OUT(self, _index: int, _range:int, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_LIST_INDEX_OUT')}
    |   List index {Fore.MAGENTA}{_index}{Fore.RESET} out of range [{Fore.MAGENTA}0-{_range-1}{Fore.RESET}].''')
        out_error_stroke(_stroke)
        os._exit(-1)

    @classmethod
    def ERROR_ARGUMENT_TYPE(self, _function_name: str, _arg_name: str, _wait_arg_type: str, _arg_type: str, _stroke: int = 0, _pos: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_ARGUMENT_TYPE')}
    |   Function [{Fore.GREEN}{_function_name}(){Fore.RESET}] in [{Fore.YELLOW}arg ({_arg_name}), pos ({_pos+1}){Fore.RESET}] waited {Fore.MAGENTA}<{_wait_arg_type}>{Fore.RESET} type argument. You taked {Fore.MAGENTA}<{_arg_type}>{Fore.RESET} argument type.
    |   {help_message} Try converting the types of arguments you are entering.''')
        out_error_stroke(_stroke)
        os._exit(-1)

    @classmethod
    def ERROR_OUT_ARGUMENT_TYPE(self, _function_name:str, _wait_arg_type: str, _arg_type: str, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_OUT_ARGUMENT_TYPE')}
    |   By definition, a function [{Fore.GREEN}{_function_name}(){Fore.RESET}] must return an argument of type {Fore.MAGENTA}<{_wait_arg_type}>{Fore.RESET}, and it returns an argument of type {Fore.MAGENTA}<{_arg_type}>{Fore.RESET}.
    |   {help_message} Try changing the body of the function so that it returns an argument of the correct type.''')
        out_error_stroke(_stroke)
        print(example_message)
        pf = out_pretty_file(f''' 
    fn <{_arg_type}> {_function_name}(arg1, arg2, ...)
        ...        
'''.split('\n'))
        for string in pf:
            print(string)
        print(example_message)
        os._exit(-1)

    @classmethod
    def ERROR_VOID_FUNCTION_NOT_BE_RETURN(self, _function_name: str, _arg_type: str, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_VOID_FUNCTION_NOT_BE_RETURN')}
    |   The function [{Fore.GREEN}{_function_name}(){Fore.RESET}] cannot return an argument of type {Fore.MAGENTA}<{_arg_type}>{Fore.RESET} because the function is defined with type {Fore.MAGENTA}<void>{Fore.RESET}
    |   {help_message} Try changing the function type.''')
        out_error_stroke(_stroke)
        os._exit(-1)

    @classmethod
    def ERROR_MATCH_WAIT_CASE(self, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_MATCH_WAIT_CASE')}
    |   The match construction waited at least one case.
    |   {help_message} Try adding additional cases.''')
        out_error_stroke(_stroke)
        os._exit(-1)
    
    @classmethod
    def ERROR_INVALID_MATCH_CONSTRUCTION(self, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_INVALID_MATCH_CONSTRUCTION')}
    |   Invalid match construction.
    |   {help_message} Try adding additional cases.''')
        out_error_stroke(_stroke)
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

    @classmethod
    def ERROR_STRUCT_INIT(self,_name, _type, _waited_types, _index, _stroke: int = 0):
        print(f'''{debug(compile_error, _stroke, 'ERROR_STRUCT_INIT')}
    |   The structure [{Fore.GREEN}{_name}{Fore.RESET}] constructer waited {Fore.MAGENTA}<{_waited_types}>{Fore.RESET} typed argument, not {Fore.MAGENTA}<{_type}>{Fore.RESET} in pos [{Fore.YELLOW}{_index+1}{Fore.RESET}].
    |   {help_message} Try adding additional cases.''')
        out_error_stroke(_stroke)
        os._exit(-1)