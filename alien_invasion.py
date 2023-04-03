#Creating a Pygame window and Responding to User Input
import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion:
    #Controlling the Frame Rate
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init() #initializes the background settings that Pygame needs to work properly
        self.clock = pygame.time.Clock() #we create an instance of the class 'Clock'
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200,800)) #assigned this display window to the attribute 'self.screen' so it will be available in all methods in the class
        """creates a display window that we'll draw all the game's graphical elements. 
        The argument (1200,800) is a tuple that defines the dimensions of the game window, 
        which will be 1,200 pixels wide and 800 pixels high."""
        pygame.display.set_caption("Alien Invasion") 
        self.ship = Ship(self) #import Ship class and make an instance of Ship
        #Setting the Background Color
        self.bg_color = (230, 230, 230) #sets the background color as light grey.
    def run_game(self): #Controls the game
        """Start the main loop for the game."""
        while True: 
            """Watch for keyboard and mouse events."""
            self._check_events()
            self.ship.update()
            self._update_screen()
            pygame.display.flip()
            """Makes the most recently drawn screen visible. Continually updates the display to show 
            the new positions of game elements and hide the old ones, creating the illusion of smooth movement."""
            self.clock.tick(60) #sets the frame rate in the argument, makes the loop run 60 times per second
    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get(): #Event loop manages the screen updates,listens for events and perform appropriate tasks depending on the kind of event that occurs.
                """To access the events that Pygame detects, we use the function 'pygame.event.get()'. Which returns a list of events 
                that have taken place since the last time we called the function. Any keyboard or mouse event will cause this for loop to run"""
                if event.type == pygame.QUIT: #when the player clicks the game window"s close button, a pygame.QUIT event is detected
                    """meant to detect and respond to specific events.""" 
                    sys.exit() #calls sys.exit() to exit the game.
                elif event.type == pygame.KEYDOWN: #responds to keydown event
                    if event.key == pygame.K_RIGHT: #checks to see if the right arrow key was pressed
                        """Move the ship to the right."""
                        self.ship.moving_right = True #and if so we set 'moving_right' to True
                    elif event.key == pygame.K_LEFT: #checks to see if the left arrow key was pressed
                        """Move the ship to the right."""
                        self.ship.moving_left = True #and if so we set 'moving_left' to True
                elif event.type == pygame.KEYUP: #responds to keyup event
                    if event.key == pygame.K_RIGHT: #checks to see if the player released the right arrow key 
                        """Move the ship to the right."""
                        self.ship.moving_right = False #and if so we set 'moving_right' to False
                    elif event.key == pygame.K_LEFT: #checks to see if the left arrow key was pressed
                        """Move the ship to the right."""
                        self.ship.moving_left = False #and if so we set 'moving_left' to True
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
if __name__ == '__main__': #only runs if the file is called directly 
    """Make a game instance, and run the game."""
    ai = AlienInvasion() #Create instance of the game 
    ai.run_game() 