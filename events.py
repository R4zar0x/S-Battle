import pygame
import config


def events_handler():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.run = False
        