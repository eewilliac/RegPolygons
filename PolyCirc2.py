import numpy
import math
import pygame
import sys

width = 1000
height = 500
screen_color = screen_color = (0, 0, 1)
line_color = (255, 0, 0)
poly_coords = []

def generate_polygon_coords():
    sides = 4
    radius = 100
    angle = 360/sides
    angle = angle * (math.pi / 180) #convert to radians
    for current_side in range(0,sides):
        x = 100 + radius * math.cos(angle*current_side)
        y = 100 + radius * math.sin(angle*current_side)
        coord = tuple([x,y])
        poly_coords.append(coord)
    poly_coords.append(poly_coords[0])
    return poly_coords

def main(poly_coords):
    screen=pygame.display.set_mode((width,height))
    screen.fill(screen_color)
    #pygame.draw.line(screen,line_color, (60, 80), (130, 100))
    pygame.draw.lines(screen,line_color,True,poly_coords)
    pygame.display.flip()

    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit(0)



if __name__ == "__main__":
    coords = generate_polygon_coords
    main(coords)