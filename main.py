import pygame, sys
from pygame import font
from damage import Damage
from man import Man, DeadMan
from fire import fire
from dragon import Dragon, Dead_Dragon
from tuxi import tuxi
from vanish import hanabi
from wavesword import wf
from ice import Ice
from boom import Boom

CAPBG = (pygame.image.load('./素材/标题界面1.png'), pygame.image.load('./素材/标题界面2.png'))
BG = pygame.image.load('./素材/背景.png')



def isclash(a, b):
    if b.axis[0] <= a.axis[0] <= b.axis[0] + b.w or b.axis[0] <= a.axis[0]+a.w <= b.axis[0] + b.w:
        if b.axis[1] <= a.axis[1] <= b.axis[1] + b.h or b.axis[1] <= a.axis[1]+a.h <= b.axis[1] + b.h:
            return True

    return False

def showhp():
    global dragon
    global man
    text = f"龙的血量:{dragon.hp}/10000   "
    if dragon.raged:
        text += "感受龙的愤怒！！"
    if dragon.DEAD:
        text = "66666666666"
    if man.DEAD:
        text = "oh不！！！"
    hprender = Font.render(text, True, (0,0,0))
    screen.blit(hprender, (10,10))

def showskill():
    text = f"AD左右移动，W跳跃，J火焰剑，K波动斩(仅地面)，L冰枪(仅空中)"
    hprender = Fonts.render(text, True, (0, 0, 0))
    screen.blit(hprender, (10, 40))


def showdm(damage, x, y):
    text = f"命中！！{damage}"
    hprender = Font.render(text, True, (0, 255, 0))
    screen.blit(hprender, (x, y))




pygame.init()
Font = font.SysFont('fangsong',32)
Fonts = font.SysFont('fangsong',20)
screen = pygame.display.set_mode((1200,700))
pygame.display.set_caption("dio的世界")
man = Man()
dragon = Dragon()
deaddragon = Dead_Dragon(0,0,0)
deadman = DeadMan(0,0,0)
fps = 50
fclock = pygame.time.Clock()

fires = []
tuxis = []
hanabis = []
damages = []
boom = []
firecount = 0
frietime = fps/2
canfire = True
end = "等待开始！"
capcount = 0
caporder = 0
deletetuxi = False


