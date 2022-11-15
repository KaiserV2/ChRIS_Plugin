# read in a jpg file and print the rgb of each pixel

import matplotlib.image as mpimg
from PIL import Image


def invert_image(inputdir, outputdir):
    im = Image.open(inputdir)
    im = im.convert("RGB")
    # for all of the pixels, invert the rgb values
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            r, g, b = im.getpixel((x, y))
            im.putpixel((x, y), (255 - r, 255 - g, 255 - b))
    im.save(outputdir)


    


def main():
    invert_image("/users/KaiserW/ChRIS_Plugin/input.jpg", "/users/KaiserW/ChRIS_Plugin/output.jpg")

if __name__ == '__main__':
    main()
