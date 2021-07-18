from const import *
import pygame


class Cell:
    def __init__(self, x=0, y=0, width=CELL_WIDTH, height=CELL_HEIGHT, color=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.row = 0
        self.col = 0
        self.color = color # color of square: dark or light brown
        self.inside = None # which player inside black/ white
        self.is_king = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, WIDTH // 8, HEIGHT // 8])

    def is_inside(self, x, y):
        if (self.x < x < self.x + self.width) and (self.y < y < self.y + self.height):
            return True
        return False

    def __repr__(self):
        if self.color == DARK_BROWN:
            return "dark brown"
        else:
            return "light brown"

    def __eq__(self, other):
        if other is None or type(other) == str:
            return False
        if self is None or type(self) == str:
            return False
        elif self.row == other.row and self.col == other.col:
            return True
        return False
