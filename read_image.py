#!/usr/bin/python3

from skimage import io
from matplotlib import pyplot as plt
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("need a image file path as input")
    sys.exit(1)

img = io.imread(filename)

print("type ", type(img))
print("dimension ", img.shape)

print(img[10, 20])

io.imshow(img)
plt.show()
