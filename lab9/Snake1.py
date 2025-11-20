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

foods = [
    ("images/apple.png", 1),
    ("images/watermelon.png", 2),
    ("images/cherry.png", 3),
    ("images/grape.png", 4),
]

snake = [pygame.Rect(width//2, height//2, cell, cell)]
direction = (cell, 0)

eatsound = pygame.mixer.Sound('images/EatSound.ogg')
diesound = pygame.mixer.Sound('images/Diesound.ogg')

score = 0
level = 1
speed = 7

font = pygame.font.Font('images/minecraft_0.ttf', 20)
gameoverfont = pygame.font.Font('images/minecraft_0.ttf', 60)

foodtime = 5  

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
            imgpath, weight = random.choice(foods)
            imgfood = pygame.image.load(imgpath)
            imgfood = pygame.transform.scale(imgfood, (cell, cell))
            return fr, imgfood, weight

food, imgfood, foodweight = foodran()
foodtimer = foodtime * speed

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

    for r in snake[1:]:
        if head.colliderect(r):
            diesound.play()
            running = False

    snake.insert(0, head)

    foodtimer -= 1

    if head.colliderect(food) or foodtimer <= 0:
        if head.colliderect(food):
            score += foodweight
            eatsound.play()
            newlevel = score // 8 + 1
            if newlevel > level:
                level = newlevel
                speed += 2  
        food, imgfood, foodweight = foodran()
        foodtimer = foodtime * speed
    else:
        snake.pop()

    background()
    for r in snake:
        pygame.draw.rect(screen, blue, r)
    screen.blit(imgfood, food)
    text = font.render(f"Score: {score}   Level: {level}", True, (0,0,0))
    screen.blit(text, (8,8))
    pygame.display.update()

screen.fill((150, 230, 150))
gotext = gameoverfont.render("GAME OVER", True, 'black')  
leveltext = font.render(f"LEVEL: {level}", True, 'black')
scoretext = font.render(f"SCORE: {score}", True, 'black')

screen.blit(gotext, (120, 200))
screen.blit(leveltext, (250, 300))
screen.blit(scoretext, (250, 340))

pygame.display.update()
pygame.time.delay(3000)
pygame.quit()