while True:
    screen.fill((255, 255, 255))

    if end == "等待开始！":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        pressed_keys = pygame.key.get_pressed()

        screen.blit(CAPBG[caporder], (0, 0))
        capcount += 1
        if capcount > fps/3:
            capcount = 0
            caporder += 1
            if caporder == len(CAPBG):
                caporder = 0

        if pressed_keys[pygame.K_SPACE]:
            end = "战斗中！"

    if end == "战斗中！":
        screen.blit(BG, (0, 0))
        showskill()
        showhp()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    if canfire:
                        man.skilling = True
                        fires.append(fire(man.axis[0], man.axis[1], 7))
                        canfire = False

                if event.key == pygame.K_k:
                    if canfire:
                        if not man.isjump:
                            man.skilling = True
                            fires.append(wf(man.axis[0], man.axis[1], 30))
                            canfire = False

                if event.key == pygame.K_l:
                    if canfire:
                        if man.isjump:
                            man.skilling = True
                            fires.append(Ice(man.axis[0], man.axis[1], 8))
                            canfire = False


        #双方死亡判定
        if dragon.DEAD:
            end = "龙死了"
            deaddragon.setaxis(dragon.axis[0],dragon.axis[1],20)
        elif man.DEAD:
            end = "男 人 死"
            deadman.setaxis(man.axis[0], man.axis[1], 20)

        else:pass

        # 飞龙动作
        screen.blit(dragon.cache, tuple(dragon.axis))
        dragon.judge(man.axis)
        if dragon.howl()[0]:
            tuxis.append(tuxi(dragon.axis[0], dragon.axis[1], dragon.speed * 5, man.axis[0], man.axis[1]))

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            man.jump()
        elif pressed_keys[pygame.K_d]:
            man.left()
        elif pressed_keys[pygame.K_a]:
            man.right()


        # 自动操作
        # 火焰蓄能
        if not canfire:
            firecount += 1
            if firecount == frietime:
                canfire = True
                firecount = 0
        # 火焰移动和消散
        for bullet in fires:
            bullet.move()
            if bullet.hitcal:
                fires.remove(bullet)
            else:
                screen.blit(bullet.img, tuple(bullet.axis))

        for bullet in tuxis:
            bullet.move()
            if isclash(bullet, man):
                man.DEAD = True

            if bullet.axis[1] > 475:
                boom.append(Boom(bullet.axis[0], bullet.axis[1]))
                deletetuxi = True

            if bullet.hitcal:
                deletetuxi = True

            if deletetuxi:
                tuxis.remove(bullet)
            else:
                screen.blit(bullet.img, tuple(bullet.axis))
            deletetuxi = False

        # 各个碰撞检测
        for bullet in fires:
            for x in tuxis:
                if isclash(bullet, x):
                    deletetuxi = True
                    hanabis.append(hanabi(bullet.axis[0], bullet.axis[1]))

            if isclash(bullet, dragon):
                dragon.hp -= bullet.damage
                damages.append(Damage(bullet.axis[0]+20, bullet.axis[1]-50,3,bullet.damage))
                if dragon.hp <= 5000:
                    dragon.rage()
                if dragon.hp <= 0:
                    dragon.DEAD = True
                deletetuxi = True
                hanabis.append(hanabi(bullet.axis[0], bullet.axis[1]))

            if deletetuxi:
                fires.remove(bullet)
            deletetuxi = False

        for dm in damages:
            if dm.hitcal:
                damages.remove(dm)
            else:
                dm.move()
                showdm(dm.damage, dm.axis[0], dm.axis[1])

        for bo in boom:
            if bo.hitcal:
                boom.remove(bo)
            else:
                bo.move()
                screen.blit(bo.img,(bo.axis[0],bo.axis[1]))



        for x in hanabis:
            x.move()
            if x.over:
                hanabis.remove(x)
            screen.blit(x.img, tuple(x.axis))
            x.img.set_colorkey((255, 255, 255))

        # 滞空和弹墙判定
        man.donothing()
        man.wallhit()
        man.cache.set_colorkey((255, 255, 255))
        dragon.cache.set_colorkey((255, 255, 255))
        screen.blit(man.cache, tuple(man.getaxis))
        screen.blit(dragon.cache, tuple(dragon.axis))

    if end == "龙死了":
        screen.blit(pygame.image.load('./素材/主角胜利.png'), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        showhp()
        if deaddragon.hitcal:
            # print("龙死了结束")
            end = "龙死了画面"
        else:
            deaddragon.move()
            screen.blit(deaddragon.img, tuple(deaddragon.axis))

    if end == "龙死了画面":
        screen.blit(pygame.image.load('./素材/龙死了结局.png'), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE]:
            capcount = 0
            caporder = 0
            fires = []
            tuxis = []
            hanabis = []
            firecount = 0
            frietime = fps
            canfire = True
            man = Man()
            dragon = Dragon()
            deaddragon = Dead_Dragon(0, 0, 0)
            end = "战斗中！"

    if end == "男 人 死":
        screen.blit(pygame.image.load('./素材/主角死亡.png'), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        showhp()
        if deadman.hitcal:
            # print("龙死了结束")
            end = "男 人 死 画 面"
        else:
            deadman.move()
            screen.blit(deadman.img, tuple(deadman.axis))

    if end == "男 人 死 画 面":
        screen.blit(pygame.image.load('./素材/主角白给.png'), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE]:
            capcount = 0
            caporder = 0
            fires = []
            tuxis = []
            hanabis = []
            firecount = 0
            frietime = fps
            canfire = True
            man = Man()
            dragon = Dragon()
            deaddragon = Dead_Dragon(0, 0, 0)
            end = "战斗中！"












    #更新
    pygame.display.update()
    fclock.tick(fps)

