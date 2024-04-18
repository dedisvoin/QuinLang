from source.VariablesFunct import Variables, ValueTypes
from source.Errors import BaseError

class Statement:
    def exec(self):
        ...


class Statements:
    """
    Represents an assignment statement that creates a new variable.
    
    The `AsignetNewVar` class encapsulates an assignment statement that sets the value of a new variable to the result of an expression.
    
    Args:
        name (str): The name of the variable to be assigned.
        expr: The expression to be evaluated and assigned to the variable.
        changed (bool): Whether the variable is a new variable that has been changed.
    
    Methods:
        exec(): Evaluates the expression and sets the value of the variable using the `Variables.set()` function.
    """
    class AsignetNewVar:
        def __init__(self, name: str, expr, changed=False) -> None:
            self.name = name
            self.expr = expr
            self.changed = changed
            self.exec()
            
        
        def exec(self):
            result = self.expr.eval()
            
            if isinstance(result, tuple):
                result = result[0]

            

            if self.changed:
                Variables.set(self.name, result, True)
            else:
                Variables.set(self.name, result, False)
            

    class AsignetBaseNewVar:
        def __init__(self, name: str, changed=False) -> None:
            self.name = name
            self.changed = changed
        
        def exec(self):
            if self.changed:
                Variables.set(self.name, ValueTypes.NoneValue(), True)
            else:
                Variables.set(self.name, ValueTypes.NoneValue(), False)

    """
    Represents an assignment statement in the program.
    
    The `Asignet` class encapsulates an assignment statement, which sets the value of a variable to the result of an expression.
    
    Args:
        name (str): The name of the variable to be assigned.
        expr: The expression to be evaluated and assigned to the variable.
    
    Methods:
        exec(): Evaluates the expression and sets the value of the variable using the `Variables.set()` function. If the variable already exists, it updates the value. If the variable does not exist or the type is incorrect, it prints an error message and exits.
    """
    class Asignet:
        def __init__(self, name: str, expr, index=None) -> None:
            self.name = name
            self.expr = expr
            self.index = index
        
        def exec(self):
            result = self.expr.eval()
            if Variables.is_exists(self.name):
                var_type = Variables.get_type(self.name)
                if var_type:
                    if self.index is None:
                        Variables.set(self.name, result, True)
                    else:
                        Variables.set(self.name, result, True, self.index)
                else:
                    BaseError.NOT_CHAINGABLE_VAR(self.name)
            else:
                BaseError.VARIABLE_NOT_FOUND(self.name)
                        
    class Function:
        def __init__(self, expr: str):
            self.expr = expr

        def eval(self):
            self.expr.eval()

        def to_str(self):
            return 'Funtion state'
