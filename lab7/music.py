import pygame
import sys

pygame.init()

W, H = 300, 380
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

billieEilish = pygame.image.load("images/billie.jpg")

sound1 = pygame.mixer.Sound('music/badguy.mp3')
sound2 = pygame.mixer.Sound('music/bury.mp3')
sound3 = pygame.mixer.Sound('music/hell.mp3')
sound4 = pygame.mixer.Sound('music/ily.mp3')
sound5 = pygame.mixer.Sound('music/party.mp3')
sound6 = pygame.mixer.Sound('music/strange.mp3')

music = [sound1, sound2, sound3, sound4, sound5, sound6]
i = 0
paused = False
music[0].play()
sc.blit(billieEilish, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.unpause()
                    paused = False
                else:
                    pygame.mixer.pause()
                    paused = True


            elif event.key == pygame.K_RIGHT:
                music[i].stop()
                i = (i + 1) % len(music)
                music[i].play()

            elif event.key == pygame.K_LEFT:
                music[i].stop()
                i = (i - 1) % len(music)
                music[i].play()

    pygame.display.update()
    clock.tick(60)
