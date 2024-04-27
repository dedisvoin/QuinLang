import os
import time
import art
from colorama import Fore, Style

def out_name():
    os.system('cls')
    print(Fore.LIGHTBLUE_EX+Style.BRIGHT)
    art.tprint('Packer v1.1',space = 1)
    print(f'{Fore.RESET}For {Fore.GREEN}(Tor Language){Fore.RESET}                               {Fore.YELLOW}By (Pavlov Ivan){Fore.RESET}')
    print(Fore.RESET)

out_name()

def create_build_file():
    file_name = input(f'input {Fore.YELLOW}[tl]{Fore.RESET} file -> ')
    out_file = input('input out filename -> ')

    code = open(file_name,'r', encoding='utf-8').readlines()

    c = ''
    for stroke in code:
        c+=stroke.replace('\n','')+'    \n'

    executer = f'''
from src.ml_tokenizer import tokenizer_api
from src.ml_parser import parser_api
from src.ml_parser import variables

code = \'''{c}\'''

class Compiler:
    def __init__(self, code, _debug: bool = False) -> None:
        self.T = tokenizer_api.Tokenizer.from_text(code)
        self.E = parser_api.Executer()
        
    def compile(self):
        self.T.run()
        self.E.send_tokens(self.T.get_tokens())
    
    def execute(self):
        self.E.parse()
        self.E.execute()

C = Compiler(code.split('\\n'),0)
C.compile()
C.execute()
print('')
input('Press enter to close terminal...')
    '''

    out_file_name = out_file.split('.')[0]

    out_f = open(out_file_name+'.py', 'w')
    out_f.write(executer)
    out_f.close()


    time.sleep(3)
    os.system(f"pyinstaller {out_file_name+'.py'} -c -D -F" )


    time.sleep(1)
    #os.remove(out_file_name+'.py')
    os.remove(out_file_name+'.spec')
    #os.system('cls')
    #out_name()
    print(f'[ {Fore.GREEN}succes {Fore.RESET}] Building finished!')
    print(f'File {Fore.CYAN}({out_file_name}.exe){Fore.RESET} out in {Fore.YELLOW}[dist/]{Fore.RESET} directory.')

command = ''
while True:
    command = input('command : ')
    if command == 'pack':
        create_build_file()
    if command == 'exit':
        print('exited!')
        break
    if command == 'cls':
        os.system('cls')
        out_name()
        


