import pygame
from settings import SCREEN_WIDTH, img
from core.entities import Enemie
import random

class EnemiesGerence():
    def __init__(self, game):
        self.game = game

    def update(self):
        if len(list(self.game.enemies)) == 0:
            self.game.enemies = pygame.sprite.Group()
            NumeroDeInimigos = random.randint(3,15)
            for i in range(NumeroDeInimigos):
                self.game.enemies.add(Enemie((random.randint(SCREEN_WIDTH,SCREEN_WIDTH*5), 500/NumeroDeInimigos*i), self.game))