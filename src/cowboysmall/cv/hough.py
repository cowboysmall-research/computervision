import sys
import math

import numpy as np

from PIL import Image



def read_image(path):
    return Image.open(path).convert('L')


def write_image(space, path):
    Image.fromarray(space).save(path)


def hough_space(image, width = 640, height = 480):
    img    = image.load()
    w, h   = image.size
    diag   = math.hypot(w, h)

    accum  = np.full((height, width), 255, dtype = np.uint8)

    thetas = np.arange(0, math.pi, math.pi / width)
    cos    = np.cos(thetas)
    sin    = np.sin(thetas)

    for i in range(w):
        for j in range(h):
            if img[i, j] != 255:
                for x in range(width):
                    rho = i * cos[x] + j * sin[x]
                    y   = int((height / 2) + round((rho / (diag * 2)) * height))
                    accum[y, x] -= 1

    return accum

