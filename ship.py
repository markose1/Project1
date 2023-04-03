import pygame
class Ship:
    """A class to manage the ship."""
    def __init__(self,ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('Project1/ship.bmp') #Load the ship image and get its rect.
        self.rect = ai_game.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom #start each new ship at the bottom center of the screen.
        self.moving_right = False #Movement flag; start with a ship that's not moving.
        self.moving_left = False
    def update(self):
        """Update the ship's positionbased on the movement flag."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)