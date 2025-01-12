import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__width = 2
    
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), self.position, self.radius, self.__width)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        change_angle = random.uniform(20, 50)
        left_velocity = self.velocity.rotate(change_angle)
        right_velocity = self.velocity.rotate(-change_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        right_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        left_asteroid.velocity = left_velocity * 1.2
        right_asteroid.velocity = right_velocity * 1.2
        