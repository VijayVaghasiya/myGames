'''
Project : Classical Snake and Ladder Game
Developed as hobby project by @pyLancing
'''

import pygame, random

# Initialise the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((900,700))

#Title and Icon
pygame.display.set_caption("Snake n Ladder")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)


# Dice 
dice_images = ['one.png','two.png','three.png','four.png','five.png','six.png']
dice = [pygame.image.load(dice_images[i]) for i in range(6)]
#number = 0


class Dice(object):

    def __init__(self, number=0):
        self.number = number 

    def create_illusion(self):
        '''
        Create illution of rolling dice 
        '''
        visual_movements = 0
        while visual_movements != 20  :

            self.number = random.randint(1,6)
            pygame.time.wait(30)   # Make dice movement visible with this delay

            # Overwrite last session to blit again
            screen.fill((255,255,255))  
            template() 
            screen.blit(dice[self.number-1],(680+65.4, 30))
            self.create_button()
            self.show_dice()
            pygame.display.update()
            visual_movements += 1
            show_player(players['player 1'][1],players['player 1'][2],players['player 1'][0])
            show_player(players['player 2'][1],players['player 2'][2],players['player 2'][0])
        return self.number


    def roll_dice(self,roll_decision):
        '''  Roll the dice based on the player's actions '''
        #global self.number

        if roll_decision:
            # Run this once when either button is clicked or space key is presses
            self.number = self.create_illusion()
        else:
            self.show_dice()# Until either "button is NOT clicked on screen" or "space key is NOT pressed", blit the image using the last stored number
        return self.number


    def show_dice(self):
        screen.blit(dice[self.number-1],(680+65.4, 30))
        show_player(players['player 1'][1],players['player 1'][2],players['player 1'][0])
        show_player(players['player 2'][1],players['player 2'][2],players['player 2'][0])

    def create_button(self):
        # Draw recangle for button
        pygame.draw.rect(screen, (0,0,0),(700+65.4,200,100,50))
        roll_text = pygame.font.Font('freesansbold.ttf', 20)
        screen.blit(roll_text.render("ROLL", True, (255,255,255)),(720+65.4, 215))

     

my_dice = Dice()

# Snack and Ladder Template
game_image = pygame.image.load('template.png')


# Players
red_player = pygame.image.load('red.png')
yellow_player = pygame.image.load('yellow.png')

players = {"player 1" : [red_player, 0, 0, 0], "player 2" : [yellow_player, 0, 0, 0]}

red_player_pos = 0


# Board Metrix
ladders = {1 : (0,0)}
snack = [21,23]
#board_metrix = { player : "", player_move_by : 0 }

x_pos = 16.7
y_pos = 605.3


player_font = pygame.font.Font('freesansbold.ttf', 12)


def display_player_text(player):
    player_text = player_font.render(player, True, (0,0,0))
    screen.blit(player_text,(680+65.4, 10))



def template():
    screen.blit(game_image,(65.4,0))

once = True
def move_player(x,y, player):
    global x_pos,y_pos
    
    x_pos = 16.7+65.4*x
    y_pos = 605.3-65.4*y
    screen.blit(player,(x_pos,y_pos))

    return x_pos, y_pos

def show_player(x_pos,y_pos, player):
    screen.blit(player,(x_pos,y_pos))

def board_metrix():

    dic = {}
    total = 0
    for i in range(1,11):
        if i%2 ==0 or i in range(20,101,20):
            for j in reversed(range(1,11)):
                for k in range(i,10*i):
                    total += 1
                    dic[total] = (j , i-1)
                    break
        if i %2 !=0 or i in range(10,101,20):
            for j in range(1,11):
                for k in range(i,10*i):
                    total += 1
                    dic[total] = (j , i-1)
                    break
    return dic

flag = True
player1_score = 0
player2_score = 0
def choose_player():
    global flag
    if flag:
        flag = False
        return "player 1"
    else:
        flag = True
        return "player 2"




#once = True
#red_player_count = 0
player = ""
# Game Loop
score = 0
running = True
while running:

    # Reset Rolling Decision
    roll_decision = False
    

    
    screen.fill((255,255,255))
    template()
    display_player_text(player)
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False

        # Rolling 1 : Press SPACE to roll the dice    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                roll_decision = True

        # Rolling 2 : Click button to roll the dice
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 701 and pygame.mouse.get_pos()[1] <= 250:
                roll_decision = True



    if roll_decision:
        show_player(players['player 1'][1],players['player 1'][2],players['player 1'][0])
        show_player(players['player 2'][1],players['player 2'][2],players['player 2'][0])
        player = choose_player()

        print(f"{player} is playing")

        count = my_dice.roll_dice(roll_decision)
        players[player][3] += count

        dic = board_metrix()
        if(players[player][3] <=100):
            players[player][1], players[player][2] = move_player(dic[players[player][3]][0],dic[players[player][3]][1],players[player][0])
        else:
            pass


    #my_dice.roll_dice(roll_decision)
    my_dice.show_dice()
#    print(players['player 1'][1], players['player 2'][2])
    show_player(players['player 1'][1],players['player 1'][2],players['player 1'][0])
    show_player(players['player 2'][1],players['player 2'][2],players['player 2'][0])
    my_dice.create_button()
    pygame.display.update()
