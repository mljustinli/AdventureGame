import sys, pygame

class Monster(pygame.sprite.Sprite):
    def __init__(self, image_file, name, strength, hp):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.image_file = image_file
        self.name = name
        self.strength = strength
        self.hp = hp
        self.maxhp = float(hp)
        self.type = "Monster"