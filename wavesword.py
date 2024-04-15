import pygame

ICE = (pygame.image.load('./素材/波4.png'), pygame.image.load('./素材/波5.png'), pygame.image.load('./素材/波6.png'))
# ICE = (pygame.image.load('./素材/冰弹1.png'),pygame.image.load('./素材/冰弹2.png'),pygame.image.load('./素材/冰弹3.png'))
for x in ICE:
    x.set_colorkey((255, 255, 255))


class wf():
    def __init__(self,x, y, speed):
        self.x = x+125
        self.y = y+50
        self.w = 120
        self.h = 68
        self.axis = [self.x, self.y]
        self.speed = speed
        self.order = 0
        self.time = 0
        self.img = ICE[self.order]
        self.damage = 1500



    def move(self):
        self.axis[0] += self.speed
        self.time+=1
        if self.time == 10:
            self.order +=1
            if self.order == 3:
                self.order = 0
            self.img = ICE[self.order]
            self.time = 0

    @property
    def hitcal(self):
        if self.x > 1000:
            return True
        else:return False