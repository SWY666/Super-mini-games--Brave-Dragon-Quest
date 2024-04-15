import pygame
SKILL1 = ('./素材/技0.png','./素材/技1.png','./素材/技2.png','./素材/技3.png','./素材/技4.png')
DEADGRAGON = (pygame.image.load('./素材/男 人 死.png'), pygame.image.load('./素材/男 人 死.png'))
for x in DEADGRAGON:
    x.set_colorkey((255, 255, 255))


class Man():
    def __init__(self):
        self.state = '站立'
        self.cache = pygame.image.load("./素材/战立.png").convert()
        self.w = 150
        self.h = 150
        self.axis = [50, 450]
        self.rectsize = (30, 70)
        self.hp = 1000
        self.time = 0
        self.jumplist = [-81,-64,-49,-36,-25,-16,-9,-4,-1,0,0,1,4,9,16,25,36,49,64,81]
        self.jumplist = [-x for x in range(29,0,-1)]+[-1,-1,-1,0,0,1,1,1]+[x for x in range(30)]
        self.isjump = False
        self.cal = 0
        self.thre = 2
        self.speed = 5
        self.skilling = False
        self.skill_time = 0
        self.skill_order = 0
        self.DEAD = False

    def jump(self):
        #跳
        # print(f"????{self.state}")
        if self.state == "站立":
            if self.isjump:
                pass
            else:
                self.isjump = True
                self.up()
        # elif self.state == "左移":
        #     print("左跳")
        # elif self.state == "右移":
        #     print("右跳")

    def up(self):
        self.axis[1] += self.jumplist[self.time]
        self.time +=1
        if self.time == len(self.jumplist):
            self.state = "站立"
            self.time = 0
            self.isjump = False

    def left(self):
        #左移
        if self.state == "站立":
            self.axis[0] += self.speed

    def right(self):
        #右移
        if self.state == "站立":
            self.axis[0] -= self.speed

    def skill1(self):
        if self.skilling:
            self.skill_time +=1
            if self.skill_time == 4:
                self.skill_time = 0
                self.skill_order+=1
                if self.skill_order == len(SKILL1):
                    self.skill_order, self.skill_time = 0, 0
                    self.cache = pygame.image.load("./素材/战立.png").convert()
                    self.skilling = False
                else:
                    self.cache = pygame.image.load(SKILL1[self.skill_order]).convert()

    def checkboom(self, boss):
        pass
        #和boss的检测碰撞

    def behit(self):
        pass
        #受击

    def earthhit(self):
        pass
        #着地检测

    def attack(self):
        pass
        #普通攻击

    def wallhit(self):
        if self.axis[0] < 0:
            self.axis[0] = 0
        if self.axis[0] > 843:
            self.axis[0] = 843
        pass
        #弹墙检测

    def donothing(self):
        self.skill1()
        if self.isjump:
            self.up()
        # self.cal+=1
        self.state = "站立"

    @property
    def getaxis(self):
        # print(f"#####################################{self.state}")
        return self.axis


class DeadMan():
    def __init__(self, x,  y, speed):
        self.x = int(x)
        self.y = int(y)
        self.w = 195
        self.h = 193
        self.axis = [self.x, self.y]
        self.order = 0
        self.time = 0
        self.img = DEADGRAGON[self.order]
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
                self.img = DEADGRAGON[1]
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