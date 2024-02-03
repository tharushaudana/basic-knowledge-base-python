from utils.symbol import Symbol
from utils.operators import And, Or, Not, Implication, DoubleImplication
from utils.model_check import ModelCheck

ambagamuwa = Symbol("Ambagamuwa") # Ambagamuwa saying truth
dhambagamuwa = Symbol("Dhambagamuwa") # Dhambagamuwa saying truth
narangamuwa = Symbol("Narangamuwa") # Narangamuwa saying truth
keselgamuwa = Symbol("Keselgamuwa") # Keselgamuwa saying truth
delgamuwa = Symbol("Delgamuwa") # Delgamuwa saying truth
charactors = [ambagamuwa, dhambagamuwa, narangamuwa, keselgamuwa, delgamuwa]

knowledge = And(
    Or(ambagamuwa, dhambagamuwa, narangamuwa, keselgamuwa, delgamuwa)
)

for c in charactors: 
    k = Or()
    for r in range(1, 6):
        k.add(Symbol(f"{c}Rank{r}"))
    knowledge.add(k)

for c in charactors:
    for r in range(1, 6):
        for r1 in range(1, 6):
            if r != r1:
                knowledge.add(Implication(Symbol(f"{c}Rank{r}"), Not(Symbol(f"{c}Rank{r1}"))))

for c in charactors:
    for r in range(1, 6):
        for c1 in charactors:
            if c1.name != c.name:
                knowledge.add(Implication(Symbol(f"{c}Rank{r}"), Not(Symbol(f"{c1}Rank{r}")))) 


model_check = ModelCheck(knowledge)
model_check.fit()