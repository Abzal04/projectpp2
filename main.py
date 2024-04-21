import pygame as pg
import random,datetime,sys,time
pg.init()

W=1000
H=750
x,y=W//2,H-200
running = True

screen=pg.display.set_mode((W,H))
pg.display.set_caption("Rain")

clock=pg.time.Clock()
FPS=60
counter_for_FPS = 0
time_since_win_displayed = 0


student_img = pg.image.load("design/studentwlaptop-frame-0 (1).png")
student_back_image=pg.image.load("design/backsprite.png")
umbrella_img=pg.transform.rotate(pg.transform.scale(pg.image.load("design/umbrella1.png"),(150,150)),30)
umbrella_rect=umbrella_img.get_rect()
raindrop_img = pg.image.load("design/raindrop.png")
bg=pg.image.load("design/background final.png")

# Game Over Screen
game_over_font = pg.font.SysFont("comicsansms",60)
game_over_text = game_over_font.render("Game Over",True,(255,255,255))
game_overRect = game_over_text.get_rect()
game_overRect.center = ((W//2,H//2))

# Win Screen
win_font = pg.font.SysFont("comicsansms",60)
win_font_text = win_font.render("You won !!!",True,(255,255,255))
win_fontRect = win_font_text.get_rect()
win_fontRect.center = ((W//2 , H//2))

# For time Table
start_time = datetime.datetime.now().replace(hour=0, minute=14, second=0, microsecond=0)
end_time = start_time.replace(minute=14,second=2)


rain_group = pg.sprite.Group()
rain_timer = pg.time.get_ticks()
spawn_interval = random.randint(1000, 2000)
paused = False
collision_time = 0

class Raindrop(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1=raindrop_img
        self.image=pg.transform.scale(self.image1,(40,40))
        self.rect=self.image.get_rect()
        self.speedx=3
        self.speedy=random.randint(2,10)
        self.rect.x=random.randint(-W//2,W)
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
            # Collision left
            if self.rect.left <= 30:
                self.direction = "right"

            # Collision right
            if self.rect.right >= W - 30:
                self.direction = "left"

            # Collision top
            if self.rect.top <= H - 240:
                self.direction = "down"

            # Collision bottom
            if self.rect.bottom >= H - 30:
                self.direction = "up"

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
            self.counter += 1
            if self.counter >= self.delay - 2:
                self.counter=0
                self.rect.move_ip(0,random.randrange(-20,-5))
                if self.rect.top < H-240:
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
        for num in range(0,5):
            img = pg.image.load(f"design/explosion/explosion final-frame-{num}.png")
            img = pg.transform.scale(img,(100,100))
            self.exp.append(img)
        self.image = self.exp[self.index]
        if self.index == 4:
            self.index =0
        else:
            self.counter += 1
            if self.counter >= self.delay+10:
                self.counter = 0
                self.index +=1
            
S1=Student()
S2=Student()

while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()

    if not paused:                                                                              ###########
        screen.blit(bg,(0,0))

        time_table_font = pg.font.SysFont("comicsansms",60)
            # print(current_time.strftime("%M:%S"))
        counter_for_FPS+=1
        if counter_for_FPS >= FPS:
            counter_for_FPS = 0
            start_time +=datetime.timedelta(seconds=1)
            if start_time > end_time:
                #music of win
                running = False
            
            # Displaying win 
                screen.fill((0,0,0))
                screen.blit(win_font_text, win_fontRect)
                pg.display.update()
                time_since_win_displayed +=1
                if time_since_win_displayed >= 120:
                    time.sleep(2)
                    pg.quit()
                    sys.exit()

                screen.fill((0,0,0))
                screen.blit(win_font_text,(W//2,H//2))
                pg.display.update()
                time_since_win_displayed +=1
                if time_since_win_displayed >= 120:
                    time.sleep(2)
                    running = False

        time_table_text = time_table_font.render(f"{start_time: %M:%S}", True, (255,0,0))
        time_tableRect = time_table_text.get_rect()
        time_tableRect.center = ((W-150,80))
        screen.blit(time_table_text,time_tableRect)
        
        mouse_x,mouse_y = pg.mouse.get_pos()
        U1=Umbrella()
    
        all_sprites=pg.sprite.Group()
        all_sprites.add(S1,U1)

        # The appearance of raindrops
        current_time=pg.time.get_ticks()
        if current_time -rain_timer > spawn_interval:
            num_raindrops = random.randint(30,60)
            for i in range(num_raindrops):
                new_raindrop=Raindrop()
                rain_group.add(new_raindrop)
            rain_timer=current_time
            spawn_interval = random.randint(1000, 2000)  
        for raindrop in rain_group:
            raindrop.update()
        rain_group.draw(screen)

        #Collision of umbrella with raindrops
        collided_rain = pg.sprite.spritecollide(U1,rain_group,dokill=False)
        for raindrop in collided_rain:
            rain_group.remove(raindrop)
        

        for entity in all_sprites:
            screen.blit(entity.image,entity.rect)
            entity.move()

        last_pos = (S1.rect.x,S1.rect.y)
        
    
        pg.display.flip()
        clock.tick(60)
    #Collision of student with raindrop
    if pg.sprite.spritecollideany(S1,rain_group):
        
        for all in rain_group:
            all.kill()
        for all in all_sprites:
            all.kill()
            
        collision_time = pg.time.get_ticks()
        paused = True
    if paused:
            S2.rect = last_pos
            S2.explosion()
            screen.blit(S2.image,S2.rect)
            screen.blit(game_over_text,game_overRect)
            pg.display.flip()
            clock.tick(FPS)