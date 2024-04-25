from typing import Any
from src.ml_parser.value_mchine import (
    Values, ValueTypes
)
from src.ml_parser.variables import Variables
from src.ml_parser.errors import Errors


class Expression:
    def __init__(self) -> None:
        ...
    
    def eval(self) -> Any:
        ...


class IntExpr:
    def __init__(self, _int_number: int) -> None:
        self.__value = Values.ValInt(_int_number)
    
    def eval(self) -> Any:
        return self.__value
    
class NoneExpr:
    def __init__(self) -> None:
        self.__value = Values.ValNone()
    
    def eval(self) -> Any:
        return self.__value
    

class FloatExpr:
    def __init__(self, _float_number: float) -> None:
        self.__value = Values.ValFloat(_float_number)
    
    def eval(self) -> Any:
        return self.__value
    

class StringExpr:
    def __init__(self, _string: str) -> None:
        self.__value = Values.ValStr(_string)
    
    def eval(self) -> Any:
        return self.__value
    

class BoolExpr:
    def __init__(self, _bool: bool) -> None:
        self.__value = Values.ValBool(_bool)
    
    def eval(self) -> Any:
        return self.__value
    

class UnaryExpr:
    def __init__(self, _expr: Expression, _operation: str) -> None:
        self.__expr = _expr
        self.__operation = _operation

    def eval(self) -> Any:
        expression_result = self.__expr.eval()

        if (expression_result.get_type() == ValueTypes.INT):
            value = expression_result.get_value()
            match self.__operation:
                case '-':
                    return Values.ValInt(-value)
                case '++':
                    return  Values.ValInt(value+1)
                case '--':
                    return  Values.ValInt(value-1)
                case _:
                    return  Values.ValInt(value)
        if (expression_result.get_type() == ValueTypes.FLOAT):
            value = expression_result.get_value()
            match self.__operation:
                case '-':
                    return Values.ValFloat(-value)
                case '++':
                    return  Values.ValFloat(value+1)
                case '--':
                    return  Values.ValFloat(value-1)
                case _:
                    return  Values.ValFloat(value)
                

class BinaryExpr:
    def __init__(self, _expr_1: Expression, _expr_2: Expression, _operation: str, _stroke: int) -> None:
        self.__expr_1 = _expr_1
        self.__expr_2 = _expr_2
        self.__operation = _operation
        self.__stroke = _stroke
    
    def eval(self):
        expression_1_result = self.__expr_1.eval()
        expression_2_result = self.__expr_2.eval()

        value_1 = expression_1_result.get_value()
        value_2 = expression_2_result.get_value()


        if ((expression_1_result.get_type() == ValueTypes.FLOAT and expression_2_result.get_type() == ValueTypes.INT) or 
            (expression_2_result.get_type() == ValueTypes.FLOAT and expression_1_result.get_type() == ValueTypes.INT)):
            
            match self.__operation:
                case '+':
                    return Values.ValFloat( value_1 + value_2 )
                case '-':
                    return Values.ValFloat( value_1 - value_2 )
                case '/':
                    return Values.ValFloat( value_1 / value_2 )
                case '*':
                    return Values.ValFloat( value_1 * value_2 )
                case '%':
                    return Values.ValFloat( value_1 % value_2 )
                case _:
                    raise 'Not supported binary operation!'

        elif (expression_1_result.get_type() == ValueTypes.INT and
            expression_2_result.get_type() == ValueTypes.INT):
            match self.__operation:
                case '+':
                    return Values.ValInt( value_1 + value_2 )
                case '-':
                    return Values.ValInt( value_1 - value_2 )
                case '/':
                    return Values.ValInt( value_1 / value_2 )
                case '*':
                    return Values.ValInt( value_1 * value_2 )
                case '%':
                    return Values.ValInt( value_1 % value_2 )
                case _:
                    raise 'Not supported binary operation!'
                
        elif (expression_1_result.get_type() == ValueTypes.STR and
            expression_2_result.get_type() == ValueTypes.INT):
            
            match self.__operation:
                case '*':
                    return Values.ValStr( value_1 * value_2 )
                case _:
                    raise 'Not str supported binary operation!'
                
        elif (expression_1_result.get_type() == ValueTypes.STR and
            expression_2_result.get_type() == ValueTypes.STR):
            
            match self.__operation:
                case '+':
                    return Values.ValStr( value_1 + value_2 )
                case _:
                    raise 'Not str supported binary operation!'
        elif (expression_1_result.get_type() == ValueTypes.LIST and
            expression_2_result.get_type() == ValueTypes.LIST):
            match self.__operation:
                case '+':
                    return Values.ValList( value_1 + value_2 )
                case _:
                    raise 'Not str supported binary operation!'
        else:
            Errors.ERROR_BINARY_OPERATION(expression_1_result.get_type(), expression_2_result.get_type(), self.__operation, self.__stroke)


