from pokemon import pokemon
from antrenor import antrenor
from batalie import batalie

Charmender = pokemon("Charmender", "Foc", "50", "10")
Charmender.testare()
Bulbasaur = pokemon("Bulbasaur", "Pamant", "60", "8")
Bulbasaur.testare()
Squirtle = pokemon("Squirtle", "Apa", "40", "14")
Squirtle.testare()
Gigel = antrenor("Gigel", [Bulbasaur.nume, Charmender.nume, Squirtle.nume])
print(Gigel.pokemoni)