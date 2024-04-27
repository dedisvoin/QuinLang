from copy import copy
from src.ml_parser.value_mchine import (
    ValueTypes, Values
)
from src.ml_tokenizer.tokens import (
    Token, TokenTypes
)
from src.ml_parser.expressions import (
    IntExpr, FloatExpr, StringExpr, UnaryExpr, BinaryExpr, VarExpr, BasiclambdaCallExpr, 
    ArrayExpr, FunctExpr, BoolExpr, CondExpr, ArrayGetExpr, DiapozonExpr, NoneExpr, LambdaExpr, lambdaCallExpr
)
from src.ml_parser.statements import Statemets
from src.ml_parser.errors import Errors
from colorama import Fore

class Parser:
    def __init__(self) -> None:
        self.__tokens = []
        self.__tokens_count = 0

        self.__pos = 0
        self.__executes = []

    def get_executes(self) -> list[Statemets]:
        return self.__executes
    
    def next_token(self) -> None:
        self.__pos += 1

    def get_token(self, _add: int = 0) -> Token:
        return self.__tokens[self.__pos + _add]

    def match(self, _token_type: TokenTypes) -> bool:
        if self.get_token().get_type() != _token_type:
            return False
        else:
            self.next_token()
            return True

    def send_tokens(self, _tokens: list[Token]) -> None:
        self.__tokens = copy(_tokens)
        self.__tokens_count = len(self.__tokens)

    def statement(self):
        current_token = self.get_token()
        if current_token.get_type() == TokenTypes.USING:
            return self.state_lib_load()
        if current_token.get_type() == TokenTypes.LET:
            return self.state_asignet_let()
        if current_token.get_type() == TokenTypes.CONST:
            return self.state_asignet_const()
        if current_token.get_type() == TokenTypes.Basic.WORD and self.get_token(1).get_type() == TokenTypes.EQUAL:
            return self.state_var_change()
        if current_token.get_type() == TokenTypes.Basic.WORD and self.get_token(1).get_type() == TokenTypes.LEFT_BRACK:
            return self.state_function_call()
        if current_token.get_type() == TokenTypes.IF:
            return self.state_if_else()
        if current_token.get_type() == TokenTypes.FOR:
            return self.state_for()
        if current_token.get_type() == TokenTypes.WHILE:
            return self.state_while()
        if current_token.get_type() == TokenTypes.FORIN:
            return self.state_forin()
        if current_token.get_type() == TokenTypes.BREAK and self.get_token(1).get_type() == TokenTypes.STRELA_RIGHT:
            return self.state_break()
        if current_token.get_type() == TokenTypes.CONTINUE and self.get_token(1).get_type() == TokenTypes.STRELA_RIGHT:
            return self.state_continue()
        if current_token.get_type() == TokenTypes.RETURN and self.get_token(1).get_type() == TokenTypes.STRELA_RIGHT:
            return self.state_return()
        if current_token.get_type() == TokenTypes.FN:
            return self.state_function_define()
        if current_token.get_type() == TokenTypes.MATCH:
            return self.state_match()
        
    def state_lib_load(self):
        self.match(TokenTypes.USING)
        if self.get_token().get_type() == TokenTypes.Basic.TEXT:
            lib_name = self.get_token().get_data()
            stroke = self.get_token().get_line()
            self.match(TokenTypes.Basic.TEXT)
            
            return Statemets.LibLoading(lib_name, stroke)
        
    def state_match(self):
        self.match(TokenTypes.MATCH)
        stroke = self.get_token().get_line()
        value_expr = self.expression()
        self.match(TokenTypes.STRELA_RIGHT)
        self.match(TokenTypes.LEFT_CURLY_BRACK)

        eval_and_exec_values = []

        while not self.match(TokenTypes.RIGHT_CURLY_BRACK):
            if self.match(TokenTypes.CASE):
                expr = self.expression()
                self.match(TokenTypes.STRELA_RIGHT)
                execute = self.state_or_block()
                eval_and_exec_values.append([expr, execute])
            else:
                Errors.ERROR_MATCH_WAIT_CASE(stroke)
        if len(eval_and_exec_values)<=0:
            Errors.ERROR_INVALID_MATCH_CONSTRUCTION(stroke)
        return Statemets.MatchCaseState(value_expr, eval_and_exec_values, stroke)

        
    def state_function_define(self):
        self.match(TokenTypes.FN)
        self.match(TokenTypes.LEFT_BRACK)
        if self.get_token().get_type() == TokenTypes.Basic.WORD:
            funtion_return_type = self.get_token().get_data()
            self.match(TokenTypes.Basic.WORD)
            self.match(TokenTypes.RIGHT_BRACK)
            if self.get_token().get_type() == TokenTypes.Basic.WORD:
                function_name = self.get_token().get_data()
                self.match(TokenTypes.Basic.WORD)
                self.match(TokenTypes.LEFT_BRACK)
                arguments = []
                while not self.match(TokenTypes.RIGHT_BRACK):
                    arg_name = self.get_token().get_data()
                    self.match(TokenTypes.Basic.WORD)
                    self.match(TokenTypes.DOUBLE_DOT)
                    arg_type = self.get_token().get_data()
                    self.match(TokenTypes.Basic.WORD)
                    self.match(TokenTypes.COMMA)
                    arguments.append([arg_name, arg_type])
                statement = self.state_block()
                return Statemets.FunctionDefineState(function_name, funtion_return_type, arguments, statement)
            else:
                raise 'function define_error'
        else:
            raise 'function'
        
    def state_break(self):
        self.match(TokenTypes.BREAK)
        self.match(TokenTypes.STRELA_RIGHT)
        return Statemets.BreakState()
    
    def state_return(self):
        self.match(TokenTypes.RETURN)
        self.match(TokenTypes.STRELA_RIGHT)

        return Statemets.ReturnState(self.expression())
    
    def state_continue(self):
        self.match(TokenTypes.CONTINUE)
        self.match(TokenTypes.STRELA_RIGHT)
        return Statemets.ContinueState()
        
    def state_forin(self):
        
        self.match(TokenTypes.FORIN)
        self.match(TokenTypes.LEFT_BRACK)
        
        arr_or_str = self.expression()
        self.match(TokenTypes.Basic.WORD)
        stroke = self.get_token().get_line()
        if self.match(TokenTypes.STRELA_RIGHT):
        
            var_name = self.get_token().get_data()
            
            
            self.match(TokenTypes.Basic.WORD)
            self.match(TokenTypes.RIGHT_BRACK)
            
            state = self.state_block()
            
            return Statemets.ForIn(arr_or_str, var_name, state, stroke)
        
    def state_for(self):
        
        self.match(TokenTypes.FOR)
        self.match(TokenTypes.LEFT_BRACK)
        
        var_statement = self.statement()
        
        self.match(TokenTypes.DOT_AND_COMMA)
        condition = self.expression()
        
        self.match(TokenTypes.DOT_AND_COMMA)
        expression = self.statement()
        
        self.match(TokenTypes.RIGHT_BRACK)
        
        state = self.state_block()
        
        
        return Statemets.For(var_statement, condition, expression, state)
    
    def state_while(self):
        
        self.match(TokenTypes.WHILE)
        self.match(TokenTypes.LEFT_BRACK)
        
        condition = self.expression()
        
        self.match(TokenTypes.RIGHT_BRACK)
        
        state = self.state_block()
        
        
        return Statemets.While(condition, state)
    

        
    def state_if_else(self):
        self.match(TokenTypes.IF)
        condition = self.expression()
        if_statement = self.state_or_block()
        else_statement = None
        if self.match(TokenTypes.ELSE):
            else_statement = self.state_or_block()

        return Statemets.If(condition, if_statement, else_statement)
    
    def state_or_block(self):
        if self.get_token().get_type() == TokenTypes.LEFT_CURLY_BRACK:
            return self.state_block()
        return self.statement()
    
    def state_block(self):
        block = Statemets.BlockState()
        self.match(TokenTypes.LEFT_CURLY_BRACK)
        while not self.match(TokenTypes.RIGHT_CURLY_BRACK):
            block.add(self.statement())
        
        return block

    def state_function_call(self):
        funct_name_token = self.get_token()
        self.match(TokenTypes.Basic.WORD)
        if self.match(TokenTypes.LEFT_BRACK):
            return self.returned_function_call(funct_name_token.get_data())


    def state_var_change(self):
        var_name_token = self.get_token()
        self.match(TokenTypes.Basic.WORD)
        if self.match(TokenTypes.EQUAL):
            var_name = var_name_token.get_data()
            var_value = self.expression()
            stroke = var_name_token.get_line()
            return Statemets.VarChainge(var_name, var_value, stroke)


    def state_asignet_let(self):
        stroke = self.get_token().get_line()
        self.match(TokenTypes.LET)
        var_types = []
        

        self.match(TokenTypes.LEFT_BRACK)
        while not self.match(TokenTypes.RIGHT_BRACK):
            var_types.append(self.get_token().get_data())
            self.match(TokenTypes.Basic.WORD)
            self.match(TokenTypes.COMMA)

        types_len = len(var_types)
        
        var_names = []
        while not self.match(TokenTypes.EQUAL):
            if self.get_token().get_type() == TokenTypes.Basic.WORD:
                var_names.append(self.get_token().get_data())
                self.match(TokenTypes.Basic.WORD)
            else:
                self.match(TokenTypes.COMMA)
        
        
        self.__pos-=1
        
        if len(var_types) == 1:
            
            if self.match(TokenTypes.EQUAL):
                var_value = self.expression()
                
                return Statemets.VarAsignet(var_names[0], var_value, var_types[0], True, stroke)
            else:
                var_type = var_types[0]
                
                Errors.ERROR_VARIABLE_NAME_IS_NOT_SET(var_type, stroke)
        else:
            exprs = []
            
            if self.match(TokenTypes.EQUAL):

                while not self.match(TokenTypes.DOT_AND_COMMA):
                    exprs.append(self.expression())
                    self.match(TokenTypes.COMMA)
            
            
            return Statemets.VarsAsignet(var_names, exprs, var_types, True, stroke)



    def state_asignet_const(self):
        self.match(TokenTypes.CONST)
        self.match(TokenTypes.LEFT_BRACK)
        var_type_token = self.get_token()
        self.match(TokenTypes.Basic.WORD)
        self.match(TokenTypes.RIGHT_BRACK)
        var_name_token = self.get_token()
        if self.match(TokenTypes.Basic.WORD):
            if self.match(TokenTypes.EQUAL):
                var_name = var_name_token.get_data()
                var_type = var_type_token.get_data()
                var_value = self.expression()
                stroke = var_name_token.get_line()
                return Statemets.VarAsignet(var_name, var_value, var_type, False, stroke)
        else:
            var_type = var_type_token.get_data()
            stroke = var_type_token.get_line()
            Errors.ERROR_VARIABLE_NAME_IS_NOT_SET(var_type, stroke)
    

    def expression(self):
        return self.or_condition()
    
    def or_condition(self):
        expr = self.and_condition()

        while True:
            if self.match(TokenTypes.OR):
                expr = CondExpr(expr, self.and_condition(), '||', self.get_token().get_line())
                continue
            break
        
        return expr
            

    def and_condition(self):
        expr = self.equality_condition()

        while True:
            if self.match(TokenTypes.AND):
                expr = CondExpr(expr, self.equality_condition(), '&&', self.get_token().get_line())
                continue
            break
        
        return expr
    
    def equality_condition(self):
        expr = self.condition()
        if self.match(TokenTypes.DOUBLE_EQUAL):
            expr = CondExpr(expr, self.condition(), '==', self.get_token().get_line())

        if self.match(TokenTypes.NOT_EQUAL):
            expr = CondExpr(expr, self.condition(), '<>', self.get_token().get_line())

        return expr

    def condition(self):
        expr = self.additive()

        while True:
            if self.match(TokenTypes.LESS):
                expr = CondExpr(expr, self.additive(), '<', self.get_token().get_line())
                continue
            if self.match(TokenTypes.BIGGER):
                expr = CondExpr(expr, self.additive(), '>', self.get_token().get_line())
                continue
            if self.match(TokenTypes.EQUAL_LESS):
                expr = CondExpr(expr, self.additive(), '<=', self.get_token().get_line())
                continue
            if self.match(TokenTypes.EQUAL_BIGGER):
                expr = CondExpr(expr, self.additive(), '>=', self.get_token().get_line())
                continue
            break
        return expr
    
    def additive(self):
        expr = self.multiplicative()
        stroke = self.get_token().get_line()
        while True:
            if self.match(TokenTypes.PLUS):
                expr = BinaryExpr(expr, self.multiplicative(), '+', stroke)
                continue
            if self.match(TokenTypes.MINUS):
                expr = BinaryExpr(expr, self.multiplicative(), '-', stroke)
                continue
            break
        return expr
    
    def multiplicative(self):
            expr = self.unary()
            stroke = self.get_token().get_line()
            while True:
                if self.match(TokenTypes.DIVISION):
                    expr = BinaryExpr(expr, self.unary(), '/', stroke)
                    continue
                elif self.match(TokenTypes.MULTIPLICATION):
                    expr = BinaryExpr(expr, self.unary(), '*', stroke)
                    continue
                elif self.match(TokenTypes.PERCENT):
                    expr = BinaryExpr(expr, self.unary(), '%', stroke)
                    continue
                break
            return expr
    
    def unary(self):
        if self.match(TokenTypes.MINUS):
            return UnaryExpr( self.primary(), '-')
        if self.match(TokenTypes.DOUBLE_PLUS):
            return UnaryExpr( self.primary(), '++')
        if self.match(TokenTypes.DOUBLE_MINUS):
            return UnaryExpr( self.primary(), '--')
        if self.match(TokenTypes.PLUS):  
            return self.primary()
        return self.primary()
    

    def is_float_number(self, _data: str) -> bool:
        if _data.count('.') == 1: return True
        return False
    
    def returned_function_call(self, _funct_name: str):
        self.match(TokenTypes.LEFT_BRACK)
        stroke = self.get_token().get_line()
        args = []
        while not self.match(TokenTypes.RIGHT_BRACK):
            expr = self.expression()
            args.append(expr)
            self.match(TokenTypes.COMMA)
        return FunctExpr(_funct_name, args, stroke)
    
    def get_arr_element(self, _funct_name: str):
        self.match(TokenTypes.LEFT_RECT_BRACK)
        stroke = self.get_token().get_line()
        index = self.expression()
        self.match(TokenTypes.RIGHT_RECT_BRACK)
        
        return ArrayGetExpr(_funct_name, index, stroke)
    

    def lambda_call(self, _funct_name: str):

        stroke = self.get_token().get_line()
        self.match(TokenTypes.SNAKE)
        self.match(TokenTypes.LEFT_BRACK)
            
            
        args = []
        
        while not self.match(TokenTypes.RIGHT_BRACK):
            expr = self.expression()
            args.append(expr)
            self.match(TokenTypes.COMMA)
        
        return lambdaCallExpr(_funct_name, args, stroke)

    
    def primary(self):
        current_token = self.get_token(0)  
        # Numbers
        if self.match(TokenTypes.Basic.NUMBER):
            value = current_token.get_data()
            if self.is_float_number(value):
                return FloatExpr(float(value))
            else:
                return IntExpr(int(value))
        
        # Text
        if self.match(TokenTypes.Basic.TEXT):
            value = current_token.get_data()
            return StringExpr(value)
        
        if self.match(TokenTypes.TRUE):
            return BoolExpr(True)
        
        if self.match(TokenTypes.FALSE):
            return BoolExpr(False)
        
        # Functions

        if self.match(TokenTypes.Basic.WORD):

            if self.get_token().get_type() == TokenTypes.LEFT_BRACK:
                return self.returned_function_call(current_token.get_data())
            elif self.get_token().get_type() == TokenTypes.LEFT_RECT_BRACK:
                return self.get_arr_element(current_token.get_data())
            elif self.get_token().get_type() == TokenTypes.SNAKE:

                return self.lambda_call(current_token.get_data())
            else:
                value = current_token.get_data()
                stroke = current_token.get_line()
                return VarExpr(value, stroke)
        
        
            
        # Brackets
        if self.match(TokenTypes.LEFT_BRACK):
            expression = self.expression()
            self.match(TokenTypes.RIGHT_BRACK)
            return expression
        
        # thunder
        if self.match(TokenTypes.THUNDER):
            return NoneExpr()
        
        # Array
        if self.match(TokenTypes.LEFT_RECT_BRACK):
            expressions = []
            stroke = current_token.get_line()
            while not self.match(TokenTypes.RIGHT_RECT_BRACK):
                expressions.append(self.expression())
                self.match(TokenTypes.COMMA)
            
            return ArrayExpr(expressions, stroke)
        
        # Diaposon
        if self.match(TokenTypes.SNAKE) and self.get_token().get_type() == TokenTypes.LEFT_RECT_BRACK:
            if self.match(TokenTypes.LEFT_RECT_BRACK):
                start_expr = self.expression()
                self.match(TokenTypes.STRELA_RIGHT)
                stop_expr = self.expression()
                step_expr = None
                if self.match(TokenTypes.DOUBLE_DOT):
                    step_expr = self.expression()
                
                self.match(TokenTypes.RIGHT_RECT_BRACK)
            
                return DiapozonExpr(start_expr, stop_expr, step_expr)
            else:
                ...
        

            

        # lambda create
        if self.match(TokenTypes.LAMBDA):
            self.match(TokenTypes.LEFT_BRACK)
            stroke = self.get_token().get_line()
            args = []
            
            while not self.match(TokenTypes.RIGHT_BRACK):
                arg_name = self.get_token().get_data()
                self.match(TokenTypes.Basic.WORD)
                self.match(TokenTypes.DOUBLE_DOT)
                arg_type = self.get_token().get_data()
                self.match(TokenTypes.Basic.WORD)
                self.match(TokenTypes.COMMA)
                args.append([arg_name, arg_type])

            self.match(TokenTypes.STRELA_RIGHT)
            self.match(TokenTypes.LEFT_CURLY_BRACK)
            expr = self.expression()
            self.match(TokenTypes.RIGHT_CURLY_BRACK)
            
            lambda_expr = LambdaExpr(args, expr, stroke)
            

            evaluate_args = []
            if self.match(TokenTypes.DOUBLE_DOT):
                if self.match(TokenTypes.LEFT_BRACK):
                    while not self.match(TokenTypes.RIGHT_BRACK):
                        evaluate_args.append(self.expression())
                        self.match(TokenTypes.COMMA)
                return BasiclambdaCallExpr(lambda_expr, evaluate_args)
            else:
                return lambda_expr

    def parse(self) -> None:
        while not self.match(TokenTypes.EOF):
            state = self.statement()
            self.__executes.append(state)

    def get_states(self):
        return self.__executes

    def execute(self) -> None:
        for state in self.__executes:
            state.exec()

class Executer:
    def __init__(self) -> 'Executer':
        self.__parser = Parser()

    @property
    def parser(self) -> Parser:
        return self.__parser

    def send_tokens(self, _tokens: list[Token]):
        self.__parser.send_tokens(_tokens)

    def view_states(self):
        for state in self.__parser.get_states():
            print(f'Executable statement ({Fore.CYAN}{type(state)}{Fore.RESET})')
        

    def parse(self):
        self.__parser.parse()

    def execute(self):
        self.__parser.execute()


