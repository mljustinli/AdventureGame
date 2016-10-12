import sys, pygame
from player import Player
from town import Town
from weapon import Weapon
from inventoryChunkMenu import InventoryChunkMenu

class Inventory():
    def __init__(self, image_file):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [0, 0]
        self.chunks = []
        self.menuSelection = "Fists"
        self.add = 0
        self.useButton = Use()
        self.outline = pygame.image.load("inventory/inventoryChunkOutline.png")
    def displayInventory(self, player, screen):
        self.chunks = []
        self.checkItems(player)
        self.createInventoryChunkMenu()
        
        for chunk in self.chunks:
            screen.blit(chunk.image, chunk.rect)
        
        self.displayOutline(screen)
        screen.blit(self.image, self.rect)
        screen.blit(self.useButton.image, self.useButton.rect)
        self.displayDescription(screen)
        print self.menuSelection
        print self.currentWeapon
    def createInventoryChunkMenu(self):
        for i in range(len(self.weapons)):
            newChunk = InventoryChunkMenu([50, (i * 100) + 50 + self.add], self.weapons[i].name)
            self.chunks.append(newChunk)
    def checkItems(self, player):
        self.weapons = player.weapons
        #can't sort because the objects have no names...
        self.weapons.sort()
        self.currentWeapon = player.currentWeapon
    def scrollUp(self):
        if self.chunks[0].rect.top < 50:
            self.add += 50
    def scrollDown(self):
        if self.chunks[len(self.chunks) - 1].rect.bottom > 440:
            self.add -= 50
    def checkSelection(self, coord, player):
        for chunk in self.chunks:
            if chunk.rect.top <= coord[1] \
            and chunk.rect.bottom >= coord[1] \
            and chunk.rect.left <= coord[0] \
            and chunk.rect.right >= coord[0]:
                self.menuSelection = chunk.name
        if self.useButton.rect.top <= coord[1] \
        and self.useButton.rect.bottom >= coord[1] \
        and self.useButton.rect.left <= coord[0] \
        and self.useButton.rect.right >= coord[0]:
            self.currentWeapon = self.menuSelection
            player.currentWeapon = self.menuSelection
    def displayDescription(self, screen):
        #self.menuSelection
        
        for weapon in self.weapons:
            if self.menuSelection == weapon.name:
                text1 = weapon.description()[0]
                text2 = weapon.description()[1]
                break
            else:
                text1 = "FUUUU"
                text2 = "FUUUUUU"
        
        font = pygame.font.Font(None, 25)
        text3 = "Current Weapon: " + self.currentWeapon
        t1 = font.render(text1, 1, (0, 0, 0))
        t2 = font.render(text2, 1, (0, 0, 0))
        t3 = font.render(text3, 1, (0, 0, 0))
        screen.blit(t1, [70, 470])
        screen.blit(t2, [70, 500])
        screen.blit(t3, [70, 530])
    def displayOutline(self, screen):
        
        for chunk in self.chunks:
            if self.menuSelection == chunk.name:
                screen.blit(self.outline, chunk.rect)
                break
            
class Use(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("inventory/equip-useChunk.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [910, 50]
    