class CondExpr:
    def __init__(self, _expr_1: Expression, _expr_2: Expression, _operation: str, _stroke: int) -> None:
        self.__expr_1 = _expr_1
        self.__expr_2 = _expr_2
        self.__operation = _operation
        self.__stroke = _stroke
    
    def eval(self):
        expression_1_result = self.__expr_1.eval()
        expression_2_result = self.__expr_2.eval()

        value_1 = expression_1_result.get_value()
        value_2 = expression_2_result.get_value()


        if ((expression_1_result.get_type() == ValueTypes.FLOAT or expression_1_result.get_type() == ValueTypes.INT) and
            (expression_2_result.get_type() == ValueTypes.FLOAT or expression_2_result.get_type() == ValueTypes.INT)):
            
            match self.__operation:
                case '==':
                    return Values.ValBool( value_1 == value_2 )
                case '<>':
                    return Values.ValBool( value_1 != value_2 )
                case '<':
                    return Values.ValBool( value_1 < value_2 )
                case '>':
                    return Values.ValBool( value_1 > value_2 )
                case '<=':
                    return Values.ValBool( value_1 <= value_2 )
                case '>=':
                    return Values.ValBool( value_1 >= value_2 )
                case _:
                    raise 'Not supported cond operation!'
                
        if (expression_1_result.get_type() == ValueTypes.BOOL or expression_1_result.get_type() == ValueTypes.BOOL):
            match self.__operation:
                case '==':
                    return Values.ValBool( value_1 == value_2 )
                case '<>':
                    return Values.ValBool( value_1 != value_2 )
                case '<=':
                    return Values.ValBool( value_1 <= value_2 )
                case '||':
                    return Values.ValBool( value_1 or value_2 )
                case '&&':
                    return Values.ValBool( value_1 and value_2 )
                case _:
                    raise 'Not supported cond operation!'
                
        if (expression_1_result.get_type() == ValueTypes.STR or expression_1_result.get_type() == ValueTypes.STR):
            match self.__operation:
                case '==':
                    return Values.ValBool( value_1 == value_2 )
                case '<>':
                    return Values.ValBool( value_1 != value_2 )
                case _:
                    raise 'Not supported cond operation!'

        else:
            Errors.ERROR_BINARY_OPERATION(expression_1_result.get_type(), expression_2_result.get_type(), self.__operation, self.__stroke)


class VarExpr:
    def __init__(self, _name: str, _stroke: int = 0) -> None:
        self.__name = _name
        self.__stroke = _stroke

    def eval(self):
        if Variables.is_in(self.__name):
            return Variables.get(self.__name)[0]
        else:
            Errors.ERROR_VARIABLE_NOT_FOUND(self.__name, self.__stroke)


class ArrayExpr:
    def __init__(self, _list_expressions: list[Expression], _stroke: int = 0) -> None:
        self.__list_expressions = _list_expressions
        self.__stroke = _stroke
        self.__list_values = []
        for expression in self.__list_expressions:
            self.__list_values.append(expression.eval())
        self.__value = Values.ValList(self.__list_values)

    def eval(self):
        return self.__value


class FunctExpr:
    def __init__(self, _name: str, _args_exprs: list[Expression], _stroke: int = 0) -> None:
        self.__name = _name
        self.__args_exprs = _args_exprs
        self.__stroke = _stroke

    def eval(self):
        from src.ml_parser.statements import Statemets
        return Statemets.FunctCall(self.__name, self.__args_exprs, self.__stroke).eval()
    
    def exec(self):
        from src.ml_parser.statements import Statemets
        return Statemets.FunctCall(self.__name, self.__args_exprs, self.__stroke).exec()
    

class ArrayGetExpr:
    def __init__(self, _name: str, _index: int, _stroke) -> None:
        self.__name = _name
        self.__index = _index
        self.__stroke = _stroke

    def eval(self):
        index = self.__index.eval()
        
        if Variables.is_in(self.__name):
            if Variables.get(self.__name)[0].get_type() == ValueTypes.LIST:
                try:
                    return Variables.get(self.__name)[0].get_value()[index.get_value()]
                except:
                    Errors.ERROR_LIST_INDEX_OUT(index.get_value(), len(Variables.get(self.__name)[0].get_value()), self.__stroke)


class DiapozonExpr:
    def __init__(self, _start_expr, _end_expr, _step_exp = None) -> None:
        self.__start_expr = _start_expr
        self.__stop_expr = _end_expr
        self.__step_expr = _step_exp

    def eval(self):
        start = self.__start_expr.eval().get_value()
        stop = self.__stop_expr.eval().get_value()
        
        if self.__step_expr is None:
            arr = [Values.ValInt(val) for val in range(start, stop+1)]
            return Values.ValList(arr)    
        else:
            
            step = self.__step_expr.eval().get_value()
            
            
            arr = [Values.ValInt(val) for val in range(start, stop+1, step)]
            return Values.ValList(arr)    
        
class LambdaExpr:
    def __init__(self, _args, _expr, _stroke) -> None:
        self.__args = _args
        self.__expr = _expr
        self.__stroke = _stroke

    def eval(self, _evaluate_args):
        evalues_args = [arg.eval() for arg in _evaluate_args]

        Variables.in_buffer()

        
        for i, argument in enumerate(self.__args):
            if argument[1] == evalues_args[i].get_type():
                Variables.set(argument[0], evalues_args[i], True, argument[1])
        
        value = self.__expr.eval()
        Variables.out_buffer()

        

        return value

