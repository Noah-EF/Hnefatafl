import pygame
from board import Board

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

top_left = 115, 115  # y, x
square_size = 70
board_size = 7
board = Board(screen, top_left, board_size, square_size)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # background color
    # TODO move into event loop to only re-render when needed
    screen.fill((135, 203, 245))
    board.draw()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
