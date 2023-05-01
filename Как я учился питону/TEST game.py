import pygame
import random
import os
import sys

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
start_img = pygame.image.load(os.path.join(img_folder, 'ground_rock.png'))
mospng = pygame.image.load(os.path.join(img_folder, 'plank.png'))
groundpng = pygame.image.load(os.path.join(img_folder, 'ground.png'))
block = pygame.image.load(os.path.join(img_folder, 'block.png'))
mostpng = pygame.image.load(os.path.join(img_folder, 'plank2.png'))
fipng = pygame.image.load(os.path.join(img_folder, '5.png'))
opng = pygame.image.load(os.path.join(img_folder, '1.png'))
tpng = pygame.image.load(os.path.join(img_folder, '2.png'))
thpng = pygame.image.load(os.path.join(img_folder, '3.png'))
fpng = pygame.image.load(os.path.join(img_folder, '4.png'))
spng = pygame.image.load(os.path.join(img_folder, '6.png'))
red = pygame.image.load(os.path.join(img_folder, 'red.png'))
blue = pygame.image.load(os.path.join(img_folder, 'blue.png'))
green = pygame.image.load(os.path.join(img_folder, 'green.png'))
yellow = pygame.image.load(os.path.join(img_folder, 'yellow.png'))

pygame.init()

WIDTH = 800
HEIGHT = 750
FPS = 60
all_sprites = pygame.sprite.Group()
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

font = pygame.font.SysFont('arial', 30)

objects = []


class wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = start_img
        self.rect = self.image.get_rect()
        self.rect.center = (100, 75)

class wall2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = start_img
        self.rect = self.image.get_rect()
        self.rect.center = (700, 375)

