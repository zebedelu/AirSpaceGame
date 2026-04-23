from core.entites.airship import Airship
import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, GAME_SPEED, img
import random
from core.effects.shoot import Shoot

class Player(Airship):
    def __init__(self, pos, game):
        super().__init__(pos)
        self.game = game
        self.EstadoAnteriorMouse = pygame.mouse.get_pressed()[0]

        self.imageflipedVertical = pygame.image.load(img("assets/images/airplaneFlipVertical.png")).convert_alpha()
        self.imageflipedVertical = pygame.transform.rotate(self.imageflipedVertical, -90)
        self.imageflipedVertical = pygame.transform.scale(self.imageflipedVertical, (60,60))
        
        self.imageflipedHorizontal = pygame.image.load(img("assets/images/airplaneFlipHorizontal.png")).convert_alpha()
        self.imageflipedHorizontal = pygame.transform.rotate(self.imageflipedHorizontal, -90)
        self.imageflipedHorizontal = pygame.transform.scale(self.imageflipedHorizontal, (60,60))

        self.imagenormal = pygame.image.load(img("assets/images/airplane.png")).convert_alpha()
        self.imagenormal = pygame.transform.rotate(self.imagenormal, -90)
        self.imagenormal = pygame.transform.scale(self.imagenormal, (60,60))

        self.image = self.imagenormal.copy()
        self.shootdelay = 10

    def update(self):
        keys = pygame.key.get_pressed()

        vel = self.speed# + (2*int(keys[pygame.K_LSHIFT]))
        if keys[pygame.K_a]:
            super().rect.x -= vel
        if keys[pygame.K_d]:
            super().rect.x += vel
        if keys[pygame.K_w]:
            super().rect.y -= vel
        if keys[pygame.K_s]:
            super().rect.y += vel
        
        if keys[pygame.K_w] or keys[pygame.K_s]:
            self.image = self.imageflipedVertical
        elif keys[pygame.K_a] or keys[pygame.K_d]:
            self.image = self.imageflipedHorizontal
        else:
            self.image = self.imagenormal

        if self.shootdelay > 0:
            self.shootdelay -= 1
            
        if (self.EstadoAnteriorMouse == False and pygame.mouse.get_pressed()[0] == True) or (keys[pygame.K_SPACE] and self.shootdelay <= 0):
            self.shootdelay = 10
            self.shoot()

        self.EstadoAnteriorMouse = pygame.mouse.get_pressed()[0]
        
        if super().rect.x < 0: super().rect.x = 0
        if super().rect.y < 0: super().rect.y = 0
        if super().rect.x > SCREEN_WIDTH-super().rect.width: super().rect.x = SCREEN_WIDTH-super().rect.width
        if super().rect.y > SCREEN_HEIGHT-super().rect.height: super().rect.y = SCREEN_HEIGHT-super().rect.height

        if pygame.sprite.spritecollideany(self, self.game.enemies):
            self.game.game_over()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def shoot(self):
        self.game.shoot.add(Shoot((self.rect.x, self.rect.y), self.game))
        self.game.shoot.add(Shoot((self.rect.x, self.rect.y+40), self.game))

class Enemie(Airship):
    def __init__(self, pos, game):
        self.inicialpos = pos[:]
        super().__init__(pos)
        self.game = game
        self.image = pygame.image.load(img("assets/images/enemie.png")).convert_alpha()
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (60,60))
        self.speedX = random.randint(1,5)
        self.speedY = random.randint(20,100)

    def update(self):
        self.speedX *= 1.001
        self.speedX = min(self.speedX, 5)
        self.rect.x -= GAME_SPEED*self.speedX
        self.rect.y += (self.game.player.rect.y - self.rect.y)/self.speedY
    
        if self.rect.x < -self.rect.height-100:
            self.game.enemies.add(Enemie((SCREEN_WIDTH, random.randint(0,SCREEN_HEIGHT)), self.game))
            self.kill()

    def explodir(self):
        self.kill()