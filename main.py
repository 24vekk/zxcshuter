import pygame
from scripts.player import Player


flags = pygame.RESIZABLE | pygame.SCALED
window = pygame.display.set_mode((800, 600), flags)
clock = pygame.time.Clock()

FPS = 60

background = pygame.image.load('images\\background.png')
background = pygame.transform.scale(background, (800, 600))
enemy = pygame.image.load('images\\enemy.png')
bullet = pygame.image.load('images\\bullet.png')
player_image = pygame.image.load('images\\player.png')

player_image = pygame.transform.scale(player_image, (75, 75))
player = Player(400, 550, player_image, 5)

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player.update()

    window.blit(background, (0, 0))
    player.render(window)

    pygame.display.update()
    clock.tick(FPS)