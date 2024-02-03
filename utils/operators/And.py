from shlex import join
from .operator import Operator
from ..symbol import Symbol

class And(Operator):
    def __init__(self, *items):
        super().__init__()
        self.items = list(items)

    def add(self, item):
        self.items.append(item)

    def symbols(self):
        for i in self.items:
            if type(i) == Symbol:
                yield i.name
            else:
                for s in i.symbols():
                    yield s

    def eval(self, cb):
        for i in self.items:
            if not self._evaluate_item(i, cb): return False
        return True
    
    def formula(self):
        f = []

        for i in self.items:
            if type(i) == Symbol:
                f.append(i.name)
            else:
                f.append(f"({i.formula()})")

        return " ∧ ".join(f)