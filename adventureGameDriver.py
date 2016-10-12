import sys, pygame
from town import Town
from cell import Cell
from player import Player
from battleDriver import Battle
from inventoryRender import Inventory
from monster import Monster
from time import sleep

pygame.init()

def checkBounds(player, direction):
    for place in places:
        if player.town == place.name:
            if place.checkBounds(player, direction):
                return True
            else:
                return False
def displayArea(player):
    for place in places:
        if player.town == place.name:
            place.showArea(player.screenLocation, screen, player)
def checkTP(player):
    if player.town == "Peach Town":
        if player.screenLocation == [14, 0] or player.screenLocation == [15, 0]:
            player.town = "Pass 1"
            player.screenLocation = [10, 64]
        elif player.screenLocation == [7, 44]:
            player.town = "Player House"
            player.screenLocation = [8, 7]
    elif player.town == "Pass 1":
        if player.screenLocation == [10, 65] or player.screenLocation == [9, 65]:
            player.town = "Peach Town"
            player.screenLocation = peachTown.TPlocation
        elif player.screenLocation == [29, 24] or player.screenLocation == [29, 25]:
            player.town = "Rosenberg City"
            player.screenLocation = rosenbergCity.TPlocation
    elif player.town == "Rosenberg City":
        if player.screenLocation == [0, 11] or player.screenLocation == [0, 10]:
            player.town = "Pass 1"
            player.screenLocation = [28, 25]
    elif player.town == "Player House":
        if player.screenLocation == [9, 7]:
            player.town = "Peach Town"
            player.screenLocation = [8, 44]
def displayAreaName(player):    
    text = player.town
    
    townName = ["Player House"]
    colors = [(140, 25, 156)]
    
    counter = -1
    
    for name in townName:
        counter += 1
        if name == player.town:
            t = locFont.render(text, 1, colors[counter])
            break
        else:
            t = locFont.render(text, 1, (0, 0, 0))
    screen.blit(t, [15, 8])
    
    
size = width, height = 1050, 630
cellsize = cwidth, cheight = 50, 30
screen = pygame.display.set_mode(size)
pygame.display.set_caption("I'M PROGRAMMING POKEMON!!!")
#lighter green color is: [43, 186, 43]
screen.fill([27, 125, 49])
clock = pygame.time.Clock()

# playerScreenLocation = [8, 39]

peachTown = Town("peachTown.txt", "Peach Town", cellsize, size)
pass1 = Town("pass1.txt", "Pass 1", cellsize, size)
rosenbergCity = Town("rosenbergCity.txt", "Rosenberg City", cellsize, size)
playerHouse = Town("playerHouse.txt", "Player House", cellsize, size)

#remember to update this when you add a new place!!!!
places = [peachTown, pass1, rosenbergCity, playerHouse]

player = Player("player/playerBack1.png", [525, 315], "Peach Town", [8, 39])
locFont = pygame.font.Font(None, 50)
inInventory = False
playerInventory = Inventory("inventory/inventoryGUI3.png")

testMonster = Monster("monster/glop.png", "Glop", 40, 2000)
test = Battle()
battleList = [test]

delay = 100
interval = 100
pygame.key.set_repeat(delay, interval)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        if len(battleList) == 0 and not inInventory:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if checkBounds(player, "up"):
                        player.screenLocation[0] -= 1
                    player.direction = "up"
                    player.changePic = True
                elif event.key == pygame.K_s:
                    if checkBounds(player, "down"):
                        player.screenLocation[0] += 1
                    player.direction = "down"
                    player.changePic = True
                elif event.key == pygame.K_a:
                    if checkBounds(player, "left"):
                        player.screenLocation[1] -= 1
                    player.direction = "left"
                    player.changePic = True
                elif event.key == pygame.K_d:
                    if checkBounds(player, "right"):
                        player.screenLocation[1] += 1
                    player.direction = "right"
                    player.changePic = True
                elif event.key == pygame.K_j:
                    interval = 25
                    pygame.key.set_repeat(delay, interval)
                elif event.key == pygame.K_k:
                    interval = 100
                    pygame.key.set_repeat(delay, interval)
                elif event.key == pygame.K_e:
                    inInventory = not inInventory
        elif len(battleList) == 0 and inInventory:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    inInventory = not inInventory
                elif event.key == pygame.K_w:
                    playerInventory.scrollUp()
                elif event.key == pygame.K_s:
                    playerInventory.scrollDown()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                playerInventory.checkSelection(event.pos, player)
#         elif not battleList[0].battleDone():
        elif len(battleList) == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.hp += 10
                elif event.key == pygame.K_DOWN:
                    player.hp -= 10
                elif event.key == pygame.K_w:
                    testMonster.hp += 200
                elif event.key == pygame.K_s:
                    testMonster.hp -= 200
            elif event.type == pygame.MOUSEBUTTONDOWN:
                battleList[0].checkClick(event.pos)
    if player.dead:
        screen.fill([23, 255, 82])
        text = "You died! Press q to quit."
        font = pygame.font.Font(None, 75)
        t = font.render(text, 1, (255, 255, 255))
        screen.blit(t, [30, 550])
    elif len(battleList) == 0:
        if not inInventory:
            #y and then x
            screen.fill([27, 125, 49])
            if player.changePic:
                player.changeState()
            checkTP(player)
            displayArea(player)
            displayAreaName(player)
            print player.screenLocation
        else:
            screen.fill([149, 110, 6])
            playerInventory.displayInventory(player, screen)
    elif len(battleList) == 1:
        screen.fill([0, 0, 0])
        #give the battle object the parameters in
        #init
        battleList[0].doBattle(player, testMonster, pass1, screen, battleList)
    
    #     screen.blit(player.image, [player.rect.left, player.rect.centery - 50])
    
    pygame.display.flip()
    
    if player.pause:
        sleep(player.pauseTime)
        player.pause = False
        player.pauseTime = 0
        
    clock.tick(20)