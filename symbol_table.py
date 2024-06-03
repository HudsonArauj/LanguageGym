class SymbolTable:
    def __init__(self):
        self.table = {}

    def get(self, name):
        if name in self.table:
            return self.table[name]
        raise Exception(f'Variable "{name}" not defined')

    def set(self, name, value):
        self.table[name] = value
