import pygame
import random
pygame.init()

width = 600
height = 600
cell = 30

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Rect Version")

clock = pygame.time.Clock()

blue = (120, 190, 255)
green1 = (150, 230, 150)
green2 = (130, 210, 130)

foodimg = pygame.image.load("images/apple.png")
foodimg = pygame.transform.scale(foodimg, (cell, cell))

snake = [pygame.Rect(width//2, height//2, cell, cell)]
direction = (cell, 0)
eatsound=pygame.mixer.Sound('images/EatSound.ogg')
diesound=pygame.mixer.Sound('images/Diesound.ogg')

score = 0
level = 1
speed = 7

font = pygame.font.Font('images/minecraft_0.ttf', 20)
gameoverfont = pygame.font.Font('images/minecraft_0.ttf', 60)
def background():
    for y in range(0, height, cell):
        for x in range(0, width, cell):
            color = green1 if (x//cell + y//cell) % 2 == 0 else green2
            pygame.draw.rect(screen, color, (x, y, cell, cell))

def foodran():
    while True:
        fx = random.randrange(0, width, cell)
        fy = random.randrange(0, height, cell)
        fr = pygame.Rect(fx, fy, cell, cell)
        if all(not fr.colliderect(r) for r in snake):
            return fr

food = foodran()

running = True
while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, cell):
                direction = (0, -cell)
            elif event.key == pygame.K_DOWN and direction != (0, -cell):
                direction = (0, cell)
            elif event.key == pygame.K_LEFT and direction != (cell, 0):
                direction = (-cell, 0)
            elif event.key == pygame.K_RIGHT and direction != (-cell, 0):
                direction = (cell, 0)

    head = snake[0].copy()
    head.x += direction[0]
    head.y += direction[1]

    if head.x < 0 or head.x >= width or head.y < 0 or head.y >= height:
        diesound.play()
        running = False

    for r in snake:
        if head.colliderect(r):
            diesound.play()
            running = False

    snake.insert(0, head)

    if head.colliderect(food):
        score += 1
        eatsound.play()

        if score % 4 == 0:
            level += 1
            speed += 2
        food = foodran()
    else:
        snake.pop()

    background()

    for r in snake:
        pygame.draw.rect(screen, blue, r)

    screen.blit(foodimg, food)
    text = font.render(f"Score: {score}   Level: {level}", True, (0,0,0))
    screen.blit(text, (8,8))
    pygame.display.update()

else:    
   screen.fill((150, 230, 150))  

   gotext = gameoverfont.render("GAME OVER", True, 'black')  
   leveltext = font.render(f"LEVEL: {level}", True, 'black')
   scoretext = font.render(f"SCORE: {score}", True, 'black')

screen.blit(gotext, (120, 200))
screen.blit(leveltext, (210, 300))
screen.blit(scoretext, (210, 340))

pygame.display.update()
pygame.time.delay(3000)


pygame.quit()
