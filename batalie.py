class batalie:
    def lupta(self, antrenor1, antrenor2):
        while True:
            pokemon1 = antrenor1.alege_pokemon()
            pokemon2 = antrenor2.alege_pokemon()
            print(pokemon1.nume, " vs ",pokemon2.nume)
            print ("Pokemon1: ", pokemon1.viata)
            print ("Pokemon2: ", pokemon2.viata)            
            pokemon1.ataca(pokemon2)
            print ("Pokemon1: ", pokemon1.viata)
            print ("Pokemon2: ", pokemon2.viata)
            if not pokemon2.este_viu():
                break    
            pokemon2.ataca(pokemon1)
            print ("Pokemon1: ", pokemon1.viata)
            print ("Pokemon2: ", pokemon2.viata)
            if not pokemon1.este_viu():
                break        

    
    def test():
        pass