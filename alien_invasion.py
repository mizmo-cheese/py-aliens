
import pygame
import sys

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    

    def __init__(self):
        
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode(
            (0, 0,), pygame.FULLSCREEN)
        
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_widght = self.screen.get_rect().width

        pygame.display.set_caption("Alien Invasion")


        self.bullet = pygame.sprite.Group
        self.ship = Ship(self)


    def _check_events(self):
        for event in pygame.event.get():   
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self.keydown_event(event)   
                elif event.type == pygame.KEYUP:
                   self.keyup_event(event)
                
    def keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
          self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_F9:
            sys.exit()
    
    def keyup_event(self, event):  
         if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
         if event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

# "updating screen"
    def _screen_update(self):
        self.screen.fill(self.settings.bgcolor)
        self.ship.blitme()
           
        pygame.display.flip()

    def run_game(self):
      while True:
          self._check_events()
          self.ship.update()
          self._screen_update()
          self.bullet.update()

    

if __name__ == '__main__':
  
    ai = AlienInvasion()
    ai.run_game()
