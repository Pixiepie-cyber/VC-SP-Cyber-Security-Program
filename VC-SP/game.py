import pygame, sys

pygame.init()

width = 1200
height = 800

player_speed = 5

fps = 60

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")

player = pygame.Rect(50, 50, 100, 100)

def movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] == True:
        player.move_ip(0, -player_speed)
    if keys[pygame.K_DOWN] == True:
        player.move_ip(0, player_speed)
    if keys[pygame.K_RIGHT] == True:
        player.move_ip(player_speed, 0)
    if keys[pygame.K_LEFT] == True:
        player.move_ip(-player_speed, 0)

running = True

while running:
    screen.fill((0,0,0))
    clock.tick(fps)
    pygame.draw.rect(screen, (255, 0, 0), player)

    movement()

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
            sys.exit()

    pygame.display.update()

pygame.quit()