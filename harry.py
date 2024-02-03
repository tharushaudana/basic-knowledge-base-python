from utils.symbol import Symbol
from utils.operators import And, Or, Not, Implication, DoubleImplication
from utils.model_check import ModelCheck

rain = Symbol("rain") # it's a rainy day
hagrid = Symbol("hagrid") # Harry visited Hagrid
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore

knowledge = And(
    Implication(Not(rain), hagrid), 
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

#print(knowledge.formula())

model_check = ModelCheck(knowledge)
model_check.fit()

print(model_check.check(rain))