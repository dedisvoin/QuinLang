from source.VariablesFunct import *



class Expression:
    def __init__(self) -> None:
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
        match self.operation:
            case '-':
                return  ValueTypes.NumberValue(-self.expr.eval())
            case _:
                return  ValueTypes.NumberValue(self.expr.eval())
            
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
             print(self.name, 'not found') 
             exit(-1)
        return Variables.get(self.name)
    
    def to_str(self):
        return f'{self.name}'