import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__width = 2
    
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), self.position, self.radius, self.__width)
    
    def update(self, dt):
        self.position += self.velocity * dt