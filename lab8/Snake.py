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

food_img = pygame.image.load("images/apple.png")
food_img = pygame.transform.scale(food_img, (cell, cell))

snake = [pygame.Rect(width//2, height//2, cell, cell)]
direction = (cell, 0)

score = 0
level = 1
speed = 7

font = pygame.font.Font('images/minecraft_0.ttf', 20)
gameoverfont = pygame.font.Font('images/minecraft_0.ttf', 60)
def draw_background():
    for y in range(0, height, cell):
        for x in range(0, width, cell):
            color = green1 if (x//cell + y//cell) % 2 == 0 else green2
            pygame.draw.rect(screen, color, (x, y, cell, cell))

def spawn_food():
    while True:
        fx = random.randrange(0, width, cell)
        fy = random.randrange(0, height, cell)
        fr = pygame.Rect(fx, fy, cell, cell)
        if all(not fr.colliderect(r) for r in snake):
            return fr

food = spawn_food()

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
        running = False

    for r in snake:
        if head.colliderect(r):
            running = False

    snake.insert(0, head)

    if head.colliderect(food):
        score += 1
        if score % 4 == 0:
            level += 1
            speed += 2
        food = spawn_food()
    else:
        snake.pop()

    draw_background()

    for r in snake:
        pygame.draw.rect(screen, blue, r)

    screen.blit(food_img, food)
    text = font.render(f"Score: {score}   Level: {level}", True, (0,0,0))
    screen.blit(text, (8,8))
    pygame.display.update()

    
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
