class Odam:
    def __init__(ism, familya, yosh):
        self.ism = ism
        self.familya = familya
        self.yosh = yosh
    def shifr(self):
        print(self.ism, self.familya, self.yosh)
o1 = Odam("Ubaydullo", "Jumayev", 21 )
o2 = Odam("Ozodbek", "Turobov", 14 )


print(o1.shifr())
print(o2.shifr())
