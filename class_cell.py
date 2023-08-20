import pygame
import config as cfg


class Cell:
    def __init__(self, cell_id, content: int, position: (int, int), visible):
        self.id = cell_id
        self.content = content
        self.visible = visible
        self.rect = pygame.Rect(position, (cfg.cell_size - 1, cfg.cell_size - 1))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.content = 1
            # print("hit on cell", self.id)

    def set_position(self, position: (int, int)):
        self.rect = pygame.Rect(position, (cfg.cell_size - 1, cfg.cell_size - 1))
