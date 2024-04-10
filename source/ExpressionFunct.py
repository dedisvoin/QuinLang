from source.VariablesFunct import *
from source.ParseStringFunct import *
from source.Errors import *


class Expression:
    def __init__(self) -> None:
        ...

    def eval(self):
        ...

    def to_str(self):
         ...

"""
Represents a numeric expression in the program.

The `NumberExp` class represents a numeric expression that evaluates to a single numeric value. It holds a `ValueTypes.NumberValue` instance which represents the numeric value of the expression.

The `eval()` method returns the numeric value of the expression, while the `to_str()` method prints the class name and the numeric value.
"""
class NumberExp(Expression):
    def __init__(self, number: int) -> None:
        self.number = ValueTypes.NumberValue(number)

    def eval(self):
        return self.number
    
    def to_str(self):
        print( self.__class__.__name__, self.number.value)

class BoolExp(Expression):
    def __init__(self, value: bool) -> None:
        self.value = ValueTypes.NumberValue(value)

    def eval(self):
        return self.value
    
    def to_str(self):
        print( self.__class__.__name__, self.value.value)

class StringExp(Expression):
    def __init__(self, string: str) -> None:
        self.string = ValueTypes.StringValue(string)

    def eval(self):
        string_parse_obj = StringParse(self.string.value, Variables.vars_map)
        string_parse_obj.parse()
        self.string.value = string_parse_obj.parsed_string
        return self.string
    
    def to_str(self):
        print( self.__class__.__name__, self.string.value)
    
"""
Represents a unary numeric expression in the program.

The `UnaryExp` class represents a unary numeric expression that evaluates to a single numeric value. It holds an `Expression` instance which represents the operand of the unary operation, and a string representing the unary operation to perform.

The `eval()` method returns the numeric value of the unary expression, applying the specified unary operation to the operand. The `to_str()` method prints the class name, the unary operation, and the numeric value of the expression.
"""
class UnaryExp(Expression):
    def __init__(self, expr: Expression, operation: str) -> None:
          self.expr = expr
          self.operation = operation

    def eval(self):
        result = self.expr.eval()
        if isinstance(result, tuple):
            result = result[0]
        if result.type == ValueTypes.NUMBER:
            result = result.value
            match self.operation:
                case '-':
                    return  ValueTypes.NumberValue(-result)
                case '++':
                    return  ValueTypes.NumberValue(result+1)
                case '--':
                    return  ValueTypes.NumberValue(result-1)
                case _:
                    return  ValueTypes.NumberValue(result)
        else:
            BaseError.NOT_SUPORTED_UNARY_TYPE(result.type, self.operation)
            
    def to_str(self):
        print( self.__class__.__name__,self.operation, self.number.value)
            
"""
Represents a binary numeric expression in the program.

The `BinaryExp` class represents a binary numeric expression that evaluates to a single numeric value. It holds two `Expression` instances which represent the left and right operands of the binary operation, and a string representing the binary operation to perform.

The `eval()` method returns the numeric value of the binary expression, applying the specified binary operation to the operands. The `to_str()` method prints the class name, the binary operation, and the numeric values of the operands.
"""
class BinaryExp(Expression):
    def __init__(self, expr1: Expression, expr2: Expression, operation: str) -> None:
        self.expr1 = expr1
        self.expr2 = expr2
        self.operation = operation
        
    def eval(self):
        value1 = self.expr1.eval()
        value2 = self.expr2.eval()
        
        if isinstance(value1, tuple):
            value1 = value1[0]
        if isinstance(value2, tuple):
            value2 = value2[0]
        
        if value1.type == ValueTypes.NUMBER and value2.type == ValueTypes.NUMBER:
            n1 = value1.value
            n2 = value2.value

            match self.operation:
                case '+':
                    return ValueTypes.NumberValue( n1 + n2 )
                case '-':
                    return ValueTypes.NumberValue( n1 - n2 )
                case '/':
                    return ValueTypes.NumberValue( n1 / n2 )
                case '*':
                    return ValueTypes.NumberValue( n1 * n2 )
                case '%':
                    return ValueTypes.NumberValue( n1 % n2 )
                case _:
                    BaseError.NOT_SUPORTED_NUMBER_OPERATION(self.operation)

        elif value1.type == ValueTypes.NUMBER and value2.type == ValueTypes.STRING:
            n1 = value1.value
            n2 = value2.value

            match self.operation:
                case '*':
                    return ValueTypes.NumberValue( n1 * n2 )
                case _:
                    BaseError.NOT_SUPORTED_NUMBER_OPERATION(self.operation)
                
        elif value1.type == ValueTypes.STRING and value2.type == ValueTypes.NUMBER:
            n1 = value1.value
            n2 = value2.value

            match self.operation:
                case '*':
                    return ValueTypes.StringValue( n1 * n2 )
                case _:
                    BaseError.NOT_SUPORTED_STRING_OPERATION(self.operation)

        elif value1.type == ValueTypes.STRING and value2.type == ValueTypes.STRING:
            n1 = value1.value
            n2 = value2.value

            match self.operation:
                case '+':
                    return ValueTypes.StringValue( n1 + n2 )
                case _:
                    BaseError.NOT_SUPORTED_STRING_OPERATION(self.operation)

        else:
            BaseError.NOT_SUPORTED_BINARY_TYPES(value1.type, value2.type, self.operation)

            
    def to_str(self):
        print( self.__class__.__name__,self.operation, self.expr1.eval().value, self.expr2.eval().value)
                

"""
Represents a variable expression in the program.

The `VariableExp` class represents a variable expression that evaluates to a single numeric value. It holds the name of the variable as a string.

The `eval()` method returns the numeric value of the variable by looking it up in the `Variables` object. If the variable is not found, it prints an error message and exits the program.

The `to_str()` method returns the name of the variable as a string.
"""
class VariableExp(Expression):
    def __init__(self, name) -> None:
          self.name = name

    def eval(self):
        if not Variables.is_exists(self.name): 
             BaseError.VARIABLE_NOT_FOUND(self.name)
        return Variables.get(self.name)
    
    def to_str(self):
        return f'{self.name}'
    
