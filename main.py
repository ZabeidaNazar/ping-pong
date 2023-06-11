import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, random



class GameSprite(pygame.sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = pygame.transform.scale(pygame.image.load(player_image), (wight, height))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def draw(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update_r(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_o] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[pygame.K_l] and self.rect.bottom < win_height:
           self.rect.y += self.speed
   def update_l(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[pygame.K_s] and self.rect.bottom < win_height:
           self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, speed_x, speed_y, wight, height):
        super().__init__(player_image, player_x, player_y, 0, wight, height)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.x <= 0 or self.rect.right >= win_width:
            self.speed_x *= -1
        
        if self.rect.y <= 0 or self.rect.bottom >= win_height:
            self.speed_y *= -1

    def check_collide(self, rect):
        if self.rect.colliderect(rect):
            self.speed_x *= -1
            # self.speed_y *= random.choice([-1, 1])

back = (200, 255, 255)
win_width = 600
win_height = 500
pygame.display.set_caption("Ping Pong")
window = pygame.display.set_mode((win_width, win_height))
window.fill(back)

# Created sprites
platform1 = Player("images\\racket.png", 20, 20, 5, 25, 150)
platform2 = Player("images\\racket.png", 555, 20, 5, 25, 150)
ball = Ball("images\\tenis_ball.png", win_width // 2 - 55 // 2, win_height // 2 - 60, 7, 2, 55, 55)

run = True
finish = False
clock = pygame.time.Clock()
FPS = 60
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
           run = False

    window.fill(back)

    platform1.draw()
    platform2.draw()
    platform1.update_l()
    platform2.update_r()

    ball.draw()
    ball.move()
    ball.check_collide(platform1)
    ball.check_collide(platform2)
  
    
    pygame.display.update()
    clock.tick(FPS)
