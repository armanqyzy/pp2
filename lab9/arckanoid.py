import pygame 
import random, sys
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
bg = (0, 0, 0)


pygame.mixer.music.load('img/arckanoid_music.mp3')

# Set initial volume (0.5 is half of maximum volume)
pygame.mixer.music.set_volume(0.2)

# Play music (you can also specify the number of loops)
pygame.mixer.music.play(-1)  # -1 means looping indefinitely


bonus_sound = pygame.mixer.Sound('img/bonus.wav')

# Global variables
is_paused = False
is_in_menu = True
paddleSpeed = 20
ballSpeed = 6

paddleW = 150
paddleH = 25
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

ballRadius = 20
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

collision_sound = pygame.mixer.Sound('img/catch.mp3')

# Block class and initialization
class Block:
    def __init__(self, block_rect, color_list, unbreakable=False, bonus=False):
        self.rect = block_rect
        self.color = color_list
        self.unbreakable = unbreakable
        self.bonus = bonus
        self.num_hits = 3 if bonus else 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color[0], self.rect)

    def handle_bonus(self):
        global paddleW
        paddleW += 20
        bonus_sound.play()
        return True

    def hit(self):
        if not self.unbreakable:
            self.num_hits -= 1
            if self.num_hits == 0:
                if self.bonus:
                    return True
                else:
                    return True
        return False

block_list = []

# Block generation
for i in range(10):
    for j in range(4):
        block_rect = pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50)
        unbreakable = (i % 2 == 0 and j % 2 == 0)
        bonus = (i % 6 == 0 and j % 2 == 0)
        if unbreakable:
            color_list = (230, 230, 250)
        elif bonus:
            color_list = (220, 20, 60)
        else:
            color_list = [(random.randrange(0, 255), random.randrange(0, 255),  random.randrange(0, 255))] 
        block_list.append(Block(block_rect, color_list, unbreakable, bonus))

# Fonts for menus
menu_font = pygame.font.SysFont('comicsansms', 40)

# Main menu function
def main_menu():
    global is_in_menu
    while is_in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    is_in_menu = False
                    return
                elif event.key == pygame.K_s:
                    settings_menu()

        screen.fill(bg)
        title_text = menu_font.render('main menu', True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(W // 2, H // 2 - 100))
        start_text = menu_font.render('Press "ENTER" so we can start', True, (255, 255, 255))
        start_rect = start_text.get_rect(center=(W // 2, H // 2))
        settings_text = menu_font.render('Press "S" for settings', True, (255, 255, 255))
        settings_rect = settings_text.get_rect(center=(W // 2, H // 2 + 100))

        screen.blit(title_text, title_rect)
        screen.blit(start_text, start_rect)
        screen.blit(settings_text, settings_rect)

        pygame.display.flip()
        clock.tick(FPS)

# Settings menu function
def settings_menu():
    global paddleSpeed, ballSpeed, is_in_menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_in_menu = True
                    return
                elif event.key == pygame.K_UP:
                    paddleSpeed += 1
                elif event.key == pygame.K_DOWN:
                    paddleSpeed -= 1
                elif event.key == pygame.K_RIGHT:
                    ballSpeed += 1
                elif event.key == pygame.K_LEFT:
                    ballSpeed -= 1

        screen.fill(bg)
        title_text = menu_font.render('Settings', True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(W // 2, 50))
        paddle_text = menu_font.render(f'Paddle Speed: {paddleSpeed}', True, (255, 255, 255))
        paddle_rect = paddle_text.get_rect(center=(W // 2, H // 2 - 50))
        ball_text = menu_font.render(f'Ball Speed: {ballSpeed}', True, (255, 255, 255))
        ball_rect = ball_text.get_rect(center=(W // 2, H // 2 ))
        back_text = menu_font.render('Press "ESC" to go back', True, (255, 255, 255))
        back_rect = back_text.get_rect(center=(W // 2, H - 50))

        screen.blit(title_text, title_rect)
        screen.blit(paddle_text, paddle_rect)
        screen.blit(ball_text, ball_rect)
        screen.blit(back_text, back_rect)

        pygame.display.flip()
        clock.tick(FPS)

# Pause menu function
def pause_menu():
    global is_paused
    while is_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    is_paused = False
                    return
                elif event.key == pygame.K_ESCAPE:
                    is_paused = False
                    return
                elif event.key == pygame.K_s:
                    settings_menu()

        screen.fill(bg)
        pause_text = menu_font.render('Game Paused', True, (255, 255, 255))
        pause_rect = pause_text.get_rect(center=(W // 2, H // 2 - 100))
        resume_text = menu_font.render('Press ENTER to resume', True, (255, 255, 255))
        resume_rect = resume_text.get_rect(center=(W // 2, H // 2))
        settings_text = menu_font.render('Press S for settings', True, (255, 255, 255))
        settings_rect = settings_text.get_rect(center=(W // 2, H // 2 + 100))

        screen.blit(pause_text, pause_rect)
        screen.blit(resume_text, resume_rect)
        screen.blit(settings_text, settings_rect)

        pygame.display.flip()
        clock.tick(FPS)
def detect_collision(dx, dy, ball, rect, is_unbreakable):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    
    if is_unbreakable:
        if abs(delta_x - delta_y) < 10:
            if dx > 0:
                ball.right = rect.left
            else:
                ball.left = rect.right
        elif delta_x > delta_y:
            ball.y += dy
        elif delta_y > delta_x:
            ball.x += dx

    return dx, dy
# Text for game over
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)


# Text for winning
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = winfont.render('Yay you WIN!', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)



incrSpeed = pygame.USEREVENT + 1
shrinkPaddle = pygame.USEREVENT + 2
pygame.time.set_timer(incrSpeed, 2000)
pygame.time.set_timer(shrinkPaddle, 2000)


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == incrSpeed:
            ballSpeed += 0.5
        if event.type == shrinkPaddle:
            paddleW -= 5
            paddle.width = paddleW

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if not is_in_menu:
                    is_paused = not is_paused
            elif is_in_menu:
                if event.key == pygame.K_RETURN:
                    main_menu()
                elif event.key == pygame.K_s:
                    settings_menu()
            elif is_paused:
                if event.key == pygame.K_RETURN:
                    is_paused = False
                elif event.key == pygame.K_s:
                    settings_menu()

    if is_paused:
        pause_menu()
        continue

    if is_in_menu:
        main_menu()
        continue

    screen.fill(bg)
    
    for block in block_list:
        block.draw(screen)
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius: 
        dy = -dy
        ball.centery = ballRadius

    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle, False)

    hitIndex = ball.collidelist([block.rect for block in block_list])

    if hitIndex != -1:
        block = block_list[hitIndex]
        if block.unbreakable:
            dx, dy = detect_collision(dx, dy, ball, block.rect, True)
        else:
            dx, dy = detect_collision(dx, dy, ball, block.rect, False)
            if block.hit():
                block_list.pop(hitIndex)
                game_score += 1
                collision_sound.play()

    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
        pygame.mixer.music.stop()
        pygame.mixer.music.stop()

        pygame.mixer.Sound('img/loser.wav').play()
        pygame.display.update()
        pygame.time.wait(2200)  # Wait 2.2 seconds before exiting the game
        pygame.quit()
        sys.exit()


    elif not any(block for block in block_list if not block.unbreakable):

        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)
        pygame.mixer.music.stop()

        pygame.mixer.Sound('img/yay.mp3').play()
        pygame.display.update()
        pygame.time.wait(5000)  # Wait 5 seconds before exiting the game
        pygame.quit()
        sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)
