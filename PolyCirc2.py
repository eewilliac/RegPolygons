import numpy
import math
import pygame

def simple():
    sides =4
    radius =100
    angle = 360/sides
    for current_side in range(1,sides):
        x = radius * math.cos(360/current_side)
        y = radius * math.sin(360/current_side)
        print("{},{}",x,y)


if __name__ == "__main__":
    simple()