from source.VariablesFunct import Variables

"""
Represents an assignment statement in the program.

The `Asignet` class encapsulates an assignment statement, which sets the value of a variable to the result of an expression.

Args:
    name (str): The name of the variable to be assigned.
    expr: The expression to be evaluated and assigned to the variable.

Attributes:
    name (str): The name of the variable to be assigned.
    expr: The expression to be evaluated and assigned to the variable.

Methods:
    exec(): Evaluates the expression and sets the value of the variable using the `Variables.set()` function.
"""
class Statements:
    class Asignet:
        def __init__(self, name: str, expr) -> None:
            self.name = name
            self.expr = expr
        
        def exec(self):
            result = self.expr.eval()
            Variables.set(self.name, result)
