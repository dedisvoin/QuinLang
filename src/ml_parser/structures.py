from src.ml_parser.value_mchine import Values

class StructureConstructs:
    structs = {}

    @classmethod
    def set_construct(self, name, args):
        self.structs[name] = args

    @classmethod
    def get(self, name):
        return self.structs[name]

class Structure:
    def __init__(self, _name, _values) -> None:
        self.__values = _values
        self.__name = _name
    
    def get_type(self):
        return 'struc'
    
    def get_values(self):
        return self.__values
    
    def get_value(self):
        values = []
        for val in self.__values:
            values.append([val[0],val[1].get_value()])
        return values




    