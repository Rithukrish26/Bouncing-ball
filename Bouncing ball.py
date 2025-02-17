import pygame
import sys
from PyGame import circx

pygame.init()




screen_width = 1000
screen_height = 600
circx, circy= 200,100
speedx,speedy= 0.6893,0.6893


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Basics")


background_color = (26,1,245)


running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
   screen.fill(background_color)
   circx+=speedx
   circy+=speedy
   if circx + 29 > screen_width or circx - 29 < 0:
       speedx = -speedx
   if circy + 29 > screen_height or circy - 29 < 0:
       speedy = -speedy

   pygame.draw.circle(screen,"White",(circx,circy),29)
   pygame.display.flip()
