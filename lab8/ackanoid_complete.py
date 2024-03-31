#увеличивает скорость мяча на 0.5 каждые 2 секунды
#уменьшает ширину paddle на 5 каждые 2 секунды
#bonus bricks создаются с помощью переменной bonus, которая устанавливается в True для определенных bricks. 
#При уничтожении бонусного brick ширина paddle увеличивается на 20 пикселя
#а также я попыталась предотвратить колебления мяча в границах


import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
bg = (0, 0, 0)

paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

collision_sound = pygame.mixer.Sound('img/catch.mp3')

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

losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

incrSpeed = pygame.USEREVENT + 1
shrinkPaddle = pygame.USEREVENT + 2
pygame.time.set_timer(incrSpeed, 2000)
pygame.time.set_timer(shrinkPaddle, 2000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == incrSpeed:
            ballSpeed += 0.5
        if event.type == shrinkPaddle:
            paddleW -= 5
            paddle.width = paddleW

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
    elif not any(block.bonus for block in block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)
        
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)
