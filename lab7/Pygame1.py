import pygame
from datetime import datetime 
pygame.init() 
screen = pygame.display.set_mode((600,500)) 
pygame.display.set_caption("Mickey Clock") 
image = pygame.image.load('images/mmm.jpg') 
image= pygame.transform.scale(image, (600, 500)) 
mhand = pygame.image.load('images/min_hand.png') 
mhand= pygame.transform.scale(mhand, (560,680)) 
shand = pygame.image.load('images/sec_hand.png') 
shand= pygame.transform.scale(shand, (540,630)) 
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            exit() 
    screen.blit(image, (0,0)) 
    now = datetime.now() 
    minutes = now.minute 
    seconds = now.second 
    mangle = -minutes * 6 
    sangle = -seconds * 6 
    rotatedm = pygame.transform.rotate(mhand, mangle) 
    rotateds = pygame.transform.rotate(shand, sangle) 
    mrect = rotatedm.get_rect(center=(300,250)) 
    srect = rotateds.get_rect(center=(300,250)) 
    screen.blit(rotatedm, mrect) 
    screen.blit(rotateds, srect) 
    pygame.display.update()





