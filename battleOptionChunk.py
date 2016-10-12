import sys, pygame
from player import Player

class BattleOptionChunk(pygame.sprite.Sprite):
    def __init__(self, location, name):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.image.load("fight/battleOptionChunk.png")
        font = pygame.font.Font(None, 25)
        text = name
        t = font.render(text, 1, (0, 0, 0))
        image_surface.blit(t, [20, 20])
        
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.name = name
        
        