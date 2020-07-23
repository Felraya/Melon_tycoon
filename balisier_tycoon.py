import pygame
import time
import math
import numpy
from random import *
 
 
class GameConfig :     #DECLARATION DE TOUTES LES CONSTANTES ET IMPORTATIONS DES IMAGES ET SONS

    #largeur du personnage : 80
    #coté Plant : 50
    #largeur melonnière : 100
    #espace entre melonière : 50
 

    windowW=1000
    windowH=800
 
    persoW = 80
    persoH = 70

    baquetW = 200
    baquetH = 130

    touchesW = 80
    touchesH = 150
 
    plant_size = 50

    marge = 25

    end = 1000

    #coordonnées X des rangs en leur milieu 
    rang1X = 100
    rang2X = 250
    rang3X = 400
    rang4X = 550
    rang5X = 700

    personnageY = 700
 
 
    bache_couleur = (61,89,100)
    terre_couleur = (91,70,49)

    red = (250,20,20)
    green = (20,210,20)
    blue = (30,160,160)
    white = (255,255,255)

    bache = pygame.image.load('image/bache.png')
 
    melon_mur_image = pygame.image.load('image/mur.png')
    melon_mur_image = pygame.transform.scale(melon_mur_image,(plant_size,plant_size))

    melon_pas_mur_image = pygame.image.load('image/pasmur.png')
    melon_pas_mur_image = pygame.transform.scale(melon_pas_mur_image,(plant_size,plant_size))

    melon_pourri_image = pygame.image.load('image/pourri.png')
    melon_pourri_image = pygame.transform.scale(melon_pourri_image,(plant_size,plant_size))

    mauvaise_herbe_image = pygame.image.load('image/herbe.png')
    mauvaise_herbe_image = pygame.transform.scale(mauvaise_herbe_image,(plant_size,plant_size))
 
    perso_image = pygame.image.load('image/perso.png')
    perso_image = pygame.transform.scale(perso_image,(persoW, persoH))

    baquet_image = pygame.image.load('image/baquet.png')
    baquet_image = pygame.transform.scale(baquet_image,(baquetW, baquetH))

    touches_image = pygame.image.load('image/touches.png')
    touches_image = pygame.transform.scale(touches_image,(touchesW, touchesH))

    simon_image = pygame.image.load('image/simon.png')
 
 
    pygame.mixer.init(frequency=8000, size=16, channels=1)

    sonTheme = pygame.mixer.Sound("sound/wiiSportResort.wav")
 
 
class Plant : #mauvaise herbe ou melon
    def __init__(self, type, rang) :
 
        self.position = rang

        if type == 1 or type == 2 or type == 3 or type == 4: #melon mur plantType 1
            self.plantType = 1
            self.plantImage = GameConfig.melon_mur_image
            
            if rang == 1 :
                self.plantX = GameConfig.rang1X
            elif rang == 2 :
                self.plantX = GameConfig.rang2X
            elif rang == 3 :
                self.plantX = GameConfig.rang3X
            elif rang == 4 :
                self.plantX = GameConfig.rang4X
            elif rang == 5 :
                self.plantX = GameConfig.rang5X
            else :
                print("erreur de rang")

            self.plantX = self.plantX - GameConfig.plant_size / 2
            self.plantY = - 50

        elif type == 5 or type == 6 : #melon pas mur plantType 2
            self.plantType = 2
            self.plantImage = GameConfig.melon_pas_mur_image

            if rang == 1 :
                self.plantX = GameConfig.rang1X
            elif rang == 2 :
                self.plantX = GameConfig.rang2X
            elif rang == 3 :
                self.plantX = GameConfig.rang3X
            elif rang == 4 :
                self.plantX = GameConfig.rang4X
            elif rang == 5 :
                self.plantX = GameConfig.rang5X
            else :
                print("erreur de rang")

            self.plantX = self.plantX - GameConfig.plant_size / 2
            self.plantY = - 50
 
        elif type == 7 or type == 8 or type == 9 or type == 10 : #melon pourri plantType 3
            self.plantType = 3
            self.plantImage = GameConfig.melon_pourri_image
            if rang == 1 :
                self.plantX = GameConfig.rang1X
            elif rang == 2 :
                self.plantX = GameConfig.rang2X
            elif rang == 3 :
                self.plantX = GameConfig.rang3X
            elif rang == 4 :
                self.plantX = GameConfig.rang4X
            elif rang == 5 :
                self.plantX = GameConfig.rang5X
            else :
                print("erreur de rang")

            self.plantX = self.plantX - GameConfig.plant_size / 2
            self.plantY = - 50

        elif type == 11 or type == 12 : #mauvaise herbe plantType 4
            self.plantType = 4
            self.plantImage = GameConfig.mauvaise_herbe_image
            if rang == 1 :
                self.plantX = GameConfig.rang1X
            elif rang == 2 :
                self.plantX = GameConfig.rang2X
            elif rang == 3 :
                self.plantX = GameConfig.rang3X
            elif rang == 4 :
                self.plantX = GameConfig.rang4X
            elif rang == 5 :
                self.plantX = GameConfig.rang5X
            else :
                print("erreur de rang")

            self.plantX = self.plantX - GameConfig.plant_size / 2
            self.plantY = - 50

        else :
            print("type de plante inconnue")


    def getX(self) :
        return self.plantX
    def getY(self) :
        return self.plantY
    def getImg(self) :
        return self.plantImage
    def getType(self) :
        return self.plantType
    def getPosition(self) :
        return self.position

    def setX(self,X) :
        self.plantX=X
    def setY(self,Y) :
        self.plantY=Y


