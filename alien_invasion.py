import sys
import pygame
from ai import ai

from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self):
        #инит настройки игры
        pygame.init()
        
        self.settings = Settings()
        self.ship = Ship(self.screen)

        self.bgcolor = (self.settings.bgcolor)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_widght, self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion")




    def run_game(self):
     while True:
             #нажатия контроль
            for event in pygame.event.get():
                #если закрыть окно
                if event.type == pygame.QUIT:
                    sys.exit()
   
          # Перерисоывается экран
            self.screen.fill(self.bgcolor)
            self.ship.blittime()

         # Последний отрисованый экран
            pygame.display.flip()

if __name__ == '__main__':
    
    ai.run_game()