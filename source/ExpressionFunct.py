class ConditionExp:
    def __init__(self, expr1, expr2, operation: str) -> None:
        self.expr1 = expr1
        self.expr2 = expr2
        self.operation = operation
        
    
    def eval(self) :
        value1 = self.expr1.eval()
        value2 = self.expr2.eval()

        n1 = value1.asDouble()
        n2 = value2.asDouble()
        
        match self.operation:
            case '==':
                return NumberVal( 1 if n1 == n2 else 0 )
            case '<':
                return NumberVal( 1 if n1 < n2 else 0 )
            case '>':
                return NumberVal( 1 if n1 > n2 else 0 )
            case '<>':
                return NumberVal( 1 if n1 != n2 else 0 )
            case 'or':
                return NumberVal( 1 if bool(n1) or bool(n2) else 0 )
            case 'and':
                return NumberVal( 1 if bool(n1) and bool(n2) else 0 )