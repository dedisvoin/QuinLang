from source.VariablesFunct import Variables

class Statements:
    class Asignet:
        def __init__(self, name: str, expr) -> None:
            self.name = name
            self.expr = expr
        
        def exec(self):
            result = self.expr.eval()
            Variables.set(self.name, result)
