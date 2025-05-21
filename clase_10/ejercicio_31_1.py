import random
class die():
    def __init__(self, cant_caras = 6):
        self.caras = cant_caras
    def roll_die(self,cant_tiros):
        for tiro in range(cant_tiros):
            print(random.randint(1,self.caras))
print("dado 6")
dado_6 = die()
dado_6.roll_die(10)
print("dado 10")
dado_10 = die(10)
dado_10.roll_die(10)
print("dado 20")
dado_20 = die(20)
dado_20.roll_die(10)
