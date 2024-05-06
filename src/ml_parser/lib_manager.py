



import importlib.util
import os
from src.ml_parser.functions import Functions
from src.ml_parser.variables import Variables
from colorama import Fore, Style
import sys
import importlib 


def load_lib(_file_name: str, _debug):

    path = f'libs/{_file_name}.py'
    spec = importlib.util.spec_from_file_location(_file_name, path)
    lib_file = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lib_file)
    
    if _debug:
        try:
            ver = lib_file.__dict__['version']
            print(f'Detected python library [{Fore.BLUE}{_file_name.split(".")[0]}{Fore.RESET} -> {Fore.LIGHTGREEN_EX}<version {ver}>{Fore.RESET}]')
        except:
            ver = 'not detected'
            print(f'Detected python library [{Fore.BLUE}{_file_name.split(".")[0]}{Fore.RESET} -> {Fore.LIGHTGREEN_EX}<version {ver}>{Fore.RESET}]')

    try:
        function_names = lib_file.__dict__['function_names']
        if len(function_names)>0:
            if _debug: print(f'<{Fore.CYAN}{_file_name}.py{Fore.RESET}> start load functions...')
            
            for funct_data in function_names:
                if _debug: print(f'    {Fore.MAGENTA}{_file_name}.py{Fore.RESET} -> function {Style.BRIGHT}{Fore.YELLOW}{funct_data[0]}{Fore.RESET}{Style.RESET_ALL} loaded...')
                try:
                    Functions.set_lib_function(funct_data[0].replace('_','.'), lib_file.__dict__[funct_data[0]], funct_data[1])
                    if _debug: print(f'    {Fore.MAGENTA}{_file_name}.py{Fore.RESET} -> {Style.BRIGHT}{Fore.YELLOW}{funct_data[0]}{Fore.RESET}{Style.RESET_ALL} compiling [ {Style.BRIGHT}{Fore.GREEN}SUCCES{Fore.RESET}{Style.RESET_ALL} ]')
                except:
                    if _debug: print(f'    {Fore.MAGENTA}{_file_name}.py{Fore.RESET} -> {Style.BRIGHT}{Fore.YELLOW}{funct_data[0]}{Fore.RESET}{Style.RESET_ALL} compiling [ {Style.BRIGHT}{Fore.RED}ERROR{Fore.RESET}{Style.RESET_ALL} ]')

    except:...
    
    try:
        const_names = lib_file.__dict__['const_names']
        if len(const_names)>0:
            if _debug: print(f'<{Fore.CYAN}{_file_name}.py{Fore.RESET}> start load constants...')
            for funct_data in const_names:
                if _debug: print(f'    {Fore.MAGENTA}{_file_name}.py{Fore.RESET} -> constant {Style.BRIGHT}{Fore.YELLOW}{funct_data[0]}{Fore.RESET}{Style.RESET_ALL} loaded...')
                try:

                    Variables.set(funct_data[0].replace('_','.'), lib_file.__dict__[funct_data[0]], False, funct_data[1])
                    if _debug: print(f'    {Fore.MAGENTA}{_file_name}.py{Fore.RESET} -> {Style.BRIGHT}{Fore.YELLOW}{funct_data[0]}{Fore.RESET}{Style.RESET_ALL} loading [ {Style.BRIGHT}{Fore.GREEN}SUCCES{Fore.RESET}{Style.RESET_ALL} ]')
                except:
                    if _debug: print(f'    {Fore.MAGENTA}{_file_name}.py{Fore.RESET} -> {Style.BRIGHT}{Fore.YELLOW}{funct_data[0]}{Fore.RESET}{Style.RESET_ALL} loading [ {Style.BRIGHT}{Fore.RED}ERROR{Fore.RESET}{Style.RESET_ALL} ]')
    except:...

        


