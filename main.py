from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import sys
import pygame
import random

import config as cfg

screen_width, screen_height = 800, 800  # 924, 693; 1366, 768; 1920, 1080; GetSystemMetrics(0), GetSystemMetrics(1)
screen = pygame.display.set_mode((screen_width, screen_height))  # pygame.FULLSCREEN
clock = pygame.time.Clock()


def main():
    while True:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # graphics
        screen.fill(pygame.Color("black"))

        clock.tick(cfg.fps)
        pygame.display.flip()


if __name__ == "__main__":
    main()
