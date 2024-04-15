import pygame

FRIE = ('./素材/冰弹1.png', './素材/冰弹2.png', './素材/冰弹3.png')
ICE = (pygame.image.load('./素材/冰弹1.png'),pygame.image.load('./素材/冰弹2.png'),pygame.image.load('./素材/冰弹3.png'))
for x in ICE:
    x.set_colorkey((255, 255, 255))



class Ice():
    def __init__(self,x, y, speed):
        self.x = x+125
        self.y = y+50
        self.w = 100
        self.h = 100
        self.axis = [self.x, self.y]
        self.speed = speed
        self.order = 0
        self.time = 0
        self.img = ICE[self.order]
        self.damage = 1500



    def move(self):
        self.axis[0] += self.speed * 1.5
        self.axis[1] += self.speed
        self.time+=1
        if self.time == 10:
            self.order +=1
            if self.order == 3:
                self.order = 0
            self.img = ICE[self.order]
            self.time = 0

    @property
    def hitcal(self):
        if self.x > 1000 or self.y > 650:
            return True
        else:return False