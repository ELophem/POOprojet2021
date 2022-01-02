#Edouard d.S.d.L 18072

import os
import sys, random, pygame
from pygame.locals import *
from abc import ABC, abstractmethod
from timeit import Timer

#Initialize pygame and setting up the window
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

WIDTH = 1080 
HEIGHT = 720 
FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("EcosysPOO")


#Declaring the color variables used to differenciate different lifeforms
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
dark_green = (0, 50, 0)
brown = (100, 40, 0)
gender = ["male", "female"]

#Initializing the base class called lifeforms which all organisms in the ecosystem will descend
class lifeforms(pygame.sprite.Sprite, ABC):
    def __init__(self, width, height, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.hp = 10 
        self.dead = False 
        self.energy = 100
        self.isOrgWas  = False 
        self.image = pygame.Surface([width, height]).convert_alpha()
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def isDead(self):
        if self.hp >= 0:
           return True
        else:
            return False

    def get_posX(self):
        return self.rect.x
    
    def get_posY(self):
        return self.rect.y

    def set_posX(self, value):
        self.rect.x = value

    def set_posY(self, value):
        self.rect.y = value

    def set_color(self, value):
        self.color = value
    
    def set_meat(self):
        self.image.fill(red)
        self.color = red

    def set_waste(self):
        self.image.fill(brown)
        self.color = brown

    def set_black(self):
        self.image.fill(black)
        self.color = black

    def get_color(self):
        return self.color 

    def set_hp(self, value): 
        i = value
        self.hp += i    
    
    def get_hp(self):
        return self.hp

    def set_energy(self, value):
        i = value
        self.energy += i
    
    def get_energy(self):
        return self.energy


    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_X(self, value):
        self.rect.x = value


#Initializing the classes of the two main lifeforms animals and plants
class Animals(lifeforms):
    def __init__(self, width, height, pos_x, pos_y):
        lifeforms.__init__(self, width, height, pos_x, pos_y)
        self.isGender = random.choice(gender)
        self.isFood = False
        self.speed = random.randrange(1, 5)
        self.move = [None, None]
        self.direction = None
        self.preg = False
        
    def set_direction(self):
        self.direction *= -1

    def get_direction(self):
        return self.direction

    def get_gender(self):
        return self.isGender
    
    def pregnant(self):
        self.preg = True

    def not_pregnant(self):
        self.preg = False
        
    def get_pregnant(self):
        return self.preg

    def get_isFood(self):
        return self.isFood

    def set_isFood(self, value):
        self.isFood = value

#here we are defining the classes of the two types of animals there are going to be predators and herbivores
class Predator(Animals):
    def __init__(self, width, height, pos_x, pos_y):
        lifeforms.__init__(self, width, height, pos_x, pos_y)
        Animals.__init__(self, width, height, pos_x, pos_y)
        pygame.sprite.Sprite.__init__(self)
        
        self.color = white
        self.image.fill(self.color)
        self.zoneVisionP = pygame.Rect(self.rect.x-10, self.rect.y-10, width+20, height+20)
    #-----------------------------Getters/setters
    def set_x(self, value):
        self.zoneVisionP.x = value

    def set_y(self, value):
        self.zoneVisionP.y = value

    def get_x(self):
        return self.zoneVisionP.x

    def get_y(self):
        return self.zoneVisionP.y
 #here is an update on the state of the animal and to add a random movement in any direction
    def update(self):
        if self.hp > 0:
            self.energy -= 0.05  
            if self.energy <= 0 :
                self.energy = 0
                if self.hp > 0:
                    self.hp -= 0.5 

            directions = {"S":((-1,2),(1,self.speed)),"SW":((-self.speed,-1),(1,self.speed)),"W":((-self.speed,-1),(-1,2)),"NW":((-self.speed,-1),(-self.speed,-1)),"N":((-1,2),(-self.speed,-1)),"NE":((1,self.speed),(-self.speed,-1)),"E":((1,self.speed),(-1,2)),"SE":((1,self.speed),(1,self.speed))} #((min x, max x)(min y, max y))
            directionsName = ("S","SW","W","NW","N","NE","E","SE") #possible directions
            if random.randrange(0,5) == 2: #move about once every 5 frames
                if self.direction == None: #if no direction is set, set a random one
                    self.direction = random.choice(directionsName)
                else:
                    a = directionsName.index(self.direction) #get the index of direction in directions list
                    b = random.randrange(a-1,a+2) #set the direction to be the same, or one next to the current direction
                    if b > len(directionsName)-1: #if direction index is outside the list, move back to the start
                        b = 0
                        self.direction = directionsName[b]
                    self.move[0] = random.randint(directions[self.direction][0][0],directions[self.direction][0][1])  #change relative x to a random number between min x and max x
                    self.move[1] = random.randint(directions[self.direction][1][0],directions[self.direction][1][1])  #change relative x to a random number between min x and max x
            if self.rect.x < 5 or self.rect.x > WIDTH - 5 or self.rect.y < 5 or self.rect.y > HEIGHT - 5: #if cell is near the border of the screen, change direction
                if self.rect.x < 5:
                    self.direction = "E"
                elif self.rect.x > WIDTH - 5:
                    self.direction = "W"
                elif self.rect.y < 5:
                    self.direction = "S"
                elif self.rect.y > HEIGHT - 5:
                    self.direction = "N"
                self.move[0] = random.randint(directions[self.direction][0][0],directions[self.direction][0][1])  #change relative x to a random number between min x and max x
                self.move[1] = random.randint(directions[self.direction][1][0],directions[self.direction][1][1])  #change relative x to a random number between min x and max x
            if self.move[0] != None: #add the relative coordinates to the cells coordinates
                self.rect.x += self.move[0]
                self.zoneVisionP.x += self.move[0]
                self.rect.y += self.move[1]
                self.zoneVisionP.y += self.move[1] 

        elif self.hp <= 0 and self.isFood == False:
            self.hp = 0
            self.image.fill(red)
            self.color = red 
            
class Herbivore(Animals):
    def __init__(self, width, height, pos_x, pos_y):
        Animals.__init__(self, width, height, pos_x, pos_y)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height]).convert_alpha()       
        self.color = dark_green
        self.image.fill(self.color)
        self.zoneVisionH = pygame.Rect(self.rect.x-10, self.rect.y-10, self.width+20, self.height+20)
        
    #-------------------------------Getters/setters---------------------    
    def set_x(self, value):
        self.zoneVisionH.x = value

    def set_y(self, value):
        self.zoneVisionH.y = value

    def get_x(self):
        return self.zoneVisionH.x

    def get_y(self):
        return self.zoneVisionH.y
 #here is an update on the state of the animal and to add a random movement in any direction
    def update(self):
        if self.hp > 0:   
            self.energy -= 0.05  
            if self.energy <= 0 :
                self.energy = 0
                if self.hp > 0:
                    self.hp -= 0.5 
            directions = {"S":((-1,2),(1,self.speed)),"SW":((-self.speed,-1),(1,self.speed)),"W":((-self.speed,-1),(-1,2)),"NW":((-self.speed,-1),(-self.speed,-1)),"N":((-1,2),(-self.speed,-1)),"NE":((1,self.speed),(-self.speed,-1)),"E":((1,self.speed),(-1,2)),"SE":((1,self.speed),(1,self.speed))} #((min x, max x)(min y, max y))
            directionsName = ("S","SW","W","NW","N","NE","E","SE") #possible directions
            if random.randrange(0,5) == 2: #move about once every 5 frames
                if self.direction == None: #if no direction is set, set a random one
                    self.direction = random.choice(directionsName)
                else:
                    a = directionsName.index(self.direction) #get the index of direction in directions list
                    b = random.randrange(a-1,a+2) #set the direction to be the same, or one next to the current direction
                    if b > len(directionsName)-1: #if direction index is outside the list, move back to the start
                        b = 0
                    self.direction = directionsName[b]
                self.move[0] = random.randint(directions[self.direction][0][0],directions[self.direction][0][1])  #change relative x to a random number between min x and max x
                self.move[1] = random.randint(directions[self.direction][1][0],directions[self.direction][1][1])  #change relative x to a random number between min x and max x
            if self.rect.x < 5 or self.rect.x > WIDTH - 5 or self.rect.y < 5 or self.rect.y > HEIGHT - 5: #if cell is near the border of the screen, change direction
                if self.rect.x < 5:
                    self.direction = "E"
                elif self.rect.x > WIDTH - 5:
                    self.direction = "W"
                elif self.rect.y < 5:
                    self.direction = "S"
                elif self.rect.y > HEIGHT - 5:
                    self.direction = "N"
                self.move[0] = random.randint(directions[self.direction][0][0],directions[self.direction][0][1])  #change relative x to a random number between min x and max x
                self.move[1] = random.randint(directions[self.direction][1][0],directions[self.direction][1][1])  #change relative x to a random number between min x and max x
            if self.move[0] != None: #add the relative coordinates to the cells coordinates
                self.rect.x += self.move[0]
                self.zoneVisionH.x += self.move[0]
                self.rect.y += self.move[1]
                self.zoneVisionH.y += self.move[1]
        elif self.hp <= 0 and self.isFood == False:
            self.hp = 0
            self.image.fill(red)
            self.color = red

           
