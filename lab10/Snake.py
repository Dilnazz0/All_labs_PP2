import pygame
import random
import psycopg2  

pygame.init()

width = 600
height = 600
cell = 30

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Rect Version")

connection = psycopg2.connect(
    host="localhost",
    database="lab10bd",
    user="postgres",
    password="123456"
)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username VARCHAR(50) PRIMARY KEY
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_score(
    username VARCHAR(50) REFERENCES users(username),
    score INT,
    level INT,
    
    PRIMARY KEY(username)
);
""")
cursor.execute("""
ALTER TABLE user_score
ADD COLUMN IF NOT EXISTS snake_length INT DEFAULT 1;
""")
connection.commit()
print("Snake tables ready!")

username = input("Enter username: ")
cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
user = cursor.fetchone()
if user is None:
    cursor.execute("INSERT INTO users(username) VALUES(%s)", (username,))
    connection.commit()
    print("New user created!")
else:
    print("Welcome back!,", username)

cursor.execute("SELECT score, level, snake_length FROM user_score WHERE username=%s", (username,))
saved = cursor.fetchone()
if saved:
    score, level, length = saved
    snake = [pygame.Rect(300 - i*cell, 300, cell, cell) for i in range(length)]
else:
    score = 0
    level = 1
    snake = [pygame.Rect(300, 300, cell, cell)]

direction = (cell, 0)
clock = pygame.time.Clock()

blue = (120, 190, 255)
green1 = (150, 230, 150)
green2 = (130, 210, 130)
wallcolor = (0,0,0)  

foods = [
    ("images/apple.png", 1),
    ("images/watermelon.png", 2),
    ("images/cherry.png", 3),
    ("images/grape.png", 4),
]

base_speed = 4

eatsound = pygame.mixer.Sound('images/EatSound.ogg')
diesound = pygame.mixer.Sound('images/Diesound.ogg')

font = pygame.font.Font('images/minecraft_0.ttf', 20)
gameoverfont = pygame.font.Font('images/minecraft_0.ttf', 60)

foodtime = 5  

def background():
    for y in range(0, height, cell):
        for x in range(0, width, cell):
            color = green1 if (x//cell + y//cell) % 2 == 0 else green2
            pygame.draw.rect(screen, color, (x, y, cell, cell))

def drawwalls(walls):
    for w in walls:
        pygame.draw.rect(screen, wallcolor, w)

def foodran(snake,walls):
    while True:
        fx = random.randrange(0, width, cell)
        fy = random.randrange(0, height, cell)
        fr = pygame.Rect(fx, fy, cell, cell)
        if all(not fr.colliderect(s) for s in snake) and all(not fr.colliderect(w) for w in walls):
            imgpath, weight = random.choice(foods)
            imgfood = pygame.image.load(imgpath)
            imgfood = pygame.transform.scale(imgfood, (cell, cell))
            return fr, imgfood, weight

def flevel(score):
    if score < 16:
        return 1
    elif score < 26:
        return 2
    else:
        return 3

def fspeed(level):
    return base_speed + (level-1)*2

def ffoodtimer(level):
    if level == 3:
        return foodtime * fspeed(level)
    else:
        return None

def genwalls(level, snake):
    walls = []
    numblocks = 0
    if level == 2:
        numblocks = 2
    elif level == 3:
        numblocks = 4
    else:
        return walls

    for _ in range(numblocks):
        while True:
            x = random.randint(0, (width // cell) - 2) * cell
            y = random.randint(0, (height // cell) - 2) * cell
            w = random.randint(1,3) * cell
            h = random.randint(2,3) * cell
            newblock = pygame.Rect(x, y, w, h)
            if all(not newblock.colliderect(s) for s in snake):
                walls.append(newblock)
                break
    return walls

start = True
while start:
    screen.fill((150, 230, 150))
    
    titletext = gameoverfont.render("SNAKE GAME", True, 'black')
    screen.blit(titletext, (100, 50))
    
    infotext = font.render(f"User: {username}  Level: {level}  Score: {score}", True, 'black')
    screen.blit(infotext, (130, 150))
    
    optiontext1 = font.render("Press 'S' to Start ", True, 'black')
    optiontext2 = font.render("Press 'R' to Restart", True, 'black')
    optiontext3 = font.render("Press 'C' to Continue", True, 'black')
    
    screen.blit(optiontext1, (180, 250))
    screen.blit(optiontext2, (180, 300))
    screen.blit(optiontext3, (180, 350))
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            connection.close()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                score = 0
                level = 1
                snake = [pygame.Rect(300, 300, cell, cell)]
                direction = (cell, 0)
                start = False
            elif event.key == pygame.K_r:
                score = 0
                level = 1
                snake = [pygame.Rect(300, 300, cell, cell)]
                direction = (cell, 0)
                cursor.execute("""
                   INSERT INTO user_score(username, score, level, snake_length)
                   VALUES (%s, %s, %s, %s)
                   ON CONFLICT (username) DO UPDATE SET
                   score = EXCLUDED.score,
                   level = EXCLUDED.level,
                   snake_length = EXCLUDED.snake_length;
                """, (username, score, level, len(snake)))
                connection.commit()
                start = False
            elif event.key == pygame.K_c:
                start = False

walls = genwalls(level, snake)
food, imgfood, foodweight = foodran(snake,walls)
level = flevel(score)
speed = fspeed(level)
foodtimer = ffoodtimer(level)

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
            elif event.key == pygame.K_p:
                cursor.execute("""
                    INSERT INTO user_score(username, score, level, snake_length)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (username) DO UPDATE SET
                        score = EXCLUDED.score,
                        level = EXCLUDED.level,
                        snake_length = EXCLUDED.snake_length;
                """, (username, score, level, len(snake)))
                connection.commit()

                paused = True
                while paused:
                    screen.fill((150, 230, 150))
                    pausetext = gameoverfont.render("PAUSE", True, 'black')
                    screen.blit(pausetext, (300,200))
                    continuetext = font.render("Press 'C' to Continue", True, 'black')
                    screen.blit(continuetext, (300,300))
                    pygame.display.update()

                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            paused = False
                            running = False
                        if e.type == pygame.KEYDOWN:
                            if e.key == pygame.K_c: 
                                paused = False

    head = snake[0].copy()
    head.x += direction[0]
    head.y += direction[1]

    for w in walls:
        if head.colliderect(w):
            diesound.play()
            running = False
    if head.x < 0 or head.x >= width or head.y < 0 or head.y >= height:
        diesound.play()
        running = False
    for r in snake[1:]:
        if head.colliderect(r):
            diesound.play()
            running = False

    snake.insert(0, head)

    if foodtimer is not None:
        foodtimer -= 1

    if head.colliderect(food) or (foodtimer is not None and foodtimer <= 0):
        if head.colliderect(food):
            score += foodweight
            eatsound.play()
        walls = genwalls(level, snake)
        food, imgfood, foodweight = foodran(snake,walls)
        foodtimer = ffoodtimer(level)
        level = flevel(score)
        speed = fspeed(level)
    else:
        snake.pop()

    background()
    drawwalls(walls)
    for r in snake:
        pygame.draw.rect(screen, blue, r)
    screen.blit(imgfood, food)
    text = font.render(f"Score: {score}   Level: {level}", True, (0,0,0))
    screen.blit(text, (8,8))
    pygame.display.update()

cursor.execute("""
    INSERT INTO user_score(username, score, level, snake_length)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (username) DO UPDATE SET
        score = EXCLUDED.score,
        level = EXCLUDED.level,
        snake_length = EXCLUDED.snake_length;
""", (username, score, level, len(snake)))
connection.commit()
connection.close()

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
