# if you'r on a 32 bit OS:
# import Image

from PIL import Image
import numpy as np

img = Image.open('images/img11.png')

# an array that corresponds into 'img' image
# and the image array will come out in a 3 dim array

imgAsArray = np.asarray(img)

print imgAsArray