#defining a new lifeform here the plants which can not move in our game 
class Plants(lifeforms):
    def __init__(self, width, height, pos_x, pos_y):
        lifeforms.__init__(self, width, height, pos_x, pos_y)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height]).convert_alpha()

        self.color = green
        self.image.fill(self.color)
        self.zoneVisionPlant = pygame.Rect(self.rect.x-50, self.rect.y-50, self.width+100, self.height+100)

    def update(self):
        if self.isDead() == False and self.energy > 0 :
            self.energy -= 0.05  
        elif self.energy <= 0 :
            self.energy = 0
            if self.hp > 0:
                self.hp -= 0.05
        elif self.hp <= 0 :
            self.hp = 0
            self.image.fill(brown)
            self.color = brown

pred_group = pygame.sprite.Group()
herb_group = pygame.sprite.Group()
plant_group = pygame.sprite.Group()
child_group = pygame.sprite.Group()

#Declaring the number of initial objects
number_of_Predators = range(10)
number_of_Herbivores = range(25)
number_of_Plants = range(50)

objPr = list()
for i in number_of_Predators:
    objPr.append(Predator(20, 20, random.randrange(10, WIDTH-10), random.randrange(10, HEIGHT-10)))
    pred_group.add(objPr[i])

objH = list()
for i in number_of_Herbivores:
    objH.append(Herbivore(20, 20, random.randrange(10, WIDTH-10), random.randrange(10, HEIGHT-10)))
    herb_group.add(objH[i])

