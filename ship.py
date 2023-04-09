import pygame
 
class Ship:
    """Управление кораблём."""
 
    def __init__(self, ai_game):
        """Ставить корабль в мидботтом и отображает его."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

#спрайт корабля (py-aliens\img\ship.bmp)
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()

# Позиция на экране
        self.rect.midbottom = self.screen_rect.midbottom
        
        #Скорость float
        self.x = float(self.rect.x)

#Флаги перемещения

        self.moving_right = False
        self.moving_left = False  
  
        #Обновление на экране и скорости
    def update(self):
       if self.moving_right and self.rect.right < self.screen_rect.right:
          self.x += self.settings.ship_speed
       elif self.moving_left and self.rect.left:
          self.x -= self.settings.ship_speed

       self.rect.x = self.x
        

    def blitme(self):
        self.screen.blit(self.image, self.rect)
