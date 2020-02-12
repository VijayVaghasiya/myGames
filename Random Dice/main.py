
'''
Project Name : Roll the Dice
Developed as hobby project by @pyLancing
'''

import pygame, random

# Initialise the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((300,260))

#Title and Icon
pygame.display.set_caption("Snake n Ladder")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)


# Create List for Dice Images 
dice_images = ['one.png','two.png','three.png','four.png','five.png','six.png']
dice = [pygame.image.load(dice_images[i]) for i in range(6)]


number = 0

def visible_dice_movements():
    '''
    Create visual movement of dice faces and appear to player as dice is rolling 
    '''
    visual_movements = 0
    while visual_movements != 30  :
        number = random.randint(0,5)
        pygame.time.wait(30)   # Make dice movement visible with this delay

        # Overwrite last session to blit again
        screen.fill((220,220,220))
        screen.blit(dice[number],(85, 30))
        create_button()
        pygame.display.update()

        visual_movements += 1
    return number


def roll_dice(roll_decision):
    '''  Roll the dice based on the player's actions '''
    global number

    if roll_decision:
        # Run this once when either button is clicked or space key is presses
        number = visible_dice_movements()
    else:
        # Until either "button is NOT clicked on screen" or "space key is NOT pressed", blit the image using the last stored number
        screen.blit(dice[number],(85, 30))

def create_button():
    # Draw recangle for button
    pygame.draw.rect(screen, (0,0,0),(100,200,100,50))
    roll_text = pygame.font.Font('freesansbold.ttf', 20)
    screen.blit(roll_text.render("ROLL", True, (255,255,255)),(125, 215))

# Game Loop
running = True
while running:

    # Reset Rolling Decision
    roll_decision = False

    # RGB = Red, Greem, Blue
    screen.fill((220,220,220))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Rolling 1 : Press SPACE to roll the dice    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                roll_decision = True

        # Rolling 2 : Click button to roll the dice
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 100 and pygame.mouse.get_pos()[1] <= 250:
                roll_decision = True

    create_button()
    roll_dice(roll_decision)   
    pygame.display.update()
