from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import sys
import pygame

import config as cfg

from class_grid import Grid

screen = pygame.display.set_mode((cfg.screen_width, cfg.screen_height))  # pygame.FULLSCREEN
clock = pygame.time.Clock()


def main():
    grid = Grid((40, 40))

    run = True
    while run:
        # events
        for event in pygame.event.get():
            grid.handle_event(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # graphics
        screen.fill(pygame.Color("white"))

        grid.draw_grid(screen)

        # display flip
        clock.tick(cfg.fps)
        pygame.display.flip()


if __name__ == "__main__":
    main()
