class batalie:
    def lupta(self, antrenor1, antrenor2):
        pokemon1 = antrenor1.alege_pokemon()
        pokemon2 = antrenor2.alege_pokemon()
        while True:
            print(pokemon1.nume, " vs ",pokemon2.nume)
            print ("Pokemon1: ", pokemon1.nume, " ", pokemon1.viata)
            print ("Pokemon2: ", pokemon2.nume, " ", pokemon2.viata)          
            pokemon1.ataca(pokemon2)
            print ("Pokemon1: ", pokemon1.nume, " ", pokemon1.viata)
            print ("Pokemon2: ", pokemon2.nume, " ", pokemon2.viata)
            if not pokemon2.este_viu():
                print (pokemon2.nume, " A murit!")
                for i in range(len(antrenor2.pokemoni)):
                    if not antrenor2.pokemoni[i].este_viu():
                        antrenor2.pokemoni.pop(i)
                if not antrenor2.are_pokemoni_vii():
                    print("antrenor 2 nu mai are pokemoni")
                    break
                pokemon2 = antrenor2.alege_pokemon()                   
            pokemon2.ataca(pokemon1)
            print ("Pokemon1: ", pokemon1.nume, " ", pokemon1.viata)
            print ("Pokemon2: ", pokemon2.nume, " ", pokemon2.viata)
            if not pokemon1.este_viu():
                print (pokemon1.nume, " A murit!")
                for i in range(len(antrenor1.pokemoni)):
                    if not antrenor1.pokemoni[i].este_viu():
                        antrenor1.pokemoni.pop(i)
                if not antrenor1.are_pokemoni_vii():
                    print("antrenor 1 nu mai are pokemoni")
                    break
                pokemon1 = antrenor1.alege_pokemon()   
                     

    
    def test():
        pass