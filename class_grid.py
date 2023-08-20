import pygame
import config as cfg
from class_cell import Cell


# TODO: ship addition process

class Grid:
    def __init__(self, position: (int, int), visible=True):
        self.char_color = pygame.Color("darkgreen")
        self.width = 10
        self.height = 10
        self.rect = pygame.Rect(position, (self.width * cfg.cell_size, self.height * cfg.cell_size))
        self.data = []

        cell_x, cell_y = 0, 0
        cell_id = 0
        for height in range(self.height):
            temp = []

            for width in range(self.width):
                temp.append(Cell(cell_id, 0, (self.rect.x + cell_x, self.rect.y + cell_y), visible))
                cell_id += 1
                cell_x += cfg.cell_size

            self.data.append(temp)
            cell_y += cfg.cell_size
            cell_x = 0

    def draw_grid(self, surface):
        for line in self.data:
            for cell in line:
                if cell.content == 0 or not cell.visible:
                    pygame.draw.rect(surface, pygame.Color("lightgray"), cell.rect, 1)
                elif cell.content == 1:
                    pygame.draw.rect(surface, pygame.Color("blue"), cell.rect, 1)

        number_x, number_y = self.rect.x - cfg.cell_size, self.rect.y
        for numb in range(10):
            text = cfg.grid_font.render(str(numb + 1), cfg.antialias, self.char_color)
            surface.blit(text, (number_x + (0 if numb == 9 else (cfg.cell_size / 4)), number_y + 5))
            number_y += cfg.cell_size

        letter_x, letter_y = self.rect.x, self.rect.y - cfg.cell_size
        for letter in cfg.letters:
            text = cfg.grid_font.render(letter, cfg.antialias, self.char_color)
            surface.blit(text, (letter_x + 8, letter_y + 5))
            letter_x += cfg.cell_size

        border_rect = (self.rect.x - 2, self.rect.y - 2, self.rect.width + 3, self.rect.height + 4)
        pygame.draw.rect(surface, pygame.Color("dimgray"), border_rect, 1)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.rect.collidepoint(pygame.mouse.get_pos()):
            for line in self.data:
                for cell in line:
                    cell.handle_event(event)

    def set_position(self, position: (int, int)):
        self.rect = pygame.Rect(position, (self.width * cfg.cell_size, self.height * cfg.cell_size))
