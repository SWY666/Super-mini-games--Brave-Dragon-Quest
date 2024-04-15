import pygame

FRIE = (pygame.image.load('./素材/火1.png'), pygame.image.load('./素材/火2.png'), pygame.image.load('./素材/火3.png'))
for x in FRIE:
    x.set_colorkey((255, 255, 255))



class fire():
    def __init__(self,x, y, speed):
        self.x = x+125
        self.y = y+50
        self.w = 120
        self.h = 68
        self.axis = [self.x, self.y]
        self.speed = speed
        self.order = 0
        self.time = 0
        self.img = FRIE[self.order]
        self.damage = 1200



    def move(self):
        self.axis[0] += self.speed
        self.time+=1
        if self.time == 10:
            self.order +=1
            if self.order == 3:
                self.order = 0
            self.img = FRIE[self.order]
            self.time = 0

    @property
    def hitcal(self):
        if self.x > 1000:
            return True
        else:return False