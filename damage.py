class Damage():
    def __init__(self,x, y, speed,damage):
        self.x = x
        self.y = y
        self.axis = [self.x, self.y]
        self.speed = speed
        self.time = 0
        self.vanish = False
        self.damage = damage



    def move(self):
        self.axis[1] -= self.speed
        self.time+=1
        if self.time == 25:
            self.vanish = True

    @property
    def hitcal(self):
        return self.vanish