from .sprite import Sprite
import pygame

class Player(Sprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= 8
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += 8
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= 8
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += 8
    def __init__(self, x, y, image, speed, health):
        super().__init__(x, y, image, speed)
        self.health = health
    def get_damage(self):
        self.health -= 1