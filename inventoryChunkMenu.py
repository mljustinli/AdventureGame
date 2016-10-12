import sys, pygame

class InventoryChunkMenu(pygame.sprite.Sprite):
        def __init__(self, location, name):
            pygame.sprite.Sprite.__init__(self)
            image_surface = pygame.image.load("inventory/inventoryChunk.png")
            font = pygame.font.Font(None, 25)
            text = name
            t = font.render(text, 1, (0, 0, 0))
            image_surface.blit(t, [20, 10])
            
            self.image = image_surface.convert()
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location
            self.name = name
            
            
            