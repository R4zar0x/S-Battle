import pygame
from class_cell import Cell

class Grid:
    def __init__(self):
        self.width = 10
        self.height = 10

        self.data = []

        for iterator in range(self.width * self.height):
            self.data.append(Cell(0))

