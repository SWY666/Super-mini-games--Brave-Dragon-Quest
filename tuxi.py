import pygame
from math import sqrt

# FRIE = ('./素材/吐息1.png', './素材/吐息2.png', './素材/吐息3.png')
FRIE = (pygame.image.load('./素材/吐息1.png'), pygame.image.load('./素材/吐息2.png'), pygame.image.load('./素材/吐息3.png'))
for x in FRIE:
    x.set_colorkey((255, 255, 255))



class tuxi():
    def __init__(self,x, y, speed, x_, y_):
        self.x = int(x)
        self.y = int(y)
        self.w = 195
        self.h = 193
        self.axis = [self.x, self.y]
        self.order = 0
        self.time = 0
        self.img = FRIE[self.order]
        self.x_ = x - x_
        self.y_ = y - y_
        self.xp = self.x_ * speed / (sqrt(self.x_ ** 2 + self.y_ ** 2))
        self.yp = self.y_ * speed / (sqrt(self.x_ ** 2 + self.y_ ** 2))


    def move(self):
        self.axis[0] -= self.xp
        self.axis[1] -= self.yp
        self.time+=1
        if self.time == 10:
            self.order +=1
            if self.order == 3:
                self.order = 0
            self.img = FRIE[self.order]
            self.time = 0

    @property
    def hitcal(self):
        if self.x < 0 or self.y < 0:
            return True
        else:return False