objP = list()
for i in number_of_Plants:
    objP.append(Plants(20, 20, random.randrange(10, WIDTH-10), random.randrange(10, HEIGHT-10)))
    plant_group.add(objP[i])



def hunt():
    global number_of_Herbivores_alive
    for i in range(0,len(objPr)):
         for j in range(0,len(objH)):
             if objH[j].get_hp() > 0:
                collide = pygame.Rect.colliderect(objPr[i].rect, objH[j].rect)
                if collide and objH[j].get_color != brown :
                    objH[j].set_hp(-5)
                    if objH[j].isDead() == True:
                        if objPr[i].get_energy() <= 5:
                            objPr[i].set_energy(5)

                        elif objPr[i].get_energy() == 6:
                            objPr[i].set_energy(4)
                            if objPr[i].get_hp() <= 9:
                                objPr[i].set_hp(1)

                        elif objPr[i].get_energy() == 7:
                            objPr[i].set_energy(3)
                            if objPr[i].get_hp() <= 8:
                                objPr[i].set_hp(2)
                            elif objPr[i].get_hp() == 9:
                                objPr[i].set_hp(1)
                            else:
                                objPr[i].set_hp(0)

                        elif objPr[i].get_energy() == 8:
                            objPr[i].set_energy(2)
                            if objPr[i].get_hp() <= 7:
                                objPr[i].set_hp(3)
                            elif objPr[i].get_hp() == 8:
                                objPr[i].set_hp(2)
                            elif objH[i].get_hp() == 9:
                                objPr[i].set_hp(1)
                            else:
                                objPr[i].set_hp(0)

                        elif objPr[i].get_energy() == 9:
                            objPr[i].set_energy(1)
                            if objPr[i].get_hp() <= 6:
                                objPr[i].set_hp(4)
                            elif objPr[i].get_hp() == 7:
                                objPr[i].set_hp(3)
                            elif objPr[i].get_hp() == 8:
                                objPr[i].set_hp(2)
                            elif objPr[i].get_hp() == 9:
                                objPr[i].set_hp(1)
                            else:
                                objPr[i].set_hp(0)

                        elif objPr[i].get_energy() == 10:
                            objPr[i].set_energy(0)
                            if objPr[i].get_hp() <= 5:
                                objPr[i].set_hp(5)
                            elif objPr[i].get_hp() == 6:
                                objPr[i].set_hp(4)
                            elif objPr[i].get_hp() == 7:
                                objPr[i].set_hp(3)
                            elif objPr[i].get_hp() == 8:
                                objPr[i].set_hp(2)
                            elif objPr[i].get_hp() == 9:
                                objPr[i].set_hp(1)
                            else:
                                objPr[i].set_hp(0)

