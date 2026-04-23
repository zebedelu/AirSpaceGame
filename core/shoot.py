import pygame
from settings import GAME_SPEED, SCREEN_WIDTH, img

class Shoot(pygame.sprite.Sprite):
    def __init__(self, pos, game):
        super().__init__()
        self.image = pygame.image.load(img("assets/images/shoot.png")).convert_alpha()
        self.game = game
        self.rect = self.image.get_rect(topleft=pos)
        
    def update(self):
        self.rect.x += GAME_SPEED*10
        if self.rect.x > SCREEN_WIDTH:
            self.kill()

        # detectar colisão
        todos_colidiram = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if todos_colidiram:
            for colisor in todos_colidiram:
                colisor.explodir()
                self.kill()