from colorama import Fore

class BaseError:


    @classmethod
    def NOT_CHAINGABLE_VAR(self, name):
        print(' | '+Fore.YELLOW + 'Error' + Fore.RESET)
        print(' | '+f'Variable [{Fore.GREEN}{name}{Fore.RESET}] is not chaingable')
        print(' | '+Fore.MAGENTA+'Use tag "var" to create a chaingable variable'+Fore.RESET)
        exit(-1)

    @classmethod
    def VARIABLE_NOT_FOUND(self, name):
        print(' | '+Fore.YELLOW + 'Error' + Fore.RESET)
        print(' | '+f'Variable [{Fore.GREEN}{name}{Fore.RESET}] not found')
        exit(-1)

    @classmethod
    def NOT_SUPORTED_STRING_OPERATION(self, operation):
        print(' | '+Fore.YELLOW + 'Error' + Fore.RESET)
        print(' | '+f'String operation [{Fore.GREEN}{operation}{Fore.RESET}] not supported')
        exit(-1)

    @classmethod
    def NOT_SUPORTED_NUMBER_OPERATION(self, operation):
        print(' | '+Fore.YELLOW + 'Error' + Fore.RESET)
        print(' | '+f'Number operation [{Fore.GREEN}{operation}{Fore.RESET}] not supported')
        exit(-1)

    @classmethod
    def NOT_SUPORTED_STATEMENT(self):
        print(' | '+Fore.YELLOW + 'Error' + Fore.RESET)
        print(' | '+f'Statement not supported')
        exit(-1)

    @classmethod
    def NOT_SUPORTED_BINARY_TYPES(self, type1, type2, operation):
        print(' | '+Fore.YELLOW + 'Error' + Fore.RESET)
        print(' | '+f'Operation [{Fore.GREEN}{operation}{Fore.RESET}] not supported between [{Fore.CYAN}{type1}{Fore.RESET}] and [{Fore.CYAN}{type2}{Fore.RESET}] types')
        exit(-1)

    @classmethod
    def NOT_SUPORTED_UNARY_TYPE(self, type, operation):
        print(' | '+Fore.YELLOW + 'Error' + Fore.RESET)
        print(' | '+f'Unary operation [{Fore.GREEN}{operation}{Fore.RESET}] with [{Fore.CYAN}{type}{Fore.RESET}] type not supported')
        exit(-1)

    @classmethod
    def FUNCTION_NOT_FOUND(self, name):
        print(' | '+Fore.YELLOW + 'Error' + Fore.RESET)
        print(' | '+f'Function [{Fore.GREEN}{name}{Fore.RESET}] not found')
        exit(-1)

    @classmethod
    def CONSUME_ERROR(self, token_type_1, token_type_2):
        print(' | '+Fore.YELLOW + 'Error' + Fore.RESET)
        print(' | '+f'Token type [{Fore.GREEN}{token_type_1}{Fore.RESET}] consume [{Fore.GREEN}{token_type_1}{Fore.RESET}] token type')
        exit(-1)