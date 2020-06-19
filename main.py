import pygame
import random
import math
from pygame import mixer
# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((600, 800))

# Background
background = pygame.image.load('14865.jpg')

# Bgm
mixer.music.load('Loveshadow_-_Tall_Man_Strut..mp3')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption('Catch The Basketball')
icon = pygame.image.load('001-basketball.png')
pygame.display.set_icon(icon)

# Basket
basketImg1 = pygame.image.load('001-basketball.png')
basketImg2 = pygame.image.load('shoot.png')
basket1X = 280
basket1Y = 650
basket2X = 280
basket2Y = 730
basket1X_change = 0
basket2X_change = 0

# Ball
ballImg1 = []
ballImg2 = []
ball1X = []
ball1Y = []
ball2X = []
ball2Y = []
ball1X_change = []
ball1Y_change = []
ball2X_change = []
ball2Y_change = []
num_of_balls = 3


for i in range(num_of_balls):
    ballImg1.append(pygame.image.load('001-basketball-ball.png'))
    ballImg2.append(pygame.image.load('002-basketball-ball.png'))
    ball1X.append(random.randint(0, 600))
    ball1Y.append(random.randint(-600, -400))
    ball2X.append(random.randint(0, 600))
    ball2Y.append(random.randint(-600, -400))
    ball1X_change_list = [1, 0.8, 0.6, 0.4, 0.2, -0.2, -0.4, -0.6, -0.8, -1]
    ball1X_change.append(random.choice(ball1X_change_list))
    ball1Y_change_list = [1, 0.8, 0.6, 0.4, 0.2]
    ball1Y_change.append(random.choice(ball1Y_change_list))
    ball2X_change_list = [1, 0.8, 0.6, 0.4, 0.2, -0.2, -0.4, -0.6, -0.8, -1]
    ball2X_change.append(random.choice(ball2X_change_list))
    ball2Y_change_list = [1, 0.8, 0.6, 0.4, 0.2]
    ball2Y_change.append(random.choice(ball2Y_change_list))

# Score
score_value = 0
font = pygame.font.Font('BebasNeue-Regular.ttf', 50)

score_textX = 10
score_textY = 10

# Game Over text
over_font = pygame.font.Font('GrindAndDeath_Demo.ttf', 80)

# Miss
miss_value = 0
miss_font = pygame.font.Font('BebasNeue-Regular.ttf', 50)

miss_textX = 450
miss_textY = 10


def display_score(x, y):
    score_text = font.render('Score :' + str(score_value), True, (255, 255, 255))
    screen.blit(score_text, (x, y))


def game_over_text():
    over_text = over_font.render('GAME OVER', True, (128, 0, 0))
    screen.blit(over_text, (90, 300))


def display_miss(x, y):
    miss_text = miss_font.render('Miss :' + str(miss_value), True, (255, 255, 255))
    screen.blit(miss_text, (x, y))


def basket1(x, y):
    screen.blit(basketImg1, (x, y))


def basket2(x, y):
    screen.blit(basketImg2, (x, y))


def ball1(x, y, i):
    screen.blit(ballImg1[i], (x, y))


def ball2(x, y, i):
    screen.blit(ballImg2[i], (x, y))


def collision1(ball1X, ball1Y, basket2X, basket2Y):
    d1 = math.sqrt(math.pow(ball1X - basket2X, 2) + math.pow(ball1Y - basket2Y, 2))
    if d1 < 25:
        return True
    else:
        return False


def collision2(ball2X, ball2Y, basket1X, basket1Y):
    d2 = math.sqrt(math.pow(ball2X - basket1X, 2) + math.pow(ball2Y - basket1Y, 2))
    if d2 < 25:
        return True
    else:
        return False


def collision3(ball1X, ball1Y, basket1X, basket1Y):
    d3 = math.sqrt(math.pow(ball1X - basket1X, 2) + math.pow(ball1Y - basket1Y, 2))
    if d3 < 25:
        return True
    else:
        return False


def collision4(ball2X, ball2Y, basket2X, basket2Y):
    d4 = math.sqrt(math.pow(ball2X - basket2X, 2) + math.pow(ball2Y - basket2Y, 2))
    if d4 < 25:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    # RGB
    screen.fill((192, 192, 192))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                basket1X_change = -2
            if event.key == pygame.K_d:
                basket1X_change = 2
            if event.key == pygame.K_LEFT:
                basket2X_change = -2
            if event.key == pygame.K_RIGHT:
                basket2X_change = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                basket1X_change = 0
                basket2X_change = 0

    basket1X += basket1X_change
    basket2X += basket2X_change

    if basket1X <= 0:
        basket1X = 0
    elif basket1X >= 536:
        basket1X = 536

    if basket2X <= 0:
        basket2X = 0
    elif basket2X >= 536:
        basket2X = 536

    for i in range(num_of_balls):
        if miss_value == 5:
            for j in range(num_of_balls):
                ball1Y[j] = 2000
                ball2Y[j] = 2000
            game_over_text()
            break

        ball1X[i] += ball1X_change[i]
        ball1Y[i] += ball1Y_change[i]
        ball2X[i] += ball2X_change[i]
        ball2Y[i] += ball2Y_change[i]

        if ball1X[i] <= 0:
            ball1X_change[i] = 0.6
            ball1Y_change[i] = 0.6
        elif ball1X[i] >= 536:
            ball1X_change[i] = -0.6
            ball1Y_change[i] = 0.6

        if ball2X[i] <= 0:
            ball2X_change[i] = 0.6
            ball2Y_change[i] = 0.6
        elif ball2X[i] >= 536:
            ball2X_change[i] = -0.6
            ball2Y_change[i] = 0.6

        blue_blue = collision1(ball1X[i], ball1Y[i], basket2X, basket2Y)
        red_red = collision2(ball2X[i], ball2Y[i], basket1X, basket1Y)
        blue_red = collision3(ball1X[i], ball1Y[i], basket1X, basket1Y)
        red_blue = collision4(ball2X[i], ball2Y[i], basket2X, basket2Y)

        if blue_blue:
            score_value += 10
            swish_sound = mixer.Sound('Swish.wav')
            swish_sound.play()
            ball1X[i] = random.randint(0, 600)
            ball1Y[i] = random.randint(-600, -400)
        elif red_red:
            score_value += 10
            swish_sound = mixer.Sound('Swish.wav')
            swish_sound.play()
            ball2X[i] = random.randint(0, 600)
            ball2Y[i] = random.randint(-600, -400)
        elif blue_red:
            score_value -= 5
            swish_sound = mixer.Sound('Swish.wav')
            swish_sound.play()
            ball1X[i] = random.randint(0, 600)
            ball1Y[i] = random.randint(-600, -400)
        elif red_blue:
            score_value -= 5
            swish_sound = mixer.Sound('Swish.wav')
            swish_sound.play()
            ball2X[i] = random.randint(0, 600)
            ball2Y[i] = random.randint(-600, -400)
        elif ball1Y[i] > 850:
            ball1X[i] = random.randint(0, 600)
            ball1Y[i] = random.randint(-600, -400)
            miss_value += 1
        elif ball2Y[i] > 850:
            ball2X[i] = random.randint(0, 600)
            ball2Y[i] = random.randint(-600, -400)
            miss_value += 1

        if score_value < 0:
            score_value = 0

        ball1(ball1X[i], ball1Y[i], i)
        ball2(ball2X[i], ball2Y[i], i)

    basket1(basket1X, basket1Y)
    basket2(basket2X, basket2Y)
    display_score(score_textX, score_textY)
    display_miss(miss_textX, miss_textY)
    pygame.display.update()
