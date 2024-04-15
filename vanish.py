import pygame

VANISH = (pygame.image.load('./素材/消散1.png'),pygame.image.load('./素材/消散2.png'),pygame.image.load('./素材/消散3.png'),pygame.image.load('./素材/消散4.png'))
for x in VANISH:
    x.set_colorkey((255, 255, 255))

class hanabi():
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.w = 100
        self.h = 98
        self.axis = [self.x, self.y]
        self.order = 0
        self.time = 0
        self.img = VANISH[self.order]
        self.over = False



    def move(self):
        self.time+=1
        if self.time == 6:
            self.order +=1
            if self.order == 4:
                self.over = True
            else:
                self.img = VANISH[self.order]
                self.time = 0

    @property
    def hitcal(self):
        if self.x > 1000:
            return True
        else:return False