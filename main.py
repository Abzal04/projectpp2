import pygame as pg
import random,time,sys
pg.init()

W=1200
H=750
x,y=W//2,H-200

screen=pg.display.set_mode((W,H))
pg.display.set_caption("Rain")

clock=pg.time.Clock()

student_img = pg.image.load("design/student with laptop.png")
#student's back image ??

umbrella_img=pg.transform.rotate(pg.transform.scale(pg.image.load("design/umbrella.png"),(150,150)),30)
umbrella_rect=umbrella_img.get_rect()
raindrop_img = pg.image.load("design/raindrop.png")
class Raindrop(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1=raindrop_img
        self.image=pg.transform.scale(self.image1,(40,40))
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

class Umbrella(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=umbrella_img
        self.rect=self.image.get_rect()
        self.rect.center=(mouse_x,mouse_y)
    def move(self):
        pass

class Student(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=student_img
        self.image=pg.transform.scale(self.image,(100,100))
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.direction=None
        self.move_timer=0
        self.images=0
        self.index=0
    def move(self):
        if pg.time.get_ticks() - self.move_timer > random.randint(2000,5000):
            self.direction=random.choice(["left",'right','up','down'])
            self.move_timer=pg.time.get_ticks()

        #Collision left
        if self.rect.centerx < 30:
            self.direction=random.choice(['right','up','down'])
            
        #Collision right
        if  self.rect.centerx > W-30:
            self.direction=random.choice(["left",'up','down'])

        #Collision top
        if self.rect.centery < H-310:
            self.direction=random.choice(["left",'right','down'])
 
        #Collision bottom
        if self.rect.centery > H-30:
            self.direction=random.choice(["left",'right','up'])

        if self.direction=="left":
            self.images=[]
            for num in range(0,3):
                img=pg.transform.flip((pg.image.load(f"design/right_walk/rigth-walk-frame-{num}.png").convert_alpha()),True,False)
                img=pg.transform.scale(img,(100,100))
                self.images.append(img)
            self.image=self.images[self.index]
            if self.index==2:
                self.index=0
            else:
                self.index+=1
            self.rect.move_ip(-2,1)
        
        elif self.direction == "right":
            self.images=[]
            for num in range(0,3):
                img=pg.image.load(f"design/right_walk/rigth-walk-frame-{num}.png").convert_alpha()
                img=pg.transform.scale(img,(100,100))
                self.images.append(img)
            self.image=self.images[self.index]
            if self.index==2:
                self.index=0
            else:
                self.index+=1
            self.rect.move_ip(2,1)
            
        elif self.direction == "up":
            self.image = student_img
            self.rect.move_ip(1, -2)
            
        elif self.direction == "down":
            self.image = student_img
            self.rect.move_ip(-1,2)
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

    #Collision of umbrella with raindrops
    collided_rain = pg.sprite.spritecollide(U1,rain_group,dokill=False)
    for raindrop in collided_rain:
            rain_group.remove(raindrop)

    #Collision of student with raindrop


#cloud and ground
    pg.draw.rect(screen,(0,0,200),(10,0,W-20,100))
    # pg.draw.rect(screen,(0,255,0),(0,H-300,W,300))


    for entity in all_sprites:
        screen.blit(entity.image,entity.rect)
        entity.move()
    
    pg.display.flip()
    clock.tick(60)