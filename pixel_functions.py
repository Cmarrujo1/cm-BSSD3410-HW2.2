from PIL import Image, ImageDraw


def compare_pixels(pix1, pix2):
    return pix1[0] > pix2[0]

def store_pixels(im):
    width = int(im.size[0])
    length = int (im.size[1])

    pixel_arr = []
    for i in range(width):
        for j in range(height):
            r, g, b = im.getpixel((i, j))
            pixel_arr.append([(r,g,b), (i, j)])

    return pixel_arr

def pixels_to_image(im, pixels):
    outimg = Image.new( "RGB", im.size)
    outimg.putdata([p[0] for p in pixels])
    return outimg


def grayscale(im, pixels):
    draw = ImageDraw.Draw(im)
    for px in pixels:
        gray_av = int((px[0][0] + px[0][1] + px[0][2]) /3)
        draw.point(px[1], (gray_av, gray_av, gray_av))

