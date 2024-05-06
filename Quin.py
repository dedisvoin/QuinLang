from src.ml_tokenizer import tokenizer_api
from src.ml_parser import parser_api
from colorama import Fore, Style
import os, sys
import shutil
import time
import art


if __name__ == '__main__':
    class Compiler:
        def __init__(self, _file_name: str, _debug: bool = False, _libs_paths: str = None) -> None:
            self.LP = _libs_paths
            self.T = tokenizer_api.Tokenizer(_file_name, _debug, self.LP)
            self.E = parser_api.Executer(_debug)
          
        def compile(self):
            self.T.run()
            self.E.send_tokens(self.T.get_tokens())
        
        def parse(self):
            self.E.parse()
        
        def execute(self):
            self.E.execute()

    class Args_Wrapper:
        def __init__(self, args) -> None:
            self.__args = args
            

        def implementation(self):
            self.__name = self.__args[1]
            self.__deb = False
            self.__build = False
            if '-d' in self.__args:
                self.__deb = True
            if '-build' in self.__args:
                self.__build = True


        def exec_args(self):
            if not self.__build:
                exec_file(self.__name, self.__deb)
            else:
                build_file(self.__name)

    def build_file(name):
        C = Compiler(name, True)
        C.compile()
        C.parse()
        create_build_file(name)
       
    def exec_file(name, debug = False):
        C = Compiler(name, debug)
        C.compile()
        C.parse()
        C.execute()

    def out_name():
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
        art.tprint('Packer v2.3', space = 1)
        print(f'{Fore.RESET}For {Fore.GREEN}(Quin language){Fore.RESET}                               {Fore.YELLOW}By (Pavlov Ivan){Fore.RESET}')
        print(Fore.RESET)

    def create_build_file(_file_name: str):
        out_name()
        file_name = _file_name
        out_file = _file_name.split('.')[0]

        code = open(file_name,'r', encoding='utf-8').readlines()

        c = ''
        for stroke in code:
            c += stroke.replace('\n', '')+'    \n'

        executer = f'''
from src.ml_tokenizer import tokenizer_api
from src.ml_parser import parser_api
from src.ml_parser import variables

code = \'''{c}\'''

class Compiler:
        def __init__(self, code, _debug: bool = False) -> None:
            self.T = tokenizer_api.Tokenizer.from_text(code, False)
            self.E = parser_api.Executer(False)
            
        def compile(self):
            self.T.run()
            self.E.send_tokens(self.T.get_tokens())
        
        def execute(self):
            self.E.parse()
            self.E.execute()

C = Compiler(code.split('\\n'),0)
C.compile()
C.execute()
input('Press enter to close terminal...')
        '''

        out_file_name = out_file.split('.')[0]

        out_f = open(out_file_name+'.py', 'w')
        out_f.write(executer)
        out_f.close()

        time.sleep(1)
        os.system(f"pyinstaller {out_file_name+'.py'} -F --onefile" )

        os.remove(out_file_name+'.py')
        os.remove(out_file_name+'.spec')
        os.remove('tokens.json')

        os.rename(f"dist\{out_file_name}.exe", f"{out_file_name}.exe")
        time.sleep(0.5)
        shutil.rmtree('build')
        shutil.rmtree('dist')
        print(f'[{Fore.GREEN} SUCCES {Fore.RESET}] Building finished!')
        print(f'File {Fore.CYAN}({out_file_name}.exe){Fore.RESET} out in this directory.')
            
    
    AW = Args_Wrapper(sys.argv)
    AW.implementation()
    AW.exec_args()
