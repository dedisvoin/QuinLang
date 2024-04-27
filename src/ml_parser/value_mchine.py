from typing import Any

class ValueTypes:
    INT = 'int'
    STR = 'str'
    FLOAT = 'float'
    BOOL = 'bool'
    FUNCT = 'funct'
    LIST = 'list'
    NONE = 'none'
    FN = 'fn'


class BasicValue:
    def __init__(self, _type: ValueTypes, _value: Any = 'none') -> None:
        self.__type = _type
        self.__value = _value

    def get_value(self) -> Any:
        return self.__value
    
    def get_type(self) -> ValueTypes:
        return self.__type
    
    def eval(self) -> Any:
        return self
    

class Values:
    class ValInt(BasicValue):
        def __init__(self, _value: int) -> None:
            super().__init__(ValueTypes.INT, _value)
    
    class ValFloat(BasicValue):
        def __init__(self, _value: float) -> None:
            super().__init__(ValueTypes.FLOAT, _value)
    
    class ValStr(BasicValue):
        def __init__(self, _value: str) -> None:
            super().__init__(ValueTypes.STR, _value)
    
    class ValBool(BasicValue):
        def __init__(self, _value: bool) -> None:
            super().__init__(ValueTypes.BOOL, _value)

    class ValList(BasicValue):
        def __init__(self, _value: list) -> None:
            super().__init__(ValueTypes.LIST, _value)

    class ValFn(BasicValue):
        def __init__(self, _fn) -> None:
            super().__init__(ValueTypes.LIST, _fn)

    class ValNone(BasicValue):
        def __init__(self) -> None:
            super().__init__(ValueTypes.NONE)
    
