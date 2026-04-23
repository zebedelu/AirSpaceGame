import pygame, random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_SPEED, img

class Effect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(img("assets/images/meteor.png")).convert_alpha()
        r = random.randint(10,30)
        self.image = pygame.transform.scale(self.image, (r,r))

        self.rect = self.image.get_rect(topleft=(0,0))
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_HEIGHT*3)
        self.rect.y = random.randint(0, SCREEN_HEIGHT)
        self.velocity = random.uniform(2,3)
    def update(self):
        self.rect.x -= GAME_SPEED*self.velocity

        if self.rect.x < -100:
            self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_HEIGHT*3)
            self.rect.y = random.randint(0, SCREEN_HEIGHT)