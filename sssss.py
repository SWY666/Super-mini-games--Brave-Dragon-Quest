import pygame
import random


MOVE = ('./素材/飞龙.png', './素材/飞龙2.png')
MOVERAGE = ('./素材/飞龙怒.png', './素材/飞龙怒2.png')
POWER = ('./素材/蓄能1.png','./素材/蓄能1.png','./素材/蓄能2.png','./素材/蓄能2.png','./素材/飞龙.png')
POWERRAGE = ('./素材/怒蓄能1.png','./素材/怒蓄能1.png','./素材/怒蓄能2.png','./素材/飞龙怒.png','./素材/飞龙怒.png')
DEADGRAGON = ('./素材/飞龙死1.png', './素材/飞龙死2.png')


def listmake(x0, y0, x1, y1, speed):
    steps = int(max(abs(x0-x1),abs(y0-y1))/speed) + 1
    # print(max(abs(x0-x1),abs(y0-y1)))
    stepx = (x0 - x1)/steps
    stepy = (y0 - y1)/steps
    return steps, stepx, stepy

class Dragon():
    def __init__(self):
        self.w = 417
        self.h = 343
        self.DEAD = False
        self.MOVE = False
        self.SKILL = False
        self.state = '呆住'
        self.op = False
        self.cache = pygame.image.load("./素材/飞龙.png").convert()
        self.axis = [900, 50]
        self.hp = 10000
        self.next = [0, 0]
        self.speed = 3
        self.attack = 300
        self.eventlist = "技能"
        self.time2 = 0
        self.order = 0
        self.emit = False
        self.POWER = POWER
        self.raged = False
        self.normal = './素材/飞龙.png'
        self.rageskillcount = 0
        self.moveorder = 0

    def prepare(self):
        if self.raged:
            if self.eventlist == "技能":
                self.rageskillcount += 1
                if self.rageskillcount < 3:
                    return "技能"
                else:
                    self.rageskillcount = 0
                    return "移动"
            if self.eventlist == "移动":
                return "技能"
        else:
            if self.eventlist == "技能":
                return "移动"
            if self.eventlist == "移动":
                return "技能"

    def move(self):
        self.axis[0] += self.stepx
        self.axis[1] += self.stepy
        self.time += 1
        if self.time == self.steps:
            self.MOVE = False

    def dead(self):
        pass

    def skill(self):
        self.time2 +=1
        if self.time2 == 10:
            self.time2 = 0
            self.order += 1
            if self.order == 3:
                self.emit = True
            if self.order == len(POWER):
                self.order, self.time2 = 0, 0
                self.cache = pygame.image.load(self.normal).convert()
                self.SKILL = False
            else:
                self.cache = pygame.image.load(self.POWER[self.order]).convert()

    def judge(self, axis):
        if self.DEAD:
            self.dead()
        else:
            if self.MOVE or self.SKILL:
                if self.MOVE:
                    self.move()
                if self.SKILL:
                    self.skill()
            else:
                judgement = self.prepare()
                if judgement == "移动":
                    self.eventlist = "移动"
                    if self.axis[1] > 350:
                        yn = random.randint(0, 200)
                    else:
                        yn = random.randint(351, 400)
                    xn = random.randint(800, 1000)
                    self.steps, self.stepx, self.stepy = listmake(xn, yn, self.axis[0], self.axis[1], self.speed)
                    # print(self.steps, xn, yn, self.axis[0], self.axis[1])
                    self.time = 0
                    self.MOVE = True
                    self.move()
                if judgement == "技能":
                    self.eventlist = "技能"
                    self.SKILL = True
                    self.skill()

    def howl(self):
        if self.emit:
            self.emit = False
            return (True, self.axis[0], self.axis[1], self.speed*2)

        else:return (False, False)

    def rage(self):
        if self.raged:
            pass
        else:
            self.raged = True
            self.speed = 5
            self.POWER = POWERRAGE
            self.normal = './素材/飞龙怒2.png'

class Dead_Dragon():
    def __init__(self, x,  y, speed):
        self.x = int(x)
        self.y = int(y)
        self.w = 195
        self.h = 193
        self.axis = [self.x, self.y]
        self.order = 0
        self.time = 0
        self.img = pygame.image.load(DEADGRAGON[self.order])
        self.speed = speed


    def move(self):
        self.time += 1
        if self.time % 10 == 0:
            self.speed = -self.speed
            if self.time <= 80:
                self.axis[1] += self.speed
                self.axis[0] += self.speed
            else:
                self.speed = abs(self.speed)
                self.img = pygame.image.load(DEADGRAGON[1])
                self.axis[1] += self.speed*3


    def setaxis(self,x, y, speed):
        self.x = int(x)
        self.y = int(y)
        self.axis = [self.x, self.y]
        self.speed = speed


    @property
    def hitcal(self):
        if self.axis[1] > 650 and self.time > 80:
            return True
        else:return False






a = f"123456\n"
print(a+"ssss")