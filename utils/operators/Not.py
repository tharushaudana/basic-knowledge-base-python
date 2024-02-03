from .operator import Operator
from ..symbol import Symbol

class Not(Operator):
    def __init__(self, item):
        super().__init__()
        self.item = item

    def symbols(self):
        if type(self.item) == Symbol:
            yield self.item.name
        else:
            for s in self.item.symbols():
                yield s

    def eval(self, cb):
        return not self._evaluate_item(self.item, cb)
    
    def formula(self):
        if type(self.item) == Symbol:
            return f"¬{self.item.name}"
        else:
            return f"¬({self.item.formula()})"