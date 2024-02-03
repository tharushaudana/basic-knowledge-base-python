from .operator import Operator
from ..symbol import Symbol

class Implication(Operator):
    def __init__(self, item_left, item_right):
        super().__init__()
        self.item_left = item_left
        self.item_right = item_right

    def symbols(self):
        for i in [self.item_left, self.item_right]:
            if type(i) == Symbol:
                yield i.name
            else:
                for s in i.symbols():
                    yield s

    def eval(self, cb):
        return not(self._evaluate_item(self.item_left, cb) and not self._evaluate_item(self.item_right, cb))
    
    def formula(self):
        f = []

        for i in [self.item_left, self.item_right]:
            if type(i) == Symbol:
                f.append(i.name)
            else:
                f.append(f"({i.formula()})")

        return " => ".join(f)