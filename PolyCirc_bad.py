import numpy
import math
import pygame
import sys

width = 1500
height = 1000
x_center = width/2
y_center = height/2

screen_color = screen_color = (0, 0, 1)
line_color = (255, 0, 0)
poly_coords = []

def generate_polygon_coords():
    radius = 100
    sides = 3
    theta = math.pi/4
    for current_side in range(0,sides):
        x = x_center+radius * math.cos(2*math.picurrent_side/sides) 
        y = y_center+radius * math.sin(2*math.picurrent_side/sides)
        x_rotated = x * math.cos(theta) - y * math.sin(theta)
        y_rotated = x * math.sin(theta) + y * math.cos(theta)
        coord = tuple([x_rotated,y_rotated])
        poly_coords.append(coord)
    poly_coords.append(poly_coords[0])
    return poly_coords

def main(poly_coords):
    screen=pygame.display.set_mode((width,height))
    screen.fill(screen_color)
    pygame.draw.lines(screen,line_color,True,poly_coords)
    pygame.display.flip()

    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit(0)

if __name__ == "__main__":
    coords = generate_polygon_coords()
    main(coords)