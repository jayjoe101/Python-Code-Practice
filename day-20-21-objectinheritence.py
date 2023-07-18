class Animal():

    def __init__(self):
        self.alive = True

    def breathe(self):
        print('breath in breath out')

class Fish(Animal): # defines inheritents relationship (fish inherits animal)
    def __init__(self):
        super().__init__() # inherets the attributes in the constructor of animal  

    def breathe(self):
        super().breathe() # brings the breathe function from animal to fish but also adds another print
        print('... but under water')