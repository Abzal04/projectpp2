import pygame as pg
import random,time,sys
pg.init()

W=1200
H=750
x,y=W//2,H-200

screen=pg.display.set_mode((W,H))
pg.display.set_caption("Rain")

clock=pg.time.Clock()

student_img = pg.image.load("student.png")
umbrella_img1 = pg.image.load("umbrella.png")
umbrella_img=pg.transform.scale(umbrella_img1,(150,150))
umbrella_rect=umbrella_img.get_rect()
raindrop_img = pg.image.load("raindrop.png")


class Student(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=student_img
        self.image=pg.transform.scale(self.image,(50,100))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.direction=None
        self.move_timer=0
    def move(self):
        if pg.time.get_ticks()-self.move_timer>random.randint(1000,3000):
            self.direction=random.choice(["left",'right','up','down'])
            self.move_timer=pg.time.get_ticks()

        if self.direction=="left" and self.rect.left> 0:
            self.rect.move_ip(-3,1)
        elif self.direction=="right" and self.rect.right < W:
            self.rect.move_ip(3,2)
        elif self.direction == "up" and self.rect.top > 0:
            self.rect.move_ip(1, -3)
        elif self.direction == "down" and self.rect.bottom < H and self.rect.top >H-300:
            self.rect.move_ip(2, 4)

class Umbrella(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=umbrella_img
        self.rect=self.image.get_rect()
        self.rect.center=(mouse_x,mouse_y)
    def move(self):
        pass

class Raindrop(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1=raindrop_img
        self.image=pg.transform.scale(self.image1,(20,20))
        self.rect=self.image.get_rect()
        self.speedx=3
        self.speedy=random.randint(2,10)
        self.rect.x=random.randint(-5,W)
        self.rect.y=random.randint(-H,-5)
    
    def update(self):
        if self.rect.bottom > H:
            self.speedx=3
            self.speedy=random.randint(2,10)
            self.rect.x=random.randint(-5,W)
            self.rect.y=random.randint(-H,-5)
        self.rect.x += self.speedx
        self.rect.y += self.speedy

rain_group = pg.sprite.Group()
for i in range(100):
    new_raindrop=Raindrop()
    rain_group.add(new_raindrop)

S1=Student()

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()

    mouse_x,mouse_y=pg.mouse.get_pos()
    U1=Umbrella()
    all_sprites=pg.sprite.Group()
    all_sprites.add(S1,U1)

    rain_group.update()
    screen.fill((0,0,0))
    rain_group.draw(screen)
#cloud and ground
    pg.draw.rect(screen,(0,0,200),(10,0,W-20,100))
    pg.draw.rect(screen,(0,255,0),(0,H-300,W,300))


    for entity in all_sprites:
        screen.blit(entity.image,entity.rect)
        entity.move()
    
    pg.display.flip()
    clock.tick(60)