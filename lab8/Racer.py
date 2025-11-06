import pygame
import random

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Dilnaz Racer")

clock = pygame.time.Clock()

back = pygame.image.load('images/roadd.jpg')
back = pygame.transform.scale(back, (500, 500))

player = pygame.image.load('images/pixel_racecar_purple.png')
player = pygame.transform.scale(player, (90, 90))

enemy = pygame.image.load('images/pixel_racecar_green.png')
enemy = pygame.transform.scale(enemy, (90, 90))

coin = pygame.image.load('images/coin 2.png')
coin = pygame.transform.scale(coin, (50, 50))

coinsound = pygame.mixer.Sound('images/coin.flac')
crashsound = pygame.mixer.Sound('images/crash.mp3')

font = pygame.font.Font('images/minecraft_0.ttf', 30)
gameoverfont = pygame.font.Font('images/minecraft_0.ttf', 60)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player
        self.rect = self.image.get_rect(center=(250, 380))
        self.rect.inflate_ip(-50, -50)
        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 82:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 380:
            self.rect.x += self.speed


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy
        self.rect = self.image.get_rect(center=(random.randint(82, 340), -150))
        self.rect.inflate_ip(-50, -50)
        self.speed = 7

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.y = -150
            self.rect.x = random.randint(82, 340)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin
        self.rect = self.image.get_rect(center=(random.randint(90, 350), -200))
        self.speed = 6

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.y = -200
            self.rect.x = random.randint(90, 350)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Background:
    def __init__(self, image):
        self.image = image
        self.y1 = 0
        self.y2 = -500
        self.speed = 5

    def update(self):
        self.y1 += self.speed
        self.y2 += self.speed
        if self.y1 >= 500:
            self.y1 = -500
        if self.y2 >= 500:
            self.y2 = -500

    def draw(self, surface):
        surface.blit(self.image, (0, self.y1))
        surface.blit(self.image, (0, self.y2))


player = Player()
enemy = Enemy()
coin = Coin()
background = Background(back)
allspiretes = pygame.sprite.Group()
allspiretes.add(player, enemy, coin)
enemies = pygame.sprite.Group()
enemies.add(enemy)
coins = pygame.sprite.Group()
coins.add(coin)
score = 0
gameover = False

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if not gameover:
        background.update()
        allspiretes.update()
        

        if pygame.sprite.spritecollide(player, coins, False):
            score += 1
            coinsound.play()
            coin.rect.y = -200
            coin.rect.x = random.randint(82, 380)

        if pygame.sprite.spritecollide(player, enemies, False):
            crashsound.play()
            gameover = True

        background.draw(screen)
        allspiretes.draw(screen)

        scoretext = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(scoretext, (300, 30))

    else:
        
        screen.fill((0, 0, 0))  
        gotext = gameoverfont.render("GAME OVER", True, (66, 14, 14))  
        scoretext = font.render(f"Final Score: {score}", True, (89, 6, 6))
        screen.blit(gotext, (65, 200))
        screen.blit(scoretext, (130, 280))

    pygame.display.update()