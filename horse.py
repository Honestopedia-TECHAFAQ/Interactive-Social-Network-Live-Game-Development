import pygame
import random

class Horse:
    def __init__(self, color, y_position, name):
        self.color = color
        self.x_position = 50
        self.y_position = y_position
        self.speed = 5
        self.name = name

    def move_forward(self):
        self.x_position += random.randint(1, self.speed)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x_position, self.y_position, 50, 30])

    def reset_position(self):
        self.x_position = 50