def eatplant():
    global number_of_Plants_alive
    for i in range(0,len(objH)):
         for j in range(0,len(objP)):
             if objP[j].get_hp() > 0:
                collide = pygame.Rect.colliderect(objH[i].rect, objP[j].rect)
                if collide:
                    objP[j].set_hp(-10)
                    if objP[j].isDead() == True:
                        objP[j].set_X(WIDTH+50)
                    if objH[i].get_energy() <= 5:
                        objH[i].set_energy(5)
                        number_of_Plants_alive -= 1

                    elif objH[i].get_energy() == 6:
                        objH[i].set_energy(4)
                        if objH[i].get_hp() <= 9:
                            objH[i].set_hp(1)
                            number_of_Plants_alive -= 1

                    elif objH[i].get_energy() == 7:
                        objH[i].set_energy(3)
                        if objH[i].get_hp() <= 8:
                            objH[i].set_hp(2)
                        elif objH[i].get_hp() == 9:
                            objH[i].set_hp(1)
                        else:
                             objH[i].set_hp(0)
                             number_of_Plants_alive -= 1

                    elif objH[i].get_energy() == 8:
                        objH[i].set_energy(2)
                        if objH[i].get_hp() <= 7:
                            objH[i].set_hp(3)
                        elif objH[i].get_hp() == 8:
                            objH[i].set_hp(2)
                        elif objH[i].get_hp() == 9:
                            objH[i].set_hp(1)
                        else:
                             objH[i].set_hp(0)
                             number_of_Plants_alive -= 1

                    elif objH[i].get_energy() == 9:
                        objH[i].set_energy(1)
                        if objH[i].get_hp() <= 6:
                            objH[i].set_hp(4)
                        elif objH[i].get_hp() == 7:
                            objH[i].set_hp(3)
                        elif objH[i].get_hp() == 8:
                            objH[i].set_hp(2)
                        elif objH[i].get_hp() == 9:
                            objH[i].set_hp(1)
                        else:
                             objH[i].set_hp(0)
                             number_of_Plants_alive -= 1

                    elif objH[i].get_energy() == 10:
                        objH[i].set_energy(0)
                        if objH[i].get_hp() <= 5:
                            objH[i].set_hp(5)
                        elif objH[i].get_hp() == 6:
                            objH[i].set_hp(4)
                        elif objH[i].get_hp() == 7:
                            objH[i].set_hp(3)
                        elif objH[i].get_hp() == 8:
                            objH[i].set_hp(2)
                        elif objH[i].get_hp() == 9:
                            objH[i].set_hp(1)
                        else:
                             objH[i].set_hp(0)
                             number_of_Plants_alive -= 1

def absorbHerb():
    global number_of_Herbivores_alive
    for i in range(0,len(objH)):
        for j in range(0,len(objP)):
            if objH[i].get_color() == brown:
                collide = pygame.Rect.colliderect(objH[i].rect, objP[j].zoneVisionPlant)
                if collide: 
                    objH[i].set_X(WIDTH+50)
                    number_of_Herbivores_alive -= 1

def absorbPred():
    global number_of_Predators_alive
    for i in range(0,len(objPr)):
        for j in range(0,len(objP)):
            if objPr[i].get_color() == brown:
                collide = pygame.Rect.colliderect(objPr[i].rect, objP[j].zoneVisionPlant)
                if collide: 
                    objPr[i].set_X(WIDTH+50)
                    number_of_Predators_alive -= 1



def create_herb():
    global number_of_Herbivores_alive
    objH.append(Herbivore(20, 20, random.randrange(10, WIDTH-10), random.randrange(10, HEIGHT-10)))
    herb_group.add(objH)
    number_of_Herbivores_alive += 1
    
def create_pred():
    global number_of_Predators_alive
    objPr.append(Predator(20, 20, random.randrange(10, WIDTH-10), random.randrange(10, HEIGHT-10)))
    pred_group.add(objPr)
    number_of_Predators_alive += 1

def create_plant():
    global number_of_Plants_alive
    objP.append(Plants(20, 20, random.randrange(10, WIDTH-10), random.randrange(10, HEIGHT-10)))
    plant_group.add(objP)
    number_of_Plants_alive += 1


    
