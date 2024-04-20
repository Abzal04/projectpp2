import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = (135, 206, 250) #голубой 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rainy day")

# student_img = pygame.image.load("student.png")
umbrella_img = pygame.image.load("umbrella.png")
raindrop_img = pygame.image.load("raindrop.png")
lightning_img = pygame.image.load("lightning.png")
puddle_img = pygame.image.load("puddle.png")
super_umbrella_img = pygame.image.load("super_umbrella.png")
laptop_img = pygame.image.load("laptop.png")
student_img = pygame.image.load("student_with_laptop.png")


TIME_LIMIT = 60

current_time = pygame.time.get_ticks()
start_time = current_time
game_over = False

# class Student(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = student_img
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH // 2, HEIGHT - 100) 
#         self.speed = 5
#         self.umbrella = Umbrella()

#     def update(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT] and self.rect.left > 0:
#             self.rect.x -= self.speed
#         if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
#             self.rect.x += self.speed
#         self.umbrella.rect.centerx = self.rect.centerx
#         self.umbrella.rect.bottom = self.rect.top  

class Student(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = student_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
        self.speed = 5
        self.laptop = Laptop()
        self.laptop.rect.centerx = self.rect.centerx
        self.laptop.rect.bottom = self.rect.top

def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and self.rect.left > 0:
        self.rect.x -= self.speed
        self.laptop.rect.x -= self.speed
    if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
        self.rect.x += self.speed
        self.laptop.rect.x += self.speed
    if keys[pygame.K_UP] and self.rect.top > 0:
        self.rect.y -= self.speed
    if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
        self.rect.y += self.speed
        
def check_hit_laptop(self):
    if self.rect.colliderect(student.laptop.rect):
        game_over()  


class Umbrella(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = umbrella_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 80)

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.clamp_ip(screen.get_rect())

class Laptop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = laptop_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.exploded = False

    def explode(self):
        self.exploded = True
        explosion_animation = [pygame.image.load(f"explosion{i}.png") for i in range(1, 6)]
        for frame in explosion_animation:
            screen.fill(BACKGROUND_COLOR)
            screen.blit(frame, self.rect)
            pygame.display.flip()
            pygame.time.wait(100)  

class Raindrop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = raindrop_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(-100, -50))
        self.speed = random.randint(5, 15)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.center = (random.randint(0, WIDTH), random.randint(-100, -50))
            self.speed = random.randint(5, 15)
        if pygame.sprite.spritecollide(self, umbrellas, False):
            self.kill()  

    def check_hit_laptop(self):
        if self.rect.colliderect(laptop.rect):
            game_over() 


def game_over():
    font = pygame.font.SysFont('couriernew', 40)
    text_surface = font.render("Oh, you did not save the laptop ಠ_ಠ)", True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

    pygame.time.delay(3000)



# class Lightning(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = lightning_img
#         self.rect = self.image.get_rect()
#         self.rect.centerx = random.randint(50, WIDTH - 50)
#         self.rect.bottom = 0

class Puddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = puddle_img
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(50, WIDTH - 50)
        self.rect.bottom = HEIGHT - 50

class SuperUmbrella(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = super_umbrella_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

all_sprites = pygame.sprite.Group()
students = pygame.sprite.Group()
umbrellas = pygame.sprite.Group()
raindrops = pygame.sprite.Group()
puddles = pygame.sprite.Group()
lightnings = pygame.sprite.Group()

student = Student()
all_sprites.add(student)
students.add(student)

umbrella = Umbrella()
all_sprites.add(umbrella)
umbrellas.add(umbrella)

laptop = Laptop()
all_sprites.add(laptop)


# for _ in range(3):
#     lightning = Lightning()
#     all_sprites.add(lightning)
#     lightnings.add(lightning)

# def avoid_lightning():
#     if pygame.sprite.spritecollide(umbrella, lightnings, False):
#         umbrella.kill() 

def jump():
    if pygame.sprite.spritecollide(student, puddles, False):
        student.rect.y -= 100 

# def display_timer():
#     current_time = pygame.time.get_ticks()
#     time_left = max(0, TIME_LIMIT - (current_time - start_time) // 1000)
#     font = pygame.font.Font(None, 36)
#     timer_text = font.render("Time left: " + str(time_left), True, (0, 0, 0))
#     screen.blit(timer_text, (10, 10))
#     if time_left == 0 and not bonus_granted:
#         bonus_granted = True
#         bonus.apply_bonus(student)


# class Bonus(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = bonus_img
#         self.rect = self.image.get_rect()
#         self.rect.center = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

#     def apply_bonus(self):
#         student.umbrella.image = super_umbrella_img
#         student.umbrella.rect = super_umbrella_img.get_rect()
#         student.umbrella.rect.center = student.rect.center

#         student.super_umbrella_active = True

#         SUPER_UMBRELLA_EXPIRATION_EVENT = pygame.USEREVENT + 1  
#         pygame.time.set_timer(SUPER_UMBRELLA_EXPIRATION_EVENT, 10000)  #10 секунд


# bonuses = pygame.sprite.Group()

# for _ in range(3):
#     bonus = Bonus()
#     all_sprites.add(bonus)
#     bonuses.add(bonus)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()

    all_sprites.update()

    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

pygame.quit()
sys.exit()

