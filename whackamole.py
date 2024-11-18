import pygame
from constants import *
import random

mole_image = pygame.image.load("mole.png")

screen = pygame.display.set_mode((640, 512))

def draw_grid():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )

    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
        )

def draw_mole(screen, x, y):
    screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))


def main():
    try:
        pygame.init()
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mole_x = random.randrange(0, WIDTH, SQUARE_SIZE)
                    mole_y = random.randrange(0, HEIGHT, SQUARE_SIZE)
            screen.fill("light green")
            draw_grid()
            draw_mole(screen, mole_x, mole_y)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