class Personnage : #personnage ceuilleur de melon
    def __init__(self) :
        self.position = 3
        self.personnageY = GameConfig.personnageY - GameConfig.persoH / 2

        if self.position == 1 :
            self.personnageX = GameConfig.rang1X - GameConfig.persoW / 2

        elif self.position == 2 :
            self.personnageX = GameConfig.rang2X - GameConfig.persoW / 2

        elif self.position == 3 :
            self.personnageX = GameConfig.rang3X - GameConfig.persoW / 2

        elif self.position == 4 :
            self.personnageX = GameConfig.rang4X - GameConfig.persoW / 2

        elif self.position == 5 :
            self.personnageX = GameConfig.rang5X - GameConfig.persoW / 2

    def persoLeft(self) :
        if self.position > 1 :
            self.position = self.position - 1

        if self.position == 1 :
            self.personnageX = GameConfig.rang1X - GameConfig.persoW / 2

        elif self.position == 2 :
            self.personnageX = GameConfig.rang2X - GameConfig.persoW / 2

        elif self.position == 3 :
            self.personnageX = GameConfig.rang3X - GameConfig.persoW / 2

        elif self.position == 4 :
            self.personnageX = GameConfig.rang4X - GameConfig.persoW / 2

        elif self.position == 5 :
            self.personnageX = GameConfig.rang5X - GameConfig.persoW / 2

    def persoRight(self) :
        if self.position < 5 :
            self.position = self.position + 1
            
        if self.position == 1 :
            self.personnageX = GameConfig.rang1X - GameConfig.persoW / 2

        elif self.position == 2 :
            self.personnageX = GameConfig.rang2X - GameConfig.persoW / 2

        elif self.position == 3 :
            self.personnageX = GameConfig.rang3X - GameConfig.persoW / 2

        elif self.position == 4 :
            self.personnageX = GameConfig.rang4X - GameConfig.persoW / 2

        elif self.position == 5 :
            self.personnageX = GameConfig.rang5X - GameConfig.persoW / 2

    def getPosition(self) :
        return self.position

    def getX(self) :
        return self.personnageX
    def getY(self) :
        return self.personnageY


