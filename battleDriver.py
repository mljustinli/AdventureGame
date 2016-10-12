import sys, pygame
from player import Player
from town import Town
from battleOptionChunk import BattleOptionChunk
from time import sleep

class Battle():
    def __init__(self):
        self.battleOver = False
        self.turn = "Player"
        self.barBits = []
        self.options = []
        self.battleSelection = ""
    
    def battleDone(self):
        return self.battleOver
    
    def doBattle(self, player, monster, passObject, screen, battleList):
        self.area = passObject.name
        
        names = {"Pass 1": "fight/battleScreenTree.png"}
        
        for name in names:
            if self.area == name:
                self.image_file = names[name]
                break
            else:
                self.image_file = "fight/battleScreenTree.png"
        self.drawBackground(screen)
        self.doBattleStuff(player, monster, screen, battleList)
        self.drawStatus(player, screen)
        self.drawStatus(monster, screen)
        
    def drawBackground(self, screen):
        self.image = pygame.image.load(self.image_file)
        screen.blit(self.image, [0, 0])
    def drawStatus(self, character, screen):
        percentage = character.hp / character.maxhp
        if percentage >= 0.50:
            color = "green"
        elif percentage >= 0.25:
            color = "yellow"
        elif percentage >= 0.1:
            color = "red"
        else:
            color = "red"
        
        for i in range(35):
            if i / 35.0 <= percentage:
                if character.type == "Monster":
                    newBit = Bar([1040 - i * 10, 50], color)
                elif character.type == "Player":
                    newBit = Bar([i * 10, 50], color)
            
                screen.blit(newBit.image, newBit.rect)
        
        print character.hp, character.type
    
    def drawText(self, text, screen):
        
        #paint over in black
        image_surface = pygame.surface.Surface([1050, 100])
        image_surface.fill([0, 0, 0])
        image = image_surface.convert()
        screen.blit(image, [0, 530])
        
        font = pygame.font.Font(None, 25)
        t = font.render(text, 1, (255, 255, 255))
        screen.blit(t, [30, 550])
        
    def displayGUI(self, screen, player):
        self.options = []
        
        self.options.append(BattleOptionChunk([0, 360], "Attack"))
        self.options.append(BattleOptionChunk([0, 430], "Run Away"))
        
        for chunk in self.options:
            screen.blit(chunk.image, chunk.rect)
        
    def checkClick(self, coord):
        for chunk in self.options:
            if chunk.rect.top <= coord[1] \
            and chunk.rect.bottom >= coord[1] \
            and chunk.rect.left <= coord[0] \
            and chunk.rect.right >= coord[0]:
                self.battleSelection = chunk.name
                
    def playerAttack(self, player, monster):
        for weapon in player.weapons:
            if player.currentWeapon == weapon.name:
                monster.hp -= weapon.power + player.strength
                break
            
    def findDamage(self, player):
        for weapon in player.weapons:
            if player.currentWeapon == weapon.name:
                return weapon.power
                break
            
    def monsterAttack(self, player, monster):
        player.hp -= monster.strength
    
    def checkDeaths(self, player, monster, battleList, screen):
        if monster.hp <= 0:
            text = "You killed the " + monster.name + "!"
            self.drawText(text, screen)
            player.pause = True
            player.pauseTime = 1
            
            while len(battleList) >= 1:
                battleList.remove(battleList[0])
        elif player.hp <= 0:
            player.dead = True
            
    def drawPlayer(self, player, screen):
        image = pygame.image.load("player/battlePlayer.png")
        screen.blit(image, [120, 130])
        
    def drawMonster(self, monster, screen):
        
        coords = {"Glop": [700, 290]}
        
        screen.blit(monster.image, coords[monster.name])
    
    def doBattleStuff(self, player, monster, screen, battleList):
        self.drawPlayer(player, screen)
        self.drawMonster(monster, screen)
        
        if self.turn == "Player":
            self.displayGUI(screen, player)
            if self.battleSelection == "Attack":
                self.drawText("You attack with your " + player.currentWeapon + "!", screen)
                player.pause = True
                player.pauseTime = 1
                
                text = "You dealt " + str(self.findDamage(player) + player.strength) + " damage!"
                self.drawText(text, screen)
                player.pause = True
                player.pauseTime = 1
                
                self.playerAttack(player, monster)
                player.pause = True
                player.pauseTime = 1
                
                self.turn = "Monster"
            elif self.battleSelection == "Run Away":
                self.drawText("Got away safely!", screen)
                player.pause = True
                player.pauseTime = 1
                while len(battleList) >= 1:
                    battleList.remove(battleList[0])
            else:
                self.drawText("What will you do?", screen)

            self.battleSelection = ""
        else:
            text = "The " + monster.name + " attacked!"
            self.drawText(text, screen)
            player.pause = True
            player.pauseTime = 1
            self.monsterAttack(player, monster)
            
            text1 = "The " + monster.name + " dealt " + str(monster.strength) + " damage!"
            self.drawText(text1, screen)
            player.pause = True
            player.pauseTime = 1
            self.turn = "Player"
        
        self.checkDeaths(player, monster, battleList, screen)
        
class Bar(pygame.sprite.Sprite):
    def __init__(self, location, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("fight/healthBlock1.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.location = location
        self.changeColor(color, location)
    def changeColor(self, color, location):
        if color == "green":
            self.image = pygame.image.load("fight/healthBlock1.png")
        elif color == "yellow":
            self.image = pygame.image.load("fight/healthBlock2.png")
        elif color == "red":
            self.image = pygame.image.load("fight/healthBlock3.png")
            
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.location = location
        
        
        
        