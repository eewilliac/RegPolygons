import math
import pygame
import sys

width = 1500
height = 1000
x_center = width / 2
y_center = height / 2

screen_color = (0, 0, 1)
line_color = (255, 0, 0)

def generate_polygon_coords(radius, sides, rotation):
    coords = []
    for i in range(sides):
        angle = 2 * math.pi * i / sides + rotation
        x = radius * math.cos(angle) + x_center
        y = radius * math.sin(angle) + y_center
        coords.append((x, y))
    coords.append(coords[0])
    return coords

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    radius = 100
    sides = 8
    rotation = 0
    rotation_speed = 0.01  # Radians per frame

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        rotation += rotation_speed
        poly_coords = generate_polygon_coords(radius, sides, rotation)

        screen.fill(screen_color)
        pygame.draw.lines(screen, line_color, True, poly_coords)
        pygame.display.flip()

        clock.tick(60)  # Limit to 60 FPS

if __name__ == "__main__":
    main()