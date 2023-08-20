import pygame

pygame.init()
"""Const"""
screen_width, screen_height = 800, 800  # 924, 693; 1366, 768; 1920, 1080; GetSystemMetrics(0), GetSystemMetrics(1)
fps = 60
cell_size = 30
antialias = False
letters = "ABCDEFGHIJ"
"""Fonts"""
grid_font = pygame.font.Font(None, cell_size)
