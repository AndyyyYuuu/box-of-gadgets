# Andy Yu
# Nov 23, 2023
# Image blurring: 2d convolution, greyscale only
from PIL import Image
import scipy, numpy
BLUR = 24
img = Image.open("dmitri.jpeg")
pixels = img.load()
pix_arr = []
for i in range(img.size[1]):
    row = []
    for j in range(img.size[0]):
        row.append(pixels[j, i])
    pix_arr.append(row)
print(img.size)

kernel_size = BLUR
sigma = BLUR/3
kernel = numpy.fromfunction(lambda x, y: (1/(2*numpy.pi*sigma**2)) * numpy.exp(-((x-(kernel_size-1)/2)**2 + (y-(kernel_size-1)/2)**2)/(2*sigma**2)),
                         (kernel_size, kernel_size))
kernel /= numpy.sum(kernel) # Normalize

new = Image.fromarray(scipy.ndimage.convolve(pix_arr, kernel).astype(numpy.uint8), "L")
new.show()
