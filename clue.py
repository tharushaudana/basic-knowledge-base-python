from utils.symbol import Symbol
from utils.operators import And, Or, Not, Implication, DoubleImplication
from utils.model_check import ModelCheck

mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons

def check_knowledge(model_check):
    for symbol in symbols:
        if model_check.check(symbol):
            print(f"{symbol}: YES")
        elif not model_check.check(Not(symbol)):
            print(f"{symbol}: MAYBE")

################ [KNOWLEDGE] ################

knowledge = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench)
)

knowledge.add(Not(mustard))
knowledge.add(Not(kitchen))
knowledge.add(Not(revolver))

knowledge.add(Or(
    Not(scarlet), Not(library), Not(wrench)
))

knowledge.add(Not(plum))
knowledge.add(Not(ballroom))

#print(knowledge.formula())

#############################################

model_check = ModelCheck(knowledge)
model_check.fit()

check_knowledge(model_check)