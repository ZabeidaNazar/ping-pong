import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame



class GameSprite(pygame.sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = pygame.transform.scale(pygame.image.load(player_image), (wight, height)) #разом 55,55 - параметри
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def draw(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
   def update_r(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[pygame.K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[pygame.K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
 
back = (200, 255, 255)
win_width = 600
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
window.fill(back)
 
run = True
finish = False
clock = pygame.time.Clock()
FPS = 60
 
 
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
           run = False
  
    
    pygame.display.update()
    clock.tick(FPS)
