from .symbol import Symbol

class ModelCheck:
    def __init__(self, knowledge):
        self.kb = knowledge
        self.situations = [] # situation(s) that 'Knowledge Base' is True

    def _itr_truth_table(self, params, cb, n=1):
        ### [Recursive approch]

        cb(params)

        if all(v for v in params): return

        for i in range(len(params)):
            if n % pow(2, i) == 0:
                params[i] = not params[i]

        n += 1

        self._itr_truth_table(params, cb, n)

        '''
        ### [Looping approch]

        cb(params)

        for n in range(1, pow(2, len(params)) + 1):
            for i in range(len(params)):
                if n % pow(2, i) == 0:
                    params[i] = not params[i]
            cb(params)
        '''

    def _evaluate_kb(self, situation:dict):
        if (self.kb.eval(lambda s: situation[s.name])): 
            self.situations.append(situation)
            #print("#"*25)
            #for k, v in situation.items(): print(k.name, ":", v)

    def fit(self):
        symbols = list(set(self.kb.symbols()))
        initial_params = [False for _ in range(len(symbols))] # initialy, all are False
        self._itr_truth_table(initial_params, lambda params: self._evaluate_kb({k: v for k, v in zip(symbols, params)}))
        #print(len(self.situations))

    def check(self, query):    
        if len(self.situations) == 0: return False

        if type(query) == Symbol:
            return all(situation[query.name] for situation in self.situations)
        
        return all(query.eval(lambda s: situation[s.name]) for situation in self.situations)