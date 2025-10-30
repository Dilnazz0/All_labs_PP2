import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
back=pygame.image.load('images/screen.jpg')
back= pygame.transform.scale(back, (400, 300))
pygame.display.set_caption("Music Player")

songs = ['images/StrangerThings.mp3','images/StrangerThings2.mp3','images/StrangerThings3.mp3']
a = 0
pygame.mixer.music.load(songs[a])

play = pygame.image.load("images/play.png")
prev = pygame.image.load("images/prev.png")
stop = pygame.image.load("images/stop.png")   
next = pygame.image.load("images/next.png")

playi = pygame.transform.scale(play, (60, 60))
previ = pygame.transform.scale(prev, (60, 60))
stopi = pygame.transform.scale(stop, (60, 60))
nexti = pygame.transform.scale(next, (60, 60))

playr = playi.get_rect(center=(200, 150))
prevr = previ.get_rect(center=(130, 150))
nextr = nexti.get_rect(center=(265, 150))
stopr = stopi.get_rect(center=(330, 150))

playing=False

while True:
    screen.blit(back, (0,0))
    if playing:
        screen.blit(stopi, playr)
    else:
        screen.blit(playi, playr)

    screen.blit(previ, prevr)
    screen.blit(nexti, nextr)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = event.pos

            if playr.collidepoint(mousepos):
                if not playing:
                    pygame.mixer.music.play()
                    playing=True
                else:
                    pygame.mixer.music.pause()
                    playing=False

            elif stopr.collidepoint(mousepos):
                pygame.mixer.music.stop()

            elif nextr.collidepoint(mousepos):
                a = (a + 1) % len(songs)
                pygame.mixer.music.load(songs[a])
                pygame.mixer.music.play()

            elif prevr.collidepoint(mousepos):
                a = (a - 1) % len(songs)
                pygame.mixer.music.load(songs[a])
                pygame.mixer.music.play()
            #elif event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_p:  # Play
                #pygame.mixer.music.play()
            #elif event.key == pygame.K_s:  # Stop
                #pygame.mixer.music.stop()
            #elif event.key == pygame.K_n:  # Next
                #a = (a + 1) % len(songs)
                #pygame.mixer.music.load(songs[a])
                #pygame.mixer.music.play()
            #elif event.key == pygame.K_b:  # Previous
                #a = (a - 1) % len(songs)
                #pygame.mixer.music.load(songs[a])
                #pygame.mixer.music.play()
    pygame.display.update()






