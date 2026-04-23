import pygame
from settings import GAME_SPEED, img

class Background(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(img("assets/images/bg.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (2500,500))
        self.rect = self.image.get_rect(topleft=pos)
    def update(self):
        self.rect.x -= GAME_SPEED
        if self.rect.x < -self.rect.width:
            self.rect.x += self.rect.width * 2