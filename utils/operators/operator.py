from ..symbol import Symbol

class Operator:
    def __init__(self):
        pass

    def _evaluate_item(self, item, cb):
        if type(item) == Symbol: 
            return cb(item)
        else: 
            return item.eval(cb)