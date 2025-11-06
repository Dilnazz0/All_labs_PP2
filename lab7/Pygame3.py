import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Window")

headi = pygame.image.load("images/head5.png")
headi = pygame.transform.scale(headi, (100, 100))
headr = headi.get_rect(center=(400, 300))

while True:
    screen.fill('White')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and headr.top > 0:
                        headr.y -= 20
            elif event.key == pygame.K_DOWN and headr.bottom < 600:
                        headr.y += 20
            elif event.key == pygame.K_LEFT and headr.left > 0:
                        headr.x -= 20
            elif event.key == pygame.K_RIGHT and headr.right < 800:
                        headr.x += 20

    
    screen.blit(headi, headr)
    pygame.display.update()

