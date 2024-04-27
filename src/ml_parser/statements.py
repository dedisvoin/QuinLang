from src.ml_parser.expressions import Expression, NoneExpr,LambdaExpr
from src.ml_parser.variables import Variables
from src.ml_parser.errors import Errors
from src.ml_parser.functions import Functions, FunctionTypes, FunctionReturnType
from src.ml_parser.value_mchine import ValueTypes,Values
from src.ml_parser.lib_manager import load_lib
import sys


sys.setrecursionlimit(1000000)

class BREAK_EXCEPTION(BaseException):
    ...

class CONTINUE_EXCEPTION(BaseException):
    ...

class RETURN_EXCEPTION(BaseException):
    ...

class Statemets:

    class LibLoading:
        def __init__(self, _name: str, _stroke: int) -> None:
            self.__name = _name
            self.__stroke = _stroke

        def exec(self):
            load_lib(f'{self.__name}')
            

    class VarAsignet:
        def __init__(self, _name: str, _expr: Expression, _type: str, _chaingable: bool = True, _stroke: int = 0) -> None:
            self.__name = _name
            self.__expr = _expr
            self.__type = _type
            self.__chaingable = _chaingable

            self.__stroke = _stroke

        def exec(self) -> None:
            
            if not isinstance(self.__expr, LambdaExpr):
                result_value = self.__expr.eval()
                if self.__type == 'auto':
                    self.__type = result_value.get_type()
                else:
                    if self.__type == result_value.get_type():
                        ...
                    else:
                        Errors.ERROR_ASIGNET_TYPE(self.__name, self.__type, result_value.get_type(), self.__stroke)
                
                Variables.set(self.__name, result_value, self.__chaingable, self.__type)
            else:
                
                if self.__type == 'call' or self.__type == 'auto':
                    Variables.set(self.__name, self.__expr, self.__chaingable, 'call')
                else:
                    Errors.ERROR_LAMBDA_ASIGNET_TYPE(self.__name, self.__type, 'call', self.__stroke)

    class VarsAsignet:
        def __init__(self, _names: list[str], _exprs: list, _types: list[str], _chaingable: bool = True, _stroke: int = 0) -> None:
            self.__names = _names
            self.__exprs = _exprs
            self.__types = _types
            self.__chaingable = _chaingable

            self.__stroke = _stroke

        def exec(self) -> None:
            for i in range(len(self.__names)):
                result_value = self.__exprs[i].eval()
                if self.__types[i] == 'auto':
                    self.__types[i] = result_value.get_type()
                else:
                    if self.__types[i] == result_value.get_type():
                        ...
                    else:
                        Errors.ERROR_ASIGNET_TYPE(self.__names[i], self.__types[i], result_value.get_type(), self.__stroke)
                
                Variables.set(self.__names[i], result_value, self.__chaingable, self.__types[i])

    class VarChainge:
        def __init__(self, _name: str, _expr: Expression, _stroke: int = 0) -> None:
            self.__name = _name
            self.__expr = _expr

            self.__stroke = _stroke
        
        def exec(self) -> None:
            result_value = self.__expr.eval()
            
            
            if Variables.is_in(self.__name):
                var_type = Variables.get(self.__name)[2]
                if Variables.get(self.__name)[1]:
                    if Variables.get(self.__name)[2] == result_value.get_type():
                        Variables.set(self.__name, result_value, True, Variables.get(self.__name)[2])
                    else:
                        Errors.ERROR_VARIABLE_TYPE(self.__name, var_type ,result_value.get_type(), self.__stroke)
                else:
                    Errors.ERROR_VARIABLE_NOT_CHAINGABLE(self.__name, self.__stroke)
            else:
                
                Errors.ERROR_VARIABLE_NOT_FOUND(self.__name, self.__stroke)

    class FunctCall:
        def __init__(self, _name: str, _args_expr: list[Expression], _stroke: int = 0) -> None:
            self.__name = _name
            self.__args_expr = _args_expr
            self.__stroke = _stroke
            

        def exec(self):
            values = []
            for arg in self.__args_expr:
                if isinstance(arg, LambdaExpr):
                    values.append(arg)
                else:
                    values.append(arg.eval())
            func = Functions.get(self.__name)[0]
            if isinstance(func, Statemets.BlockState):
                function_type = Functions.get(self.__name)[2]
                Variables.in_buffer()
                for i, argument in enumerate(Functions.get(self.__name)[3]):
                    if argument[1] == values[i].get_type():
                        Variables.set(argument[0], values[i], True, argument[1])
                    else:
                        Errors.ERROR_ARGUMENT_TYPE(self.__name, argument[0], argument[1], values[i].get_type(), self.__stroke, i)
            
                try:
                    func.exec()
                except Statemets.ReturnState as exp:
                    result = exp.get_result()
                    if function_type != 'void' and function_type != 'auto':
                        if result.get_type() == function_type:
                            return result
                        else:
                            Errors.ERROR_OUT_ARGUMENT_TYPE(self.__name, function_type, result.get_type(), self.__stroke)
                    elif function_type == 'auto':
                        return result
                    else:
                        Errors.ERROR_VOID_FUNCTION_NOT_BE_RETURN(self.__name, result.get_type(), self.__stroke)

                Variables.out_buffer()
            else:
                func(*values, _stroke=self.__stroke)
        
        def eval(self):
            values = []
            for arg in self.__args_expr:
                if isinstance(arg, LambdaExpr):
                    values.append(arg)
                else:
                    values.append(arg.eval())
            func = Functions.get(self.__name)[0]
            
            if isinstance(func, Statemets.BlockState):
                function_type = Functions.get(self.__name)[2]
                Variables.in_buffer()
                for i, argument in enumerate(Functions.get(self.__name)[3]):
                    if argument[1] == values[i].get_type():
                        Variables.set(argument[0], values[i], True, argument[1])
                    else:
                        Errors.ERROR_ARGUMENT_TYPE(self.__name, argument[0], argument[1], values[i].get_type(), self.__stroke, i)
                
                
                try:
                    func.exec()
                except Statemets.ReturnState as exp:
                    result = exp.get_result()
                    if function_type != 'void' and function_type != 'auto':
                        if result.get_type() == function_type:
                            return result
                        else:
                            Errors.ERROR_OUT_ARGUMENT_TYPE(self.__name, function_type, result.get_type(), self.__stroke)
                    elif function_type == 'auto':
                        return result
                    else:
                        Errors.ERROR_VOID_FUNCTION_NOT_BE_RETURN(self.__name, result.get_type(), self.__stroke)

                Variables.out_buffer()
                
            else:
                return func(*values, _stroke=self.__stroke)

    class If:
        def __init__(self, _condition: Expression, _state_if, _state_else = None) -> None:
            self.__condition = _condition
            self.__state_if = _state_if
            self.__state_else = _state_else

        def exec(self):
            condition_value = self.__condition.eval()
            if condition_value.get_value() == True:
                self.__state_if.exec()
            elif condition_value.get_value() == False and self.__state_else != None:
                self.__state_else.exec()

    class For:
        def __init__(self, _var_state, _condition, _expr, _state) -> None:
            self.__var_state = _var_state
            self.__condition = _condition
            self.__expr = _expr
            self.__state = _state

        def exec(self):
            self.__var_state.exec()
            
            while self.__condition.eval().get_value() == True:
                try:
                    
                    self.__state.exec()  
                except BREAK_EXCEPTION:
                    break
                except CONTINUE_EXCEPTION:
                    self.__expr.exec()
                    continue
                self.__expr.exec()
    
    class While:
        def __init__(self, _condition, _state) -> None:
            self.__condition = _condition
            self.__state = _state

        def exec(self):
            while self.__condition.eval().get_value() == True:
                try:
                    self.__state.exec()  
                except BREAK_EXCEPTION:
                    break
                except CONTINUE_EXCEPTION:
                    continue
             
    class ForIn:
        def __init__(self, _arr, _var_name, _state, _stroke: int = 0) -> None:
            self.__arr = _arr
            self.__var_name = _var_name
            self.__state = _state
            self.__stroke = _stroke

        def exec(self):
            array = self.__arr.eval()
            if array.get_type() == ValueTypes.LIST:
                array = array.get_value()
                array_len = len(array)
                Variables.set(self.__var_name, None, True, 'any')
                i = 0
                while i<array_len:
                    
                    Variables.set(self.__var_name, array[i], True, 'any')
                    i+=1
                    try:
                        self.__state.exec()
                    except BREAK_EXCEPTION:
                        break
                    except CONTINUE_EXCEPTION:
                        continue
            elif array.get_type() == ValueTypes.STR:
                array = array.get_value()
                array_len = len(array)
                Variables.set(self.__var_name, None, True, 'any')
                i = 0
                while i<array_len:
                    Variables.set(self.__var_name, Values.ValStr( array[i] ), True, 'any')
                    i+=1
                    try:
                        self.__state.exec()
                    except BREAK_EXCEPTION:
                        break
                    except CONTINUE_EXCEPTION:
                        continue
            else:
                Errors.ERROR_FORIN_WAIT_TYPE(array.get_type(), self.__stroke)
                
    class BlockState:
        def __init__(self) -> None:
            self.__statements = []

        def exec(self):
            for state in self.__statements:
                state.exec()

        def add(self, _statement):
            self.__statements.append(_statement)

    class BreakState:
        def __init__(self) -> None:
            ...

        def exec(self):
            raise BREAK_EXCEPTION()
        
    class ContinueState:
        def __init__(self) -> None:
            ...

        def exec(self):
            raise CONTINUE_EXCEPTION()
    
    class ReturnState(BaseException):
        def __init__(self, _expr) -> None:
            self.__expr = _expr
            self.__result = None

        def get_result(self):
             return self.__result

        def exec(self):
            self.__result = self.__expr.eval()
            raise self

    class FunctionDefineState:
        def __init__(self, _funct_name: str, _funct_type: str, _arguments: list, _statement) -> None:
            self.__funct_name = _funct_name
            self.__funct_type = _funct_type
            self.__argumnts = _arguments
            self.__statement = _statement

        def exec(self):
            Functions.set(self.__funct_name, self.__statement, FunctionTypes.USER, self.__funct_type, self.__argumnts)

    class MatchCaseState:
        def __init__(self, _expr, _evaled_exprs: list, _stroke: int = 0) -> None:
            self.__expr = _expr
            self.__evaled_exprs = _evaled_exprs
            self.__stroke = _stroke

        def exec(self):
            value = self.__expr.eval().get_value()

            eval_expr = [[e, s] for e, s in self.__evaled_exprs if type(e) != NoneExpr]
            base_expr = None
            for state in self.__evaled_exprs:
                if type(state[0]) == NoneExpr:
                    base_expr = state[1]
                
            for evaluate in eval_expr:
                if evaluate[0].eval().get_value() == value:
                    evaluate[1].exec()
                    break
            else:
                if base_expr is not None:   base_expr.exec()