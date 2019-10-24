import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0,255,0)

MARGIN = 5
WIDTH = 20
HEIGHT = 20
grid = []
for row in range(10):
    grid.append([])
    for col in range(10):
        grid[row].append(0)
grid[1][5] = 1
pygame.init()
size = [255,255]
screen = pygame.display.set_mode(size)

running = False
clock = pygame.time.Clock()

while not running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // (MARGIN + WIDTH)
            row = pos[1] // (MARGIN + HEIGHT)
            grid[row][col] = 1
            print("Clicked: ", pos, row, col)
    screen.fill(BLACK)


    for row in range(10):
        for col in range(10):
            color = WHITE
            if grid[row][col] == 1:
                color = GREEN
            pygame.draw.rect(screen, 
            color, 
            [ (MARGIN + WIDTH) * col + MARGIN,
            (MARGIN + HEIGHT) * row + MARGIN,
            WIDTH,
            HEIGHT
            ])

    clock.tick(60)

    pygame.display.flip()

pygame.quit()



        