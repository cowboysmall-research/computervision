from cowboysmall.cv import hough


def test():
    image = hough.read_image('./data/hough/images/pentagon.png')
    space = hough.hough_space(image)
    hough.write_image(space, './images/hough/transformed/pentagon.png')

    image = hough.read_image('./data/hough/images/hexagon.jpg')
    space = hough.hough_space(image)
    hough.write_image(space, './images/hough/transformed/hexagon.png')

    image = hough.read_image('./data/hough/images/octagon.png')
    space = hough.hough_space(image)
    hough.write_image(space, './images/hough/transformed/octagon.png')

