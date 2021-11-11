class Utensils:
    def __init__(self,material):
        self.material=material
    def use(self):
        print("USed in kitchen and material is"+self.material)
class Plate(Utensils):
    def __init(self,material):
        Utensils.__init__(self,material)
p=Plate('plate')
p.use()
class Spoon(Utensils):
    def __init__(self, material):
        Utensils.__init__(self,material)
    def use(self):
        print("used to eat and is made of"+self.material)
s=Spoon('steel')
s.use()
class Bowl(Utensils):
    def __init__(self, material):
        super().__init__(material)
    def use(self):
        print('used to store food and is made of '+self.material)
b=Bowl("bowl")
b.use()


    