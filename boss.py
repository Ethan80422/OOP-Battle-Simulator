from enemy import enemy
import random

class dragon(enemy):
    
    #def __init__(self,name):
    #    super().__init(self, name)
    #    self.attack_power= self.power(1)
    #    self.health=1
    def __init__(self, name):
        super().__init__(name)
        f=random.randint(0,1)
        if f==1:
            f=10000000
        self.attack_power= f
        #self.attack_power= 100000
        self.health=1
        #self.color = color
    