class Magnit:
    def __init__(self, cola, tvorog):
        self.drink = cola
        self.milk_prod = tvorog
    def napitok(self):
        print("napitok of in class Magnit")

    def milk(self):
        print("milk of in class Magnit")

    def frukt (self):
        print("frukt of in class Magnit")


class family_magnit(Magnit):
    def __init__(self, cola , tvorog, banan ):
        super().__init__(cola, tvorog)
        self.banan = banan

    def frukt(self):
        print("frukt of in class family magnit")


class Magnit_y_home(Magnit):
    def __init__(self, napitok="default_napitok", milk="default_milk" ):
        super().__init__(napitok, milk)

    def chokolaters(self):
        print("chokolaters of in class Magnit_y_home")

    def ice_cream(self):
        print("ice_cream of in class Magnit_y_home")


a = Magnit("cola_value", "tvorog_value")
b = family_magnit("cola_value", "tvorog_value","banan_bvalue")
c = Magnit_y_home()


a.napitok()
a.milk()
a.frukt()

b.napitok()
b.milk()
b.frukt()


c.napitok()
c.milk()
c.frukt()
c.chokolaters()
c.ice_cream()