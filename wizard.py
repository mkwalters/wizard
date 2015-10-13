import pygame
import random 
import math

pygame.init()


display_width = 800
display_height = 600


fireballs = []
enemies = []

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('wizard')
clock = pygame.time.Clock()

wizard_img = pygame.image.load('wizard.png')
shadow_img = pygame.image.load('shadow.png')
ent_img = pygame.image.load('ent.png')
gargoyle_img = pygame.image.load('gargoyle.png')
gargoyle_width = 88


class Wizard():
    def __init__(self):
        self.wizardx = display_width /2 - 25
        self.wizardy = display_height - 100
        self.xvelocity = 0
        self.yvelocity = 0
    

    def draw_self(self):
        gameDisplay.blit(wizard_img, (self.wizardx, self.wizardy))

    def cast_fireball(self, mousex, mousey):
        fireballs.append(Fireball(mousex,mousey))
    
    def move_left(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
        
                self.wizardx += -5
        
    
    
        

class Fireball():
    def __init__(self , x, y):
        self.xpos = mitchell.wizardx + 15
        self.ypos = mitchell.wizardy - 10
        self.velocity = 10
        self.width = 8
        self.damage = 5
        
        self.theta = math.atan2((y - self.ypos),(x - self.xpos))
        
        self.xchange = self.velocity * math.cos(self.theta)
        self.ychange = self.velocity * math.sin(self.theta)
        
    
    def check_bounds(self):
        if self.xpos < 0 or self.xpos > display_width:
            fireballs.remove(self)
        if self.ypos < 0 or self.ypos > display_height:
            fireballs.remove(self)
            
    
    def draw_self(self):
        pygame.draw.rect(gameDisplay, (255,0,0), [self.xpos, self.ypos, self.width, self.width])
        self.xpos += self.xchange
        self.ypos += self.ychange
    
    def get_rekt(self):
        for i in enemies:
            if self.xpos > i.xpos and (self.xpos + self.width) < (i.xpos + i.width):
                if self.ypos > i.ypos and (self.ypos + self.width) < (i.ypos + i.height):
                    i.health = i.health - self.damage
                    print i.health /i.starting_health
                    
                    fireballs.remove(self)
                    if i.health <= 0:
                        enemies.remove(i)
                
                
        
class Enemy():
    def __init__(self):
        self.xpos = random.randint(0, display_width)
        self.ypos = 0
        self.velocity = 2
        
        self.health = 15
        self.starting_health = 15
        
        
    def draw_health_bar(self, width):
        pygame.draw.rect(gameDisplay, (0,0,0) ,[self.xpos, self.ypos -8 , width ,10])
        pygame.draw.rect(gameDisplay, (255,0,0) ,[self.xpos, self.ypos -8, (width * self.health / self.starting_health),10])
        
    def check_bounds(self):
        if self.ypos > display_height - 100:
            enemies.remove(self)
        
    
    def move(self):
        self.ypos += self.velocity
        
    
class Shadow(Enemy):
    width = 40
    height = 41
    
    
    def draw_self(self):
        self.draw_health_bar(40)
        gameDisplay.blit(shadow_img, (self.xpos, self.ypos))
    
class Ent(Enemy):
    width = 47
    height = 54

    def draw_self(self):
        self.draw_health_bar(47)
        gameDisplay.blit(ent_img, (self.xpos, self.ypos))
    
class Gargoyle(Enemy):
    def __init__(self):
        self.xpos = random.randint(0, display_width)
        self.ypos = 0
        self.velocity = 2
        
        self.health = 30
        self.starting_health = 30
    width = 88
    height = 93
    def draw_self(self):
        self.draw_health_bar(88)
        gameDisplay.blit(gargoyle_img, (self.xpos, self.ypos))
    
class Portal():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        
        
    def draw_portal(self):
        pygame.draw.rect(gameDisplay, (0,0,0), [self.x, self.y, self.width, self.height])

    def enemy_spawner(self):
        roll = random.randint(0,1000)
        if roll >20 and roll < 30:
            enemies.append(Gargoyle())
    
        if roll < 20 and roll > 10:
            enemies.append(Ent())
        
        if roll< 10:
            enemies.append(Shadow())
            
  




portal1 = Portal(100,100)
mitchell = Wizard()
still_playing = True

while still_playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            mitchell.cast_fireball(mouse[0], mouse[1])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                
                mitchell.xvelocity += -2
            elif event.key == pygame.K_RIGHT:
                mitchell.xvelocity += 2
                
            elif event.key == pygame.K_UP:
                mitchell.yvelocity += -2
                
            elif event.key == pygame.K_DOWN:
                mitchell.yvelocity += 2
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                mitchell.xvelocity = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                mitchell.yvelocity = 0
        
    
    gameDisplay.fill((35,183,69))
    mitchell.wizardx += mitchell.xvelocity
    mitchell.wizardy += mitchell.yvelocity
    portal1.enemy_spawner()
    for i in fireballs:
        i.draw_self()
        i.check_bounds()
        i.get_rekt()
    for i in enemies:
        i.move()
        i.check_bounds()
        i.draw_self()
        
        
    mitchell.draw_self()
    
    
    
    pygame.display.update()
    clock.tick(50)