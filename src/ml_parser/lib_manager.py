



from src.ml_parser.functions import Functions
from src.ml_parser.variables import Variables
from colorama import Fore, Style
import sys




def load_lib(_file_name: str):
    try:
        lib_file = __import__(f"libs.{_file_name}")
    except:
        lib_file = __import__(f"{_file_name}")
    



    lib_file = lib_file.__dict__[_file_name]

    try:
        ver = function_names = lib_file.__dict__['version']
        print(f'Detected python library [{Fore.BLUE}{_file_name.split(".")[0]}{Fore.RESET} -> {Fore.LIGHTGREEN_EX}<version {ver}>{Fore.RESET}]')
    except:
        ver = 'not detected'
        print(f'Detected python library [{Fore.BLUE}{_file_name.split(".")[0]}{Fore.RESET} -> {Fore.LIGHTGREEN_EX}<version {ver}>{Fore.RESET}]')

    try:
        function_names = lib_file.__dict__['function_names']
        if len(function_names)>0:
            print(f'<{Fore.CYAN}{_file_name}.py{Fore.RESET}> start load functions...')
            
            for funct_data in function_names:
                print(f'    {Fore.MAGENTA}{_file_name}.py{Fore.RESET} -> function {Style.BRIGHT}{Fore.YELLOW}{funct_data[0]}{Fore.RESET}{Style.RESET_ALL} loaded...')
                try:
                    Functions.set_lib_function(funct_data[0].replace('_','.'), lib_file.__dict__[funct_data[0]], funct_data[1])
                    print(f'    {Fore.MAGENTA}{_file_name}.py{Fore.RESET} -> {Style.BRIGHT}{Fore.YELLOW}{funct_data[0]}{Fore.RESET}{Style.RESET_ALL} compiling [ {Style.BRIGHT}{Fore.GREEN}SUCCES{Fore.RESET}{Style.RESET_ALL} ]')
                except:
                    print(f'    {Fore.MAGENTA}{_file_name}.py{Fore.RESET} -> {Style.BRIGHT}{Fore.YELLOW}{funct_data[0]}{Fore.RESET}{Style.RESET_ALL} compiling [ {Style.BRIGHT}{Fore.RED}ERROR{Fore.RESET}{Style.RESET_ALL} ]')

    except:...
    
    try:
        const_names = lib_file.__dict__['const_names']
        if len(const_names)>0:
            print(f'<{Fore.CYAN}{_file_name}.py{Fore.RESET}> start load constants...')
            for funct_data in const_names:
                print(f'    {Fore.MAGENTA}{_file_name}.py{Fore.RESET} -> constant {Style.BRIGHT}{Fore.YELLOW}{funct_data[0]}{Fore.RESET}{Style.RESET_ALL} loaded...')
                try:

                    Variables.set(funct_data[0].replace('_','.'), lib_file.__dict__[funct_data[0]], False, funct_data[1])
                    print(f'    {Fore.MAGENTA}{_file_name}.py{Fore.RESET} -> {Style.BRIGHT}{Fore.YELLOW}{funct_data[0]}{Fore.RESET}{Style.RESET_ALL} loading [ {Style.BRIGHT}{Fore.GREEN}SUCCES{Fore.RESET}{Style.RESET_ALL} ]')
                except:
                    print(f'    {Fore.MAGENTA}{_file_name}.py{Fore.RESET} -> {Style.BRIGHT}{Fore.YELLOW}{funct_data[0]}{Fore.RESET}{Style.RESET_ALL} loading [ {Style.BRIGHT}{Fore.RED}ERROR{Fore.RESET}{Style.RESET_ALL} ]')
    except:...

        


