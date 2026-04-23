import pygame, time
from settings import img
import sys

class GameOver:
    def __init__(self, menu, game):
        self.menu = menu
        self.game = game
    def run(self):
        self.load_render()
        while True:
            self.render()
            self.render_clicks(pygame.mouse.get_pos())
            self.handle_events()
            pygame.display.flip()
            self.game.tela.fill((0,0,0))
            self.game.clock.tick(60)
    
    def load_render(self):
        self.gameovertitle = pygame.image.load(img("assets/menu/gameover.png")).convert_alpha()
        self.gameovertitle = pygame.transform.scale(self.gameovertitle, (300,200))

        self.RetryButton = pygame.image.load(img("assets/menu/retry.png")).convert_alpha()
        self.RetryButton = pygame.transform.scale(self.RetryButton, (300,100))

        self.BackMenu = pygame.image.load(img("assets/menu/sair.png")).convert_alpha()
        self.BackMenu = pygame.transform.scale(self.BackMenu, (300,100))
        
    def render_clicks(self, mousePosition):
        for surf, rect, acao in self.buttons:
            if rect.collidepoint(mousePosition):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if pygame.mouse.get_pressed()[0]:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    acao()
                return
            
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    
    def render(self):
        self.game.tela.blit(self.gameovertitle, (250, 70))

        retry_rect = self.RetryButton.get_rect(topleft=(450, 350))
        self.game.tela.blit(self.RetryButton, (450, 350))

        back_rect = self.BackMenu.get_rect(topleft=(100, 350))
        self.game.tela.blit(self.BackMenu, (100, 350))

        self.buttons = [(self.RetryButton, retry_rect, self.menu.start),
                        (self.BackMenu, back_rect, self.menu.run)]
        
    def GoToMenu(self):
        self.menu.run()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()