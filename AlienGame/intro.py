import pygame
import game_stats
import time
import alien_invasion
from alien_invasion import AlienInvasion
clock = pygame.time.Clock() 
display_width = 1200
display_height = 800

ship = pygame.image.load('images/Blue.png')

x =  (680)
y = (300)

update = AlienInvasion()
purple =(106,13,173)
pink =(255,100,180)
white =(255,255,255)
black =(0,0,0) 
red =(139,0,0)
def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

gameDisplay = pygame.display.set_mode((display_width,display_height))
def game_intro():

    intro = True
    

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #########################
        
        gameDisplay.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Space Wars", largeText)
        TextRect.center = ((display_width/2+140),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(ship,(x,y))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        print(mouse)

        if mouse[0] in range (470,570) and mouse[1] in range (480,580):
            pygame.draw.rect(gameDisplay, pink,(470,480,100,50))
            pygame.draw.rect(gameDisplay, pink,(870,480,100,50))
            #logic for if the mouse clicks on the go button
            if click[0] ==1:
                #update._check_events()
                intro = False
                
                
                
                
        elif mouse[0] in range (870,970) and mouse[1] in range (480,580):
            pygame.draw.rect(gameDisplay, pink,(470,480,100,50))
            pygame.draw.rect(gameDisplay, pink,(870,480,100,50))
        else:
            pygame.draw.rect(gameDisplay, purple,(470,480,100,50))   
            pygame.draw.rect(gameDisplay, purple,(870,480,100,50))

        goText = pygame.font.Font("freesansbold.ttf",20)
        exitText= pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("start!", goText)

        textRect.center = (520),(505)
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)
