import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, img
from core.game.game import Game
import sys, os

class Menu:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                                        # -2147483648*int(SCREEN_FULLSCREEN))
        pygame.display.set_caption('AirSpaceGame (ASG v1)')
        self.clock = pygame.time.Clock()
        self.buttons = []
        pygame.mouse.set_visible(True)
    
    def run(self):
        self.load_buttons()
        while True:
            self.render_buttons()
            self.render_clicks(pygame.mouse.get_pos())
            self.handle_events()
            pygame.display.flip()
            self.tela.fill((11,10,10))
            self.clock.tick(FPS)
        
    def render_clicks(self, mousePosition):
        for surf, rect, acao in self.buttons:
            if rect.collidepoint(mousePosition):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if pygame.mouse.get_pressed()[0]:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    acao()
                return
            
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    
    def load_buttons(self):
        self.title = pygame.image.load(img("assets/menu/title.png")).convert_alpha()
        self.title = pygame.transform.scale(self.title, (350,350))
        self.startButton = pygame.image.load(img("assets/menu/start.png")).convert_alpha()
        self.startButton = pygame.transform.scale(self.startButton, (300,100))
        self.ranking = pygame.image.load(img("assets/menu/ranking.png")).convert_alpha()
        self.ranking = pygame.transform.scale(self.ranking, (300,100))
        self.sair = pygame.image.load(img("assets/menu/sair.png")).convert_alpha()
        self.sair = pygame.transform.scale(self.sair, (300,100))

    def render_buttons(self):
        self.tela.blit(self.title, (50,50))

        start_rect = self.startButton.get_rect(topleft=(470,40))
        self.tela.blit(self.startButton, start_rect)

        ranking_rect = self.ranking.get_rect(topleft=(470,200))
        self.tela.blit(self.ranking, ranking_rect)

        sair_rect = self.sair.get_rect(topleft=(470,360))
        self.tela.blit(self.sair, sair_rect)

        self.buttons = [
            (self.startButton, start_rect, self.start),
            (self.ranking, ranking_rect, self.openyoutube),
            (self.sair, sair_rect, sys.exit)
        ]
    def openyoutube(self):
        os.system("start brave.exe youtube.com")

    def start(self):
        Game(self).run()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()