class most(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (150, 75)
        

class wall1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (195, 75)

class most1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (243, 75)

class wallg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (293, 75)

class most2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (336, 75)

class wallg1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (391, 75)

class most3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (429, 75)

class wallg2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (489, 75)

class most4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (522, 75)

class wallg3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (587, 75)

class wallg4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (700, 75)


class most5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (645, 75)

class mostd(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mostpng
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (700, 108)










        

class wallg5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (100, 150)

class wallg6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (700, 150)

class most6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (150, 150)
        

class wallg7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (195, 150)

class most7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (243, 150)

class wallg8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (293, 150)

class most8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (336, 150)

class wallg9(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (391, 150)

class most9(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (429, 150)

class wallg10(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (489, 150)

class most10(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (522, 150)

class wallg11(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (587, 150)

class wallg12(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (700, 150)

class most11(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (645, 150)

class mostd1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mostpng
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 182)


class wallg13(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (100, 225)

class wallg14(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (700, 225)

class most12(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (150, 225)
        

class wallg14(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (195, 225)

class most13(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (243, 225)

class wallg15(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (293, 225)

class most14(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (336, 225)

class wallg16(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (391, 225)

class most15(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (429, 225)

class wallg17(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (489, 225)

class most16(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (522, 225)

class wallg18(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (587, 225)

class wallg19(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (700, 225)


class most17(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (645, 225)

class mostd2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mostpng
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (700, 257)



        

class wallg20(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (100, 300)

class wallg21(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (700, 300)

class most18(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (150, 300)
        

class wallg22(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (195, 300)

class most19(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (243, 300)

class wallg23(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (293, 300)

class most20(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (336, 300)

class wallg24(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (391, 300)

class most21(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (429, 300)

class wallg25(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (489, 300)

class most22(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (522, 300)

class wallg26(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (587, 300)

class wallg27(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (700, 300)
        self.rect.center = (100, 375)

class most23(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (645, 300)

class mostd3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mostpng
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 332)

class wallg28(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (587, 375)
        self.rect.center = (489, 375)

class wallg29(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (587, 375)

class wallg30(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (391, 375)

class wallg31(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (293, 375)

class wallg32(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = groundpng
        self.rect = self.image.get_rect()
        self.rect.center = (191, 375)

class most24(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (645, 375)

class most25(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (522, 375)

class most26(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (429, 375)

class most27(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (336, 375)

class most28(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (243, 375)

class most29(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 25))
        self.image = mospng
        self.rect = self.image.get_rect()
        self.rect.center = (150, 375)

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#e33947',
            'hover': '#6cc4c4',
            'pressed': '#54bf66',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (255, 255, 255))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()
        
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)







class kyb1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image = opng
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)

class kyb2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image = tpng
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)

class kyb3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image = thpng
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)

class kyb4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image = fpng
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)

class kyb5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image = fipng
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)

class kyb6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image = spng
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)
        
kyb4 = kyb4()
kyb5 = kyb5()
kyb6 = kyb6()
kyb2 = kyb2()
kyb3 = kyb3()
kyb1 = kyb1()

class red123(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((12, 13))
        self.image = red
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (88, 63)

red123 = red123()
class kybdat():
    def kyb():
        r1 = random.uniform(1, 6)
        r2 = round(r1)
        if r2 == 1:
           all_sprites.add(kyb1)
           all_sprites.remove(kyb2)
           all_sprites.remove(kyb3)
           all_sprites.remove(kyb4)
           all_sprites.remove(kyb5)
           all_sprites.remove(kyb6)
        elif r2 == 2:
           all_sprites.add(kyb2)
           all_sprites.remove(kyb1)
           all_sprites.remove(kyb3)
           all_sprites.remove(kyb4)
           all_sprites.remove(kyb5)
           all_sprites.remove(kyb6)
        elif r2 == 3:
            all_sprites.add(kyb3)
            all_sprites.remove(kyb2)
            all_sprites.remove(kyb1)
            all_sprites.remove(kyb4)
            all_sprites.remove(kyb5)
            all_sprites.remove(kyb6)
        elif r2 == 4:
           all_sprites.add(kyb4)
           all_sprites.remove(kyb2)
           all_sprites.remove(kyb3)
           all_sprites.remove(kyb1)
           all_sprites.remove(kyb5)
           all_sprites.remove(kyb6)
        elif r2 == 5:
           all_sprites.add(kyb5)
           all_sprites.remove(kyb2)
           all_sprites.remove(kyb3)
           all_sprites.remove(kyb4)
           all_sprites.remove(kyb1)
           all_sprites.remove(kyb6)
        elif r2 == 6:
           all_sprites.add(kyb6)
           all_sprites.remove(kyb2)
           all_sprites.remove(kyb3)
           all_sprites.remove(kyb4)
           all_sprites.remove(kyb5)
           all_sprites.remove(kyb1)

    
        if r2 == 1:
          red123.rect.x += 93.5
        elif r2 == 2:
          red123.rect.x += 187
        elif r2 == 3:
          red123.rect.x += 280.5
        elif r2 == 4:
          red123.rect.x += 374
        elif r2 == 5:
          if red123.rect.center == (88, 63):
              red123.rect.x += 467,5
          elif red123.rect.center == (183, 63):
              red123.rect.x == 682
              red123.rect.y == 63
          elif red123.rect.center == (280, 63):
              red123.rect.x == 682
              red123.rect.y == 132
          elif red123.rect.center == (391 - 17, 63):
              red123.rect.x == 587 - 17
              red123.rect.y == 132
          elif red123.rect.center == (489 - 17, 63):
              red123.rect.x == 489 - 17
              red123.rect.y == 132
          elif red123.rect.center == (587 - 17, 63):
              red123.rect.x == 391 - 17
              red123.rect.y == 132
          elif red123.rect.center == (700 - 17, 63):
              red123.rect.x == 293 - 17
              red123.rect.y == 132
          
        elif r2 == 6:
          if red123.rect.center == (88, 63):
              red123.rect.x += 587
          elif red123.rect.center == (183, 63):
              red123.rect.x == 682
              red123.rect.y == 132
          elif red123.rect.center == (280, 63):
              red123.rect.x == 570
              red123.rect.y == 132
          elif red123.rect.center == (391 - 17, 63):
              red123.rect.x == 489 - 17
              red123.rect.y == 132
          elif red123.rect.center == (489 - 17, 63):
              red123.rect.x == 391 - 17
              red123.rect.y == 132
          elif red123.rect.center == (587 - 17, 63):
              red123.rect.x == 293 - 17
              red123.rect.y == 132
          elif red123.rect.center == (700 - 17, 63):
              red123.rect.x == 195 - 17
              red123.rect.y == 132
          
            
        


        





    






        








    

    
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Бродилка Белоиванова")
clock = pygame.time.Clock()
most24 = most24()
most25 = most25()
most26 = most26()
most27 = most27()
most28 = most28()
most29 = most29()
wallg30 = wallg30()
wallg31 = wallg31()
wallg32 = wallg32()
wall = wall()
wall2 = wall2()
most = most()
wall1 = wall1()
most1 = most1()
wallg = wallg()
most2 = most2()
wallg1 = wallg1()
most3 = most3()
wallg2 = wallg2()
most4 = most4()
wallg3 = wallg3()
wallg4 = wallg4()
most5 =  most5()
mostd = mostd()
most6 = most6()
most7 = most7()
most8 = most8()
most9 = most9()
most10 = most10()
most11 = most11()
wallg5 = wallg5()
wallg6 = wallg6()
wallg7 = wallg7()
wallg8 = wallg8()
wallg9 = wallg9()
wallg10 = wallg10()
wallg11 = wallg11()
mostd1 = mostd1()
most12 = most12()
most13 = most13()
most14 = most14()
most15 = most15()
most16 = most16()
most17 = most17()
most18 = most18()
most19 = most19()
most20 = most20()
most21 = most21()
most22 = most22()
most23 = most23()
mostd2 = mostd2()
mostd3 = mostd3()
wallg13 = wallg13()
wallg14 = wallg14()
wallg15 = wallg15()
wallg16 = wallg16()
wallg17 = wallg17()
wallg18 = wallg18()
wallg29 = wallg29()
wallg19 = wallg19()
wallg20 = wallg20()
wallg21 = wallg21()
wallg22 = wallg22()
wallg23 = wallg23()
wallg24 = wallg24()
wallg25 = wallg25()
wallg26 = wallg26()
wallg27 = wallg27()
wallg12 = wallg12()
wallg28 = wallg28()

    
        
    

customButton = Button(0, 650, 200, 100, '1 - ый игрок', kybdat.kyb)
customButton = Button(200, 650, 200, 100, '2 - ой игрок', kybdat)
customButton = Button(400, 650, 200, 100, '3 - ий игрок', kybdat)
customButton = Button(600, 650, 200, 100, '4 - ый игрок', kybdat)





all_sprites.add(most29, most28, most27, most26, most25, most24, wallg32, wallg31, wallg30, wallg29, wallg28, wall, wall2, most, wall1, most1, wallg, most2, wallg1, most3, wallg2, most4, wallg3, wallg4, most5, mostd, mostd1, most6, most7, most8, most9, most10, most11, wallg5, wallg6, wallg7, wallg8, wallg9, wallg10, wallg11, wallg12, most13, most14, most15, most16, most17, most18, most19, most20, most21, most22, most23, mostd2, mostd3, wallg13, wallg14, wallg15, wallg16, wallg17, wallg18, wallg19, wallg20, wallg21, wallg22, wallg23, wallg24, wallg25, wallg26, wallg27, red123)
print(objects)
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
    
    # Рендеринг
    screen.fill(WHITE)
    all_sprites.draw(screen)
    for object in objects:
        object.process()
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()

