import sys
import pygame

from settings import Settings


class AlienInvasion:

    def __init__(self):
        #инит настройки игры
        pygame.init()
        self.settings = Settings()

        self.bgcolor = (230, 230, 230)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_widght, self.settings.screen_height))
        pygame.display.set_caption("Заголовок")



    def run_game(self):
     while True:
             #нажатия контроль
            for event in pygame.event.get():
                #если закрыть окно
                if event.type == pygame.QUIT:
                    sys.exit()
   
          # Перерисоывается экран
            self.screen.fill(self.bgcolor)

         # Последний отрисованый экран
            pygame.display.flip()

if __name__ == '__main__':
    
    ai = AlienInvasion()
    ai.run_game()