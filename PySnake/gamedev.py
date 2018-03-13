
import pygame
import time
import random
 
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green=(0,155,0)

display_width = 800
display_height = 600

gamedisplay = pygame.display.set_mode((display_width,display_height))

icon = pygame.image.load(r'G:\Python\pygames\icon.png')

pygame.display.set_icon(icon)

pygame.display.set_caption('Killer')

gameexit  = False 

img = pygame.image.load(r'G:\Python\pygames\snake.png')
apple = pygame.image.load(r'G:\Python\pygames\apple.png')
clock = pygame.time.Clock()

block_size =20
FPS = 15
smallfont = pygame.font.SysFont('comicsansms',25)
mediumfont = pygame.font.SysFont('comicsansms',40)
largefont = pygame.font.SysFont('comicsansms',60)


direction="right"


def snake(block_size,snakelist):
    if(direction == "right"):
        head=pygame.transform.rotate(img,270)
    if(direction == "left"):
        head=pygame.transform.rotate(img,90)
    if(direction == "up"):
        head=img
    if(direction == "down"):
        head=pygame.transform.rotate(img,180)
    
    gamedisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        
         pygame.draw.rect(gamedisplay,green,[XnY [0],XnY[1],block_size,block_size])
        
def objects(text,color,size):
    if (size == 'small'): 
        textsurface = smallfont.render(text,True,color)
    if (size == 'medium'): 
        textsurface = mediumfont.render(text,True,color)
    if (size == 'large'): 
        textsurface = largefont.render(text,True,color)
    return textsurface,textsurface.get_rect()

def message_to_screen(msg,color,y_displace=0,size="small"):
    textsurface,textrect = objects(msg,color,size)
    #screen_text = font.render(msg,True,color)
    #gamedisplay.blit(screen_text,(display_width/2,display_height/2))
    textrect.center=(display_width/2),(display_height/2)+y_displace
    gamedisplay.blit(textsurface,textrect)


    
def intro():
    intro= True

    while intro == True:
        gamedisplay.fill(white)
        
        message_to_screen("Welcome to PySnake !!!",red,-50,size='large')
        message_to_screen("  Press C to Start. Q to Quit",black,50,size='medium')

        pygame.display.update()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = False
                    gameexit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro= False
                        gameLoop()
                    if event.key == pygame.K_q:
                        gameexit = True
                        gameover = False
        clock.tick(15)

        
    
def gameLoop():
    
    

    gameexit = False
    gameover = False

    lead_x = display_width/2
    lead_y = display_height/2
    lead_xchange = 10
    lead_ychange = 0
    
    snakelist=[]
    snakeLength = 1

    randAppleX = round(random.randrange(0,display_width-block_size))
    randAppleY = round(random.randrange(0,display_height-block_size))

    
    while not gameexit:
        global direction
        
        
        while gameover == True:
            gamedisplay.fill(white)
            
            message_to_screen("Game Over !!!",red)
            message_to_screen("  Press C to Play Again. Q to Quit",black,50)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = False
                    gameexit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        
                        gameLoop()
                    if event.key == pygame.K_q:
                        
                        gameexit = True
                        gameover = False
                        
                    
                    
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameexit = True
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LEFT :
                     direction = "left"
                     lead_xchange = -block_size
                     lead_ychange = 0
                 elif event.key == pygame.K_RIGHT :
                     direction = "right"
                     lead_xchange = +block_size
                     lead_ychange = 0
                 elif event.key == pygame.K_UP :
                     direction = "up"
                     lead_ychange = -block_size
                     lead_xchange = 0
                 elif event.key == pygame.K_DOWN :
                     direction = "down"
                     lead_ychange = +block_size
                     lead_xchange = 0

             if lead_x >= display_width or lead_x<=0 or lead_y >= display_height or lead_y<=0:
                 gameexit = False
                 gameover = True
          
                     

        lead_x +=lead_xchange
        lead_y +=lead_ychange  
        thickness=20
        gamedisplay.fill(white)
        gamedisplay.blit(apple,(randAppleX,randAppleY))
        #pygame.draw.rect(gamedisplay,red,[randAppleX,randAppleY,thickness,thickness])

        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakelist.append(snakeHead)
        if(len(snakelist)>snakeLength):
            del snakelist[0]

        for eachSegment in snakelist[:-1]:
            if eachSegment == snakeHead:
                gameover = True
            
            
            
        snake(block_size,snakelist )
        pygame.display.update()

        if lead_x>=randAppleX and lead_x<=randAppleX+thickness or lead_x+block_size>=randAppleX and lead_x+block_size<=randAppleX+thickness:
                if lead_y>=randAppleY and lead_y<=randAppleY+thickness:
                    randAppleX = round(random.randrange(0,display_width-block_size))
                    randAppleY = round(random.randrange(0,display_height-block_size))
                    snakeLength += 1
                elif lead_y+block_size>=randAppleY and lead_y+block_size<=randAppleY+thickness:
                    randAppleX = round(random.randrange(0,display_width-block_size))
                    randAppleY = round(random.randrange(0,display_height-block_size))
                    snakeLength += 1
                
    
                   

        clock.tick(FPS)
         
       
          #print(event)
    

    pygame.quit()
    quit()

intro()
gameLoop()

