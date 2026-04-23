import pygame
from core.entities import Player
from settings import *
from core.background import Background
from core.effect import Effect
from core.enemiesgerencer import EnemiesGerence
import time
import sys
from core.gameover import GameOver

GAME_SPEED=5

class Game:
    def __init__(self, menu):
        pygame.init()
        self.menu = menu
        self.tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.background = pygame.sprite.Group(
            Background((0,0)),
            Background((2500,0))
        )
        self.player = Player((200,200), self)
        self.enemiegerencer = EnemiesGerence(self)

        self.enemies = pygame.sprite.Group()

        self.shoot = pygame.sprite.Group()
        self.particles = pygame.sprite.Group()
        self.particles.add(Effect())

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
    
    def update(self):
        self.background.update()
        self.particles.update()
        self.player.update()
        self.enemies.update()
        self.shoot.update()
        self.enemiegerencer.update()

    def draw(self):
        self.tela.fill((0, 0, 0))
        self.background.draw(self.tela)
        self.particles.draw(self.tela)

        self.player.update()
        self.player.draw(self.tela)

        self.enemies.draw(self.tela)
        self.shoot.draw(self.tela)
        
        pygame.display.flip()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
    def game_over(self):
        gameover = GameOver(self.menu, self)
        gameover.run()