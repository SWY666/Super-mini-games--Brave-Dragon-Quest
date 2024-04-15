class boss():
    def __init__(self):
        self.state = '站立'
        self.cache = "./素材/战立.png"
        self.axis = [50, 450]
        self.rectsize = (30, 70)
        self.hp = 1000

    def jump(self):
        #跳

    def left(self):
        #左移

    def right(self):
        #右移

    def skill1(self):
        #斩击


    def skill2(self):
        #空爆

    def checkboom(self, boss):
        #和boss的检测碰撞

    def behit(self):
        #受击

    def earthhit(self):
        #着地检测

    def attack(self):
        #普通攻击

    def wallhit(self):
        #弹墙检测