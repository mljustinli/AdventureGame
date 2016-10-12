import sys, pygame
from cell import Cell
from player import Player

class Town():
    def __init__(self, fileName, name, cellsize, size):
        self.matrix = [];
        self.matrixDepth = -1
        self.cellsize = cellsize
        self.size = size
        self.name = name
        self.getDefault()
        self.openMap(fileName)
        self.createCells(self.matrix)
        self.TPlocation = self.getTPlocation()
    def openMap(self, fileName):
        try:
            data = open(fileName, "r")
            
            holderString = data.readline()
            while holderString:
                holderString = holderString.strip()
                self.matrix.append([])
                self.matrixDepth += 1
                for char in holderString:
                    self.matrix[self.matrixDepth].append(char)
                holderString = data.readline();
            self.matrixDepth += 1 #you started at 0 so to compensate
            
            data.close()
        except:
            print "You done messed up fool"
    def printMatrix(self):
        for i in range(self.matrixDepth):
            for j in range(len(self.matrix[0])):
                print self.matrix[i][j],
            print "\n"
        print self.matrix
    def createCells(self, matrix):        
        self.cellmatrix = []
        for i in range(len(matrix)):
            self.cellmatrix.append([])
            for j in range(len(matrix[0])):
                status = matrix[i][j]
                
#                 location = [i * self.cellsize[0], j * self.cellsize[1]]
                newCell = Cell(status, self.cellsize, self)
                self.cellmatrix[i].append(newCell)
    def showArea(self, location, screen, player):        
        screenMatrix = self.findScreen(location, player)
        
        clear = ['s', 't', 'q']
        
        #not too sure what size is...
        #for printing the defGround
        newCell = Cell(self.defGround, [50, 30], self)
        
        
        for i in range(len(screenMatrix)):
            #not exactly sure what to do here...
            #only if it's a tree or tall object does it
            #draw behind the player!!!!
            
            for j in range(len(screenMatrix[i])):
                if screenMatrix[i][j].status == "P":
                    screenMatrix[i][j].rect.right, screenMatrix[i][j].rect.bottom = [(j + 1) * 50, (i + 1) * 30]
                elif screenMatrix[i][j].status == "s":
                    screenMatrix[i][j].rect.right, screenMatrix[i][j].rect.bottom = [(j + 1) * 50, (i + 1) * 30]
                else:
                    screenMatrix[i][j].rect.centerx, screenMatrix[i][j].rect.bottom = [j * 50 + 25, (i + 1) * 30]
                
                newCell.rect.centerx, newCell.rect.bottom = [j * 50 + 25, (i + 1) * 30]
                
                for thing in clear:
                    if screenMatrix[i][j].status == thing:
                        screen.blit(newCell.image, newCell.rect)
                screen.blit(screenMatrix[i][j].image, screenMatrix[i][j].rect)
                if i == 10:
                    screen.blit(player.image, [player.rect.left, player.rect.centery - 50])

    def findScreen(self, location, player):
        #assumes you're not at the edge/player controls that
        #or something... hopefully
        self.screenMatrix = []
        columns = self.size[0] / self.cellsize[0]
        rows = self.size[1] / self.cellsize[1]
        
#         print location
#         print columns
#         print rows
#         print len(self.cellmatrix) - 11
#         print len(self.cellmatrix[0]) - 11
        
        for i in range(rows):
            self.screenMatrix.append([])
            for j in range(columns):
#                 if (location[0] >= 9 and location[0] <= len(self.cellmatrix) - 11 and location[1] >= 9 and location[1] <= len(self.cellmatrix[0]) - 11):
                if (location[0] - columns/2 + i >= 0 \
                    and location[0] - columns/2 + i <= len(self.cellmatrix) - 1 \
                    and location[1] - rows/2 + j >= 0 \
                    and location[1] - rows/2 + j <= len(self.cellmatrix[0]) - 1):
                    self.screenMatrix[i].append(self.cellmatrix[location[0] - columns/2 + i][location[1] - rows/2 + j])
                else:
#                     defaultStatus = '^'
#                     houses = ["Player House"]
#                     
#                     for name in houses:
#                         if self.name == name:
#                             defaultStatus = '*'
                    defaultStatus = self.defFar
                                                
                    newCell = Cell(defaultStatus, self.cellsize, self)
                    self.screenMatrix[i].append(newCell)
        return self.screenMatrix
    def checkBounds(self, player, direction):
        returnBool = True
        check = ['^', 'r', 'P', 'b', 't', 's', '*']
        if direction == "up":
            for item in check:
                if self.screenMatrix[9][10].status == item:
                    returnBool = False
        elif direction == "down":
            for item in check:
                if self.screenMatrix[11][10].status == item:
                    returnBool = False
        elif direction == "left":
            for item in check:
                if self.screenMatrix[10][9].status == item:
                    returnBool = False
        elif direction == "right":
            for item in check:
                if self.screenMatrix[10][11].status == item:
                    returnBool = False
        return returnBool
    def getTPlocation(self):
        if self.name == "Peach Town":
            return [14, 1]
        elif self.name == "Rosenberg City":
            return [1, 10]
        else:
            return [0, 0]
    def getDefault(self):
        towns = ["Peach Town", "Pass 1", "Rosenberg City" \
                 , "Player House"]
        defGround = ["O", "O" , "O", "w"]
        defFar = ['^', '^', '^', '*']
        
        counter = -1
        for townName in towns:
            counter += 1
            if self.name == townName:
                self.defGround = defGround[counter]
                self.defFar = defFar[counter]
                break
                
                