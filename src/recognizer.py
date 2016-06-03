# if you'r on a 32 bit OS:
# import Image

from PIL import Image

import numpy as np
import matplotlib.pyplot as plt

img = Image.open('images/img1.png')

# an array that corresponds into 'img' image
# and the image array will come out in a 3 dim array

# Array => (R, G, B, Alpha)

imageArray = np.asarray(img)

# print imageArray

plt.imshow(imageArray)
plt.show()

