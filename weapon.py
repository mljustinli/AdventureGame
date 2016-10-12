import sys, pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, power, name):
        pygame.sprite.Sprite.__init__(self)
        self.power = power
        self.name = name
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()

    def description(self):
        returnDescription = ["", ""]
        weaponNames = ["Fists", "Long Sword", "Salad", "Banana", "Mouth"]
        descriptions = ["Punch something!", \
                        "A long sword... (Bring me my long sword, ho!)", \
                        "The ultimate weapon against... big people...", \
                        "Banana... Bananaa! (Minions...)", \
                        "Just eat it!"]
        
        counter = -1
        for name in weaponNames:
            counter += 1
            if name == self.name:
                returnDescription[0] = "Power: " + str(self.power)
                returnDescription[1] = "Description: " + descriptions[counter]
                break
            else:
                returnDescription += "Power: NONE" \
                + "\n \n" + "A useless weapon."
                
        return returnDescription