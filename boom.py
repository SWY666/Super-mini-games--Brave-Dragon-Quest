import pygame


BOOMS = (pygame.image.load('./素材/地爆1.png'),pygame.image.load('./素材/地爆2.png'),pygame.image.load('./素材/地爆3.png'),pygame.image.load('./素材/地爆4.png')
         ,pygame.image.load('./素材/地爆5.png'),pygame.image.load('./素材/地爆6.png'),pygame.image.load('./素材/地爆7.png'),pygame.image.load('./素材/地爆8.png'))
for i in BOOMS:
    i.set_colorkey((255, 255, 255))



class Boom():
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.w = 120
        self.h = 68
        self.axis = [self.x, self.y]
        self.order = 0
        self.time = 0
        self.img = BOOMS[self.order]
        self.damage = 1200
        self.over = False


    def move(self):
        self.time += 1
        if self.time % 7 == 0:
            self.order += 1
            if self.order >= len(BOOMS):
                self.over = True
            else:
                self.img = BOOMS[self.order]

    @property
    def hitcal(self):
        return self.over