class GameState : #Instance de jeu
    def __init__(self, window) :
 
        self.window = window
        self.ensemblePlant=[]
        self.personnage=Personnage()
        self.nbMelon = 0
 
        self.score = 0
        self.avancement = 0
 
        #vitesse de défilement
        self.speed = 1.2

        #vitesse de spawn (apparition d'une plant tout les x de score)
        self.intervalSpawn = 5

        self.newSpawn = 5

        self.baquet = 0
 

    def draw(self) : #affichage à chaque instance de jeu

        #background couleur terre
        self.window.fill(GameConfig.terre_couleur)
 
        #dessiner les rangs
        self.window.blit(GameConfig.bache,(GameConfig.rang1X-50,0))
        self.window.blit(GameConfig.bache,(GameConfig.rang2X-50,0))
        self.window.blit(GameConfig.bache,(GameConfig.rang3X-50,0))
        self.window.blit(GameConfig.bache,(GameConfig.rang4X-50,0))
        self.window.blit(GameConfig.bache,(GameConfig.rang5X-50,0))

        #score
        displayMessage(self.window, "Score : " + str(round(self.score)), 24, 860, 20, GameConfig.red)
        displayMessage(self.window, "Avancement : " + str(round((self.avancement / GameConfig.end) * 100)) + " %", 24, 860, 50, GameConfig.red)

        #touches
        self.window.blit(GameConfig.touches_image,(765,80))
        displayMessage(self.window, "Gauche / Droite", 22, 920, 95, GameConfig.white)
        displayMessage(self.window, "Ramasser melon", 22, 920, 135, GameConfig.white)
        displayMessage(self.window, "Retirer melon", 22, 920, 175, GameConfig.white)
        displayMessage(self.window, "Vider baquet", 22, 920, 215, GameConfig.white)

        #baquet
        if self.baquet == 10 :
            displayMessage(self.window, "Baquet plein !", 30, 850, 275, GameConfig.green)
            self.window.blit(GameConfig.baquet_image,(775,310))
        else :
            displayMessage(self.window, "Baquet : " + str(self.baquet) + " / 10", 30, 860, 275, GameConfig.green)

        #simon
        self.window.blit(GameConfig.simon_image,(750,480))
            
        #affichage des plantes
        for plant in self.ensemblePlant :
            self.window.blit(plant.getImg(),(plant.getX(),plant.getY()))

        #personnage
        self.window.blit(GameConfig.perso_image,(self.personnage.getX(),self.personnage.getY()))
 
 
    def advanceState(self,nextM) :
 
        #changement du score
        self.avancement = self.avancement + 0.1

        #mouvement des plants
        for plant in self.ensemblePlant :
            plant.setY(plant.getY() + self.speed)
 

        #création d'une nouvelle plant
        if self.avancement > self.newSpawn :
            self.newSpawn = self.newSpawn + self.intervalSpawn
            
            type = randint(1,12)
            rand1 = randint(1,5)
            rand2 = randint(1,5)

            if rand2 == rand1 :
                change = randint(1,2)
                if change == 1 and rand2 > 1 :
                    rand2 = rand2 - 1
                elif rand2 < 5 :
                    rand2 = rand2 + 1
                else :
                    rand2 = rand2 - 1
            newPlant = Plant(type, rand1)
            newPlant2 = Plant(5, rand2) #spawn d'un melon pas mur supplémentaire
            self.ensemblePlant.append(newPlant)
            self.ensemblePlant.append(newPlant2)

        #éxécution du prochain mouv
        if nextM == 1: #gauche
            self.personnage.persoLeft()

        elif nextM == 2: #droite
            self.personnage.persoRight()
            
        elif nextM == 3 : #ramasser melon
            self.ramasser()

        elif nextM == 4 : #retirer melon
            self.retirer()

        elif nextM == 5 : #vider baquet
            self.vider()

        self.badPlant()
            
  
    #permet d'être sur de retirer les plantes inutiles
    def clear(self) :
        for plant in self.ensemblePlant :
            if plant.getX() > 800 :
                self.ensemblePlant.remove(plant)

        for plant in self.ensemblePlant :
            if plant.getType() == 1 and plant.getX() > 800 :
                self.ensemblePlant.remove(plant)
                self.score = self.score - 20
            elif plant.getType() == 2 and plant.getX() > 800 :
                self.ensemblePlant.remove(plant)
            elif plant.getType() == 1 and plant.getX() > 800 :
                self.ensemblePlant.remove(plant)
                self.score = self.score - 10
            elif plant.getType() == 4 and plant.getX() > 800 :
                self.ensemblePlant.remove(plant)


    #ramasse un melon
    def ramasser(self) :
        for plant in self.ensemblePlant :
            if plant.getType() == 1 and plant.getY() + GameConfig.plant_size < self.personnage.getY() + GameConfig.persoH + GameConfig.marge and plant.getY() > self.personnage.getY() - GameConfig.marge and self.personnage.getPosition() == plant.getPosition() :
                if self.baquet < 10 :
                    self.baquet = self.baquet + 1
                    self.ensemblePlant.remove(plant)
                    self.score = self.score + 20
            elif plant.getType() == 2 and plant.getY() + GameConfig.plant_size < self.personnage.getY() + GameConfig.persoH + GameConfig.marge and plant.getY() > self.personnage.getY() - GameConfig.marge and self.personnage.getPosition() == plant.getPosition() :
                self.ensemblePlant.remove(plant)
                self.score = self.score - 10
                if self.baquet < 10 :
                    self.baquet = self.baquet + 1
            elif plant.getType() == 3 and plant.getY() + GameConfig.plant_size < self.personnage.getY() + GameConfig.persoH + GameConfig.marge and plant.getY() > self.personnage.getY() - GameConfig.marge and self.personnage.getPosition() == plant.getPosition() :
                self.ensemblePlant.remove(plant)
                self.score = self.score - 5
                if self.baquet < 10 :
                    self.baquet = self.baquet + 1
                    

    def retirer(self) :
        for plant in self.ensemblePlant :
            if plant.getType() == 1 and plant.getY() + GameConfig.plant_size < self.personnage.getY() + GameConfig.persoH + GameConfig.marge and plant.getY() > self.personnage.getY() - GameConfig.marge and self.personnage.getPosition() == plant.getPosition() :
                self.ensemblePlant.remove(plant)
                self.score = self.score - 10
            elif plant.getType() == 2 and plant.getY() + GameConfig.plant_size < self.personnage.getY() + GameConfig.persoH + GameConfig.marge and plant.getY() > self.personnage.getY() - GameConfig.marge and self.personnage.getPosition() == plant.getPosition() :
                self.ensemblePlant.remove(plant)
                self.score = self.score - 10
            elif plant.getType() == 3 and plant.getY() + GameConfig.plant_size < self.personnage.getY() + GameConfig.persoH + GameConfig.marge and plant.getY() > self.personnage.getY() - GameConfig.marge and self.personnage.getPosition() == plant.getPosition() :
                self.ensemblePlant.remove(plant)
                self.score = self.score + 10


    def badPlant(self) :
        for plant in self.ensemblePlant :
            if plant.getType() == 4 and plant.getY() + GameConfig.plant_size < self.personnage.getY() + GameConfig.persoH and plant.getY() > self.personnage.getY() and self.personnage.getPosition() == plant.getPosition() :
                self.ensemblePlant.remove(plant)
                self.score = self.score - 15


    def vider(self) :
        if self.baquet == 10 :
            self.baquet = 0
 
 
    def isOver(self) :
        if self.avancement >= GameConfig.end : #fin du jeu normal
            return True  


