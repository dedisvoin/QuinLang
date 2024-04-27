from colorama import Fore, Style
import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

version = '1.3'
const_names = [
    ['colorama_fore_red', 'str'],
    ['colorama_fore_green', 'str'],
    ['colorama_fore_yellow', 'str'],
    ['colorama_fore_blue', 'str'],
    ['colorama_fore_cyan', 'str'],
    ['colorama_fore_resset', 'str']
]

from src.ml_parser.value_mchine import Values
from src.ml_parser.errors import Errors, test_type

colorama_fore_red = Values.ValStr(Fore.RED)
colorama_fore_green = Values.ValStr(Fore.GREEN)
colorama_fore_yellow = Values.ValStr(Fore.YELLOW)
colorama_fore_blue = Values.ValStr(Fore.BLUE)
colorama_fore_cyan = Values.ValStr(Fore.CYAN)
colorama_fore_resset = Values.ValStr(Fore.RESET)