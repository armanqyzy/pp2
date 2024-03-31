import pygame
from pygame.locals import *
import random
import sys
import time
# Initialize pygame
pygame.init()

# Set up FPS (Frames Per Second)
FPS = 60
FramePerSec = pygame.time.Clock()

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up speed and points variables
SPEED = 5
SCORE=0
Points = 0
point = 150
cycle = 1
points = str(Points)

# Set up screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Load game background
bg = pygame.image.load("img/AnimatedStreet.png")

# Create the display surface
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)

# Set up fonts
font = pygame.font.Font("fonts/Lato-Black.ttf", 60)
font_small = pygame.font.Font("fonts/Lato-Black.ttf", 40)
game_over = font.render("Game Over", True, BLUE)

# Create classes for coins, enemies, and player car
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/coin_gold_racer.png")
        self.rect = self.image.get_rect()
        self.reset()  # Initialize coin position

    def reset(self):
        # Spawn the coin at a random position horizontally, above the screen
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)
        self.rect.y = -self.rect.height  # coin position above the screen

    def move(self):
        #  downwards 
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.reset()

    def coin_kill(self):
        # random position above the screen
        self.rect.center = (random.randint(0, SCREEN_WIDTH), 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        # Reset enemy position if it goes beyond the screen boundaries
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE+=1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()


#creating useful groups to use our sprites
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
coins = pygame.sprite.Group()
coins.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                P1.rect.move_ip(-5, 0)
            elif event.key == pygame.K_RIGHT:
                P1.rect.move_ip(5, 0)

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(bg, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    point_counter = font_small.render(points, True, BLUE)
    DISPLAYSURF.blit(point_counter, (SCREEN_WIDTH - point_counter.get_width() - 10, 10))

    #cycle of movements of sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    #condition of collision
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('img/crash.wav').play()
        # time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        last_point = font_small.render("Points: ", True, BLUE)
        DISPLAYSURF.blit(last_point, (40, 320))
        DISPLAYSURF.blit(point_counter, (200, 320))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        pygame.time.wait(2000)  # Wait 2 seconds before exiting the game
        pygame.quit()
        sys.exit()

    for coin in coins:
        if pygame.sprite.collide_rect(P1, coin):
            Points += point
            coin.coin_kill()

    points = str(Points)

    #make game more challenging
    if Points >= 1000 * cycle:
        SPEED += 1
        point += 50
        cycle += 1

    pygame.display.update()
    FramePerSec.tick(FPS)
