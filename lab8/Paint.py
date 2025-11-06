import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

drawing = False
startpos = (0, 0)
points = []

currenttool = 'Brush'  
color = (237, 130, 202)
radius = 5  
font = pygame.font.Font('images/minecraft_0.ttf', 30)  

screen.fill((255,255,255))

palette = [
    ((237,130,202), pygame.Rect(10,10,30,30)),  
    ((222,58,69), pygame.Rect(50,10,30,30)),    
    ((129,212,108), pygame.Rect(90,10,30,30)),   
    ((99,179,214), pygame.Rect(130,10,30,30)),   
    ((225,237,88), pygame.Rect(170,10,30,30)),  
    ((0,0,0), pygame.Rect(210,10,30,30)),        
    ((255,255,255), pygame.Rect(250,10,30,30)),  
    ((160,120,255), pygame.Rect(290,10,30,30))   
]

def drawLineBetween(screen, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    if iterations == 0:
        pygame.draw.circle(screen, color, start, width)
        return
    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                currenttool = 'Brush'
            elif event.key == pygame.K_2:
                currenttool = 'Rectangle'
            elif event.key == pygame.K_3:
                currenttool = 'Circle'
            elif event.key == pygame.K_4:
                currenttool = 'Eraser'

        if event.type == pygame.MOUSEBUTTONDOWN:
            for c,r in palette:
                if r.collidepoint(event.pos):
                    color = c
                    drawing = False
                    break

            drawing = True
            startpos = event.pos
            if currenttool in ['Brush','Eraser']:
                points = [event.pos]

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            endpos = event.pos
            if currenttool == 'Rectangle':
                rect = pygame.Rect(startpos,(endpos[0]-startpos[0], endpos[1]-startpos[1]))
                pygame.draw.rect(screen, color, rect, 2)
            elif currenttool == 'Circle':
                radiuscircle = int(((endpos[0]-startpos[0])**2 + (endpos[1]-startpos[1])**2)**0.5)
                pygame.draw.circle(screen, color, startpos, radiuscircle, 2)


    if drawing and currenttool in ['Brush','Eraser']:
        mousepos = pygame.mouse.get_pos()
        points.append(mousepos)
        points = points[-256:]
        drawcolor = color if currenttool == 'Brush' else (255,255,255)
        for i in range(len(points)-1):
            drawLineBetween(screen, points[i], points[i+1], radius, drawcolor)

    pygame.draw.rect(screen, ('white'), (330, 0, 220, 50))

    for c,r in palette:
        pygame.draw.rect(screen, c, r)
        pygame.draw.rect(screen, (0,0,0), r, 2)  

    tooltext = font.render(currenttool, True, (0, 0, 0))
    screen.blit(tooltext,(350,10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()


