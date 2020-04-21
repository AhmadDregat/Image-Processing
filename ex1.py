import numpy as np

import numpy.matlib
import matplotlib.pyplot as plt
import  cv2



def imReadAndConvert(filename, representation):
    # Loading an image
    img = cv2.imread(filename)
    if img is not None:
        # normolaize pixels
        img = img * (1. / 255)
        if representation == 1:
            # representation = 1 means grayscale image
            img = RGBtoGray(img)
        else:
            # representation = 2 means RGB image
            b, g, r = cv2.split(img)
            img = cv2.merge([r, g, b])
    else:
        print("Invalid path for image")

    return img