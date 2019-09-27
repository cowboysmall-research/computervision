import sys
import math

import numpy as np

from PIL import Image



def read_image(path):
    return Image.open(path).convert('L')


def write_image(space, path):
    Image.fromarray(space).save(path)


def hough_space_01(image, width = 640, height = 480):
    img     = image.load()
    w, h    = image.size
    diag    = math.hypot(w, h)

    accum   = np.full((height, width), 255, dtype = np.uint8)

    for i in range(w):
        for j in range(h):
            if img[i, j] != 255:
                for x in range(width):
                    theta = (math.pi / width) * x
                    rho   = i * math.cos(theta) + j * math.sin(theta)
                    y     = int((height / 2) + round((rho / (diag * 2)) * height))
                    accum[y, x] -= 1

    return accum


def hough_space_02(image, width = 640, height = 480):
    img    = image.load()
    w, h   = image.size
    diag   = math.hypot(w, h)

    thetas = np.arange(0, math.pi, math.pi / width)
    cos    = np.cos(thetas)
    sin    = np.sin(thetas)

    accum  = np.full((height, width), 255, dtype = np.uint8)

    for i in range(w):
        for j in range(h):
            if img[i, j] != 255:
                for x in range(width):
                    rho = i * cos[x] + j * sin[x]
                    y   = int((height / 2) + round((rho / (diag * 2)) * height))
                    accum[y, x] -= 1

    return accum

 
def main(argv):
    image = read_image('./data/hough/images/pentagon.png')
    space = hough_space_01(image)
    write_image(space, './data/hough/transformed/hough_pentagon_01.png')
    space = hough_space_02(image)
    write_image(space, './data/hough/transformed/hough_pentagon_02.png')


    image = read_image('./data/hough/images/hexagon.jpg')
    space = hough_space_01(image)
    write_image(space, './data/hough/transformed/hough_hexagon_01.png')
    space = hough_space_02(image)
    write_image(space, './data/hough/transformed/hough_hexagon_02.png')


    image = read_image('./data/hough/images/octagon.png')
    space = hough_space_01(image)
    write_image(space, './data/hough/transformed/hough_octagon_01.png')
    space = hough_space_02(image)
    write_image(space, './data/hough/transformed/hough_octagon_02.png')

 
if __name__ == "__main__":
    main(sys.argv[1:])

