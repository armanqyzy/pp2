import pygame, sys
pygame.init()

W, H = 600, 500
sc = pygame.display.set_mode((W, H))

radius = 25
x = W // 2
y = H // 2
color = (255, 0, 0)

while True:
    sc.fill((255, 255, 255))

    pygame.draw.circle(sc, color, (x, y), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = max(radius, y - 30) 
            elif event.key == pygame.K_DOWN:
                y = min(H - radius, y + 30)
            elif event.key == pygame.K_LEFT:
                x = max(radius, x - 30)  
            elif event.key == pygame.K_RIGHT:
                x = min(W - radius, x + 30)  

    pygame.display.update()

pygame.quit()
