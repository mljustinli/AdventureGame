import sys, pygame
import time
from weapon import Weapon

class Player(pygame.sprite.Sprite):
    def __init__(self, image_file, location, town, screenLocation):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.town = town
        self.screenLocation = screenLocation
        self.changePic = False
        self.direction = "up"
        self.time = time.time()
        self.image_file = image_file
        self.cycle = 0
        self.hp = 100
        self.maxhp = 100.0
        self.type = "Player"
        self.strength = 14
        self.beforeBattle = [0, 0]
        #add weapons here
        self.weapons = [Weapon(8, "Fists"), \
                        Weapon(20, "Long Sword"), \
                        Weapon(1000, "Salad"), \
                        Weapon(1001, "Banana"), \
                        Weapon(5, "Mouth")]
        self.currentWeapon = "Banana"
        self.rect.center = location
        self.dead = False
        self.pause = False
        self.pauseTime = 0
    def changeState(self):
        numCycles = 4
        #only slightly hardcodey *cough cough cough*
        
        if time.time() - self.time > 0.1:
            if self.direction == "up":
                if self.image_file == "player/playerBack1.png":
                    self.changeImage("player/playerBack2.png", self.rect.center)
                else:
                    self.changeImage("player/playerBack1.png", self.rect.center)
                self.cycle += 1
            elif self.direction == "down":
                if self.image_file == "player/playerFront1.png":
                    self.changeImage("player/playerFront2.png", self.rect.center)
                else:
                    self.changeImage("player/playerFront1.png", self.rect.center)
                self.cycle += 1
            elif self.direction == "left":
                if self.image_file == "player/playerSide4.png":
                    self.changeImage("player/playerSide5.png", self.rect.center)
                elif self.image_file == "player/playerSide5.png":
                    self.changeImage("player/playerSide6.png", self.rect.center)
                elif self.image_file == "player/playerSide6.png":
                    self.changeImage("player/playerSide4.png", self.rect.center)
                else:
                    self.image_file = "player/playerSide4.png"
                self.cycle += 1
            elif self.direction == "right":
                if self.image_file == "player/playerSide1.png":
                    self.changeImage("player/playerSide2.png", self.rect.center)
                elif self.image_file == "player/playerSide2.png":
                    self.changeImage("player/playerSide3.png", self.rect.center)
                elif self.image_file == "player/playerSide3.png":
                    self.changeImage("player/playerSide1.png", self.rect.center)
                else:
                    self.image_file = "player/playerSide1.png"
                self.cycle += 1
                
            self.time = time.time()
        if self.cycle >= numCycles:
            self.changePic = False
            self.cycle = 0
    
    def changeImage(self, image_file, coord):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = coord
        self.image_file = image_file
        
        