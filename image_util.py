#!/usr/bin/python3

from skimage import util
from skimage import io
from skimage import exposure
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
import sys
import numpy as np

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("need a image file path as input")
    sys.exit(1)

img = io.imread(filename)
img0 = img[:, :, 0]
img_shape = img0.shape
#invert_img = util.invert(img)
#
##io.imshow(invert_img)
#
#print("hist ", exposure.histogram(img0))
#
##img_gamma = exposure.adjust_gamma(img)
img_zero = np.empty(shape=(img_shape[0], img_shape[1]))
img_zero.fill(0)

img_contrast = np.empty(shape=img.shape).astype(int)
img_contrast[:, :, 0] = img[:, :, 0]
img_contrast[:, :, 1] = img[:, :, 1]
img_contrast[:, :, 2] = img_zero

print ("max ", img_contrast[:, :, 0].max(), img_contrast[:, :, 1].max(), img_contrast[:, :, 2].max())
print ("min ", img_contrast[:, :, 0].min(), img_contrast[:, :, 2].min(), img_contrast[:, :, 2].min())

fig = plt.figure(figsize = (100, 100))
gs = GridSpec(1, 2)
ax0 = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[0, 1])

ax0.imshow(img)
ax0.set_title('original')
ax1.imshow(img_contrast)
ax1.set_title('gamma')

plt.plot()
plt.show()