#Reproduction of a male and femal predator also reproduction of plants 
def reproduction_Herbivores():
    for i in range(0,len(objH)):
        for j in range(0,len(objH)):
            collide = pygame.Rect.colliderect(objH[i].zoneVisionH, objH[j].zoneVisionH)
            if objH[j].get_energy() >= 8 and objH[i].get_energy() >= 8:
                if collide and objH[j].get_gender() == "male" and objH[i].get_gender() == "female" and objH[j].isDead() == False and objH[i].isDead() == False and objH[i].get_pregnant() == False:
                    objH[i].pregnant()
                if random.randrange(0,20) == 2 and objH[i].get_pregnant() == True and number_of_Herbivores_alive < 20:
                    create_herb()
                    objH[i].not_pregnant()

def reproduction_Predators():
    for i in range(0,len(objPr)):
        for j in range(0,len(objPr)):
            collide = pygame.Rect.colliderect(objPr[i].zoneVisionP, objPr[j].zoneVisionP)
            if objPr[j].get_energy() >= 8 and objPr[i].get_energy() >= 8:
                if collide and objPr[j].get_gender() == "male" and objPr[i].get_gender() == "female" and objPr[j].isDead() == False and objPr[i].isDead() == False and objPr[i].get_pregnant() == False:
                    objPr[i].pregnant()
                if random.randrange(0,20) == 2 and objPr[i].get_pregnant() == True and number_of_Predators_alive < 20:
                    create_pred()
                    objPr[i].not_pregnant()

def reproduction_Plants():
    if random.randrange(0,20) == 2:
        for i in range(0,len(objP)):
            if objP[i].get_energy() >= 5 and objP[i].get_hp() != 0 and random.randrange(0,20) == 2:
                    create_plant()
            else:
                return None


def malesHerb():
    for i in number_of_Herbivores:
        for j in number_of_Herbivores:
            if objH[j].get_gender() == "male":
                male = pygame.Rect(objH[j].get_xC()-10, objH[j].get_yC()-10, objH[j].get_width()+20, objH[j].get_height()+20)
                pygame.draw.rect(screen, (0, 255, 0), male)
            if objH[i].get_gender() == "male":               
                male = pygame.Rect(objH[i].get_xC()-10, objH[i].get_yC()-10, objH[i].get_width()+20, objH[i].get_height()+20)
                pygame.draw.rect(screen, (0, 255, 255), male)

def malesPred():
    for i in number_of_Predators:
        for j in number_of_Predators:
            if objPr[j].get_gender() == "male":
                male = pygame.Rect(objPr[j].get_xC()-10, objPr[j].get_yC()-10, objPr[j].get_width()+20, objPr[j].get_height()+20)
                pygame.draw.rect(screen, (0, 255, 0), male)
            if objPr[i].get_gender() == "male":               
                male = pygame.Rect(objPr[i].get_xC()-10, objPr[i].get_yC()-10, objPr[i].get_width()+20, objPr[i].get_height()+20)
                pygame.draw.rect(screen, (0, 255, 255), male) 

def zoneVisionPlant():
    for i in number_of_Plants: 
        pygame.draw.rect(screen, (255, 255, 0), objP[i].zoneVisionPlant )

def become_orgw():
    for j in range(0,len(objH)):
        for i in range(0,len(objPr)):
            if objH[j].get_color() == red and random.randrange(0,100) == 2:
                objH[j].set_isFood(True)
                objH[j].set_waste()

def become_orgw2():
    for i in range(0,len(objPr)):
        if objPr[i].get_color() == red and random.randrange(0,100) == 2:
            objPr[i].set_isFood(True)
            objPr[i].set_waste()

def become_orgw3():
    for i in range(0,len(objP)):
        if objP[i].get_hp() == 0 and random.randrange(0,100) == 2:
            objP[i].set_X(WIDTH+50)

number_of_Herbivores_alive = 0
initial_Herbivores = len(objH)

number_of_Predators_alive = 0
initial_Predators = len(objPr)

number_of_Plants_alive = 0
initial_Plants = len(objP)


#Initializing the mainloop for our pygame
def mainloop():
    while True:
        pygame.time.Clock().tick(FPS) 
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit() 
                sys.exit() 
        
        screen.fill(0)
        
        hunt()
        eatplant()    
        absorbHerb()
        absorbPred()
        reproduction_Predators()
        reproduction_Herbivores()
        reproduction_Plants()
        pred_group.update()
        herb_group.update()
        plant_group.update()
        become_orgw()
        become_orgw2()
        become_orgw3()
        pred_group.draw(screen)
        herb_group.draw(screen)
        plant_group.draw(screen)
        pygame.display.flip()


mainloop()
