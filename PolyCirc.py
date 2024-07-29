#application for Regular polygon and circles.
import pygame
import sys

width = 1000
height = 500
screen_color = screen_color = (0, 0, 1)
line_color = (255, 0, 0)
poly_coords = []

def generate_poly_coords():
    #do something
    print("generate polygon coordinates")

def main():
    screen=pygame.display.set_mode((width,height))
    screen.fill(screen_color)
    pygame.draw.line(screen,line_color, (60, 80), (130, 100))
    pygame.display.flip()

    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit(0)


if __name__ == "__main__":
    main()