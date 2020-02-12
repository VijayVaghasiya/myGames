
'''
Project Name : Space Invader
Developed as hobby project by @pyLancing

'''

import pygame, random, math
from pygame import mixer

# Initialise the Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('background.png')

# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

#-------------------------------------------------------
# Attribution for icons 'player.png' and 'enemy.png' : 
# Icons made by https://www.flaticon.com/authors/freepik
#-------------------------------------------------------

# Player
player_image = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
# playerY_change = 0

# Enemy
enemy_image = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_image.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(3)
    enemyY_change.append(30)


# Enemy

# ready - state where we cant see bullet
# fire - bullet is in movement

bullet_image = pygame.image.load('bullet.png')    
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = 'ready'

# Score
score_range = [10,25,40,60,90]
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over Text
game_over_font = pygame.font.Font('freesansbold.ttf', 70)


def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score,(x, y))

def game_over_text():
    game_over = game_over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(game_over,(200, 250))


def player(x,y):
    screen.blit(player_image,(x, y))

def enemy(x,y,i):
    screen.blit(enemy_image[i],(x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_image, (x+16, y+10))


def is_collision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))
    return distance < 27


# Game Loop
running = True
while running:

    # RGB = Red, Greem, Blue
    screen.fill((0,0,0))

    #Background Image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # On keystroke, check right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3

            if event.key == pygame.K_RIGHT:
                playerX_change = 3

            if event.key == pygame.K_SPACE:

                #Get the current X cordinate of spaceship
                if bullet_state == 'ready':
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX            
                    fire_bullet(playerX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0 


    # Player movement
    playerX += playerX_change

    # Boundary for player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):
        #Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        # Enemy movement
        enemyX[i] += enemyX_change[i]
        # Boundary for  enemy
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision 
        collision = is_collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = 'ready'
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
            score_value += 1


        enemy(enemyX[i], enemyY[i], i)


    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)
    show_score(textX,textY)


    pygame.display.update()
