import sys, pygame

class Cell(pygame.sprite.Sprite):
    def __init__(self, status, size, town):
        pygame.sprite.Sprite.__init__(self)
        imageName = self.translateChar(status, town) + ".png"
        self.image = pygame.image.load(imageName)
        self.rect = self.image.get_rect()
        self.size = size
        self.status = status
    def changeColor(self, color):
        if color == "next":
            image_surface = pygame.surface.Surface(self.size)
            image_surface.fill([255, 255, 0])
            self.image = image_surface.convert()
        else:
            image_surface = pygame.surface.Surface(self.size)
            image_surface.fill([0, 255, 255])
            self.image = image_surface.convert()
    def change(self, defGround):
        stati = ['O', 'w']
        translate = ["environment/grassDark", "buildings/woodFloor"]
        
        imageName = ""
        counter = -1
        
        for char in stati:
            counter += 1
            if defGround == char:
                imageName = translate[counter]
                break
            else:
                imageName = "environment/grassDark"
        return imageName
    def translateChar(self, status, town):
        stati = ['^', 'o', 'O', 'r', 'P', 'b', '*' \
                 , 'q', 'w', 't', 's']
        translate = ["environment/startTree", "environment/grassLight" \
                     , "environment/grassDark", "environment/startRock" \
                     , "buildings/playerHouse", self.change(town.defGround) \
                     , "environment/darkness", "furniture/cushionyChair" \
                     , "buildings/woodFloor", "furniture/singleTable" \
                     , "furniture/bookshelf"]
        
        imageName = ""
        counter = -1
        
        for char in stati:
            counter += 1
            if status == char:
                imageName = translate[counter]
                break
            else:
                imageName = "environment/startTree"
        return imageName