def gameLoop(window,horloge) :
    gameState = GameState(window)
    game_over = False
    pygame.key.set_repeat(10,100)
 
    #sontheme = GameConfig.sonTheme #MUSIC DE JEU
    #sontheme.play()
 
    while not game_over :
        nextMove=0
      
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                sontheme.stop()
                game_over = True

            if pygame.key.get_pressed()[pygame.K_LEFT] : #aller à gauche
                nextMove = 1

            elif pygame.key.get_pressed()[pygame.K_RIGHT] : #aller à droite
                nextMove = 2

            elif pygame.key.get_pressed()[pygame.K_UP] : #ramasser melon
                nextMove = 3

            elif pygame.key.get_pressed()[pygame.K_DOWN] : #retier melon pourri
                nextMove = 4

            elif pygame.key.get_pressed()[pygame.K_SPACE] : #vider baquet
                nextMove = 5

        #lancement de l'avancement du jeu
        gameState.advanceState(nextMove)

        #redessinage de la page
        gameState.draw()

        if(gameState.isOver()) :
            try:
                sontheme.stop()
            except :
                print("Sound not found")

            string_score = "Votre score est de : " + str(gameState.score)
            displayMessage(window, string_score,50,GameConfig.windowW/2,GameConfig.windowH/2-50, GameConfig.red)
            displayMessage(window,"Appuyer sur ENTRE pour rejouer",30,GameConfig.windowW/2,GameConfig.windowH/2, GameConfig.blue)
            displayMessage(window,"Appuyer sur ECHAP pour quitter",30,GameConfig.windowW/2,GameConfig.windowH/2+50, GameConfig.blue)
            game_over = True

        pygame.display.update()
        gameState.clear()
 
        horloge.tick(100)

    if(playAgain()) :
        gameLoop(window, horloge)
    else :
        pygame.quit()


def playAgain() :
    time.sleep(1)
    while True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE] :
                return False
            elif pygame.key.get_pressed()[pygame.K_SPACE] or pygame.key.get_pressed()[pygame.K_ENTER]:
                return True
            
            else :
                time.sleep(0.5)
 

def displayMessage(window, text, fontSize, x, y, color) :
    font = pygame.font.Font('BradBunR.ttf',fontSize)
    img = font.render(text, True, color)
    displayRect = img.get_rect()
    displayRect.center=(x,y)
    window.blit(img, displayRect)


def main() :
    pygame.init()
    horloge=pygame.time.Clock()
    window=pygame.display.set_mode((GameConfig.windowW, GameConfig.windowH))
    pygame.display.set_caption("Balisier tycoon")
    gameLoop(window, horloge)
    pygame.quit()
    quit()
 
 
main()
 
 
 
 
 

