import pygame as pg
import random,time,sys
pg.init()

W=1200
H=750
x,y=W//2,H-200

screen=pg.display.set_mode((W,H))
pg.display.set_caption("Rain")

clock=pg.time.Clock()

student_img = pg.image.load("design/studentwlaptop-frame-0 (1).png")
student_back_image=pg.image.load("design/backsprite.png")
umbrella_img=pg.transform.rotate(pg.transform.scale(pg.image.load("design/umbrella1.png"),(150,150)),30)
umbrella_rect=umbrella_img.get_rect()
raindrop_img = pg.image.load("design/raindrop.png")

rain_timer = pg.time.get_ticks()
spawn_interval = random.randint(1000, 2000)

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
            self.kill()
        else:
            self.rect.x += self.speedx
            self.rect.y += self.speedy


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
        self.counter=0
        self.delay=5
        self.exp=0
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
        # Movement left
        if self.direction=="left":
            self.images=[]
            for num in range(0,3):
                img=pg.transform.flip((pg.image.load(f"design/walking_frame/walkright-frame-{num}.png").convert_alpha()),True,False)
                img=pg.transform.scale(img,(100,100))
                self.images.append(img)
            self.image=self.images[self.index]
            if self.index==2:
                self.index=0
            else:
                self.counter += 1
                if self.counter >= self.delay +5:
                    self.counter = 0
                    self.index+=1
                    self.rect.move_ip(random.randrange(-30,-20),random.randrange(-5,5))
                    if self.rect.left < 35:
                        self.direction=random.choice(["up",'right','down'])
        # Movement right
        elif self.direction == "right":
            self.images=[]
            for num in range(0,3):
                img=pg.image.load(f"design/walking_frame/walkright-frame-{num}.png").convert_alpha()
                img=pg.transform.scale(img,(100,100))
                self.images.append(img)
            self.image=self.images[self.index]
            if self.index==2:
                self.index=0
            else:
                self.counter += 1
                if self.counter >=self.delay:
                    self.counter = 0
                    self.index+=1
                    self.rect.move_ip(random.randrange(20,30),random.randrange(-5,5))
                    if self.rect.right > W-35:
                        self.direction=random.choice(["left",'up','down'])
        # Movement up
        elif self.direction == "up":
            self.image = student_back_image
            self.counter+=1
            if self.counter >= self.delay-2:
                self.counter=0
                self.rect.move_ip(0,random.randrange(-20,-5))
                if self.rect.top < H-310:
                    self.direction=random.choice(["left",'right','down'])
        # Movement down
        elif self.direction == "down":
            self.counter +=1
            self.image = student_img
            if self.counter >=self.delay-2:
                self.counter = 0
                self.rect.move_ip(0,random.randrange(5,20))
                if self.rect.bottom > H-35:
                    self.direction=random.choice(["left",'right','up']) 
    def explosion(self):
        self.exp=[]
        for num in range(1,5):
            img = pg.image.load(f"design/explosion/explosion final-frame-{num}.png")
            img = pg.transform.scale(img,(100,100))
            self.exp.append(img)
        self.image = self.exp[self.index]
        if self.index == 4:
            self.kill()
        else:
            self.counter += 1
            if self.counter >= self.delay:
                self.counter = 0
                self.index +=1
            
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

    rain_group = pg.sprite.Group()
    current_time=pg.time.get_ticks()
    if current_time -rain_timer > spawn_interval:
        num_raindrops = random.randint(20,40)
        for i in range(num_raindrops):
            new_raindrop=Raindrop()
            rain_group.add(new_raindrop)
        rain_timer=current_time
        spawn_interval = random.randint(1000, 2000)  
    for raindrop in rain_group:
        raindrop.update()
    screen.fill((0,0,0))
    rain_group.draw(screen)

    #Collision of umbrella with raindrops
    collided_rain = pg.sprite.spritecollide(U1,rain_group,dokill=False)
    for raindrop in collided_rain:
            rain_group.remove(raindrop)

    #Collision of student with raindrop
    if pg.sprite.spritecollide(S1,rain_group,dokill=False):
        S1.explosion()
        time.sleep(0.5)


#cloud and ground
    pg.draw.rect(screen,(0,0,200),(10,0,W-20,100))
    # pg.draw.rect(screen,(0,255,0),(0,H-300,W,300))

    for entity in all_sprites:
        screen.blit(entity.image,entity.rect)
        entity.move()
    
    pg.display.flip()
    clock.tick(60)