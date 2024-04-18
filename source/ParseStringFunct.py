from copy import copy

"""
Provides a class `StringParse` that allows parsing a string with placeholders and replacing them with corresponding values.

The `StringParse` class has the following methods:

- `__init__(self, string, values)`: Initializes the `StringParse` object with the input `string` and a dictionary of `values` to be used for replacement.
- `parse(self)`: Parses the input `string` and replaces the placeholders with the corresponding values from the `values` dictionary.
- `parse_expression(self)`: Helper method used by `parse()` to extract the name of the placeholder from the input `string`.
"""
class StringParse:
    def __init__(self, string, values) -> None:
        self.string = string
        self.parsed_string = copy(self.string)
        self.values = values
        self.pos = 0

    def parse(self):
        while self.pos<len(self.string):
            char = self.string[self.pos]
            if char == '{':
                
                self.parse_expression()
            else:
                self.pos += 1

    def parse_expression(self):
        char = self.string[self.pos]
        name = ''
        while char != '}':
            self.pos += 1
            char = self.string[self.pos]
            name+=char

        name = name[:-1]


        values = {}
        for name in self.values:
            values[name] = self.values[name][0].value

        self.parsed_string = self.string.format(**values)


if __name__ == '__main__':

    sp = StringParse('my name is {name} i am {age}', {'name':'hello', 'age':16})
    sp.parse()
    print(sp.parsed_string)
