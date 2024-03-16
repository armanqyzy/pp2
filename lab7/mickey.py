import pygame
import datetime

pygame.init()

width, height = 800, 800
x = width // 2
y = height // 2
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((width, height))

mickey = pygame.image.load("images/main-clock.png")
leftHand = pygame.image.load("images/left-hand.png")
rightHand = pygame.image.load("images/right-hand.png")
mickeyRect = mickey.get_rect()

def blitrotate(sur, image, center, angle):
    rotated = pygame.transform.rotate(image, angle)
    newrect = rotated.get_rect(center=image.get_rect(center=center).center)
    sur.blit(rotated, newrect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute
    
    left_angle = (seconds / 60) * 360
    right_angle = (minutes / 60) * 360

    left_angle = -left_angle + 90
    right_angle = -right_angle + 90

    sc.fill(WHITE)

    sc.blit(mickey, (x - mickeyRect.width / 2, y - mickeyRect.height / 2))
    blitrotate(sc, leftHand, (x, y), left_angle)
    blitrotate(sc, rightHand, (x, y), right_angle)

    pygame.display.update()


