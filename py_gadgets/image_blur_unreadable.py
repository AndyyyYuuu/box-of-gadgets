# Andy Yu
# Nov 23, 2023
# Image blurring: 2d convolution, greyscale only, rendered utterly unreadable

k=10;from PIL import Image
p=(f:=Image.open("?.png")
).load();from numpy import*
c=fromfunction(lambda x,y:1
/(2*pi*k*k/9)*exp(-((x-(k-1)
/2)**2+(y-(k-1)/2)**2)/(2*k*
k/9)),(k,k));from scipy import*
Image.fromarray(ndimage.convolve(
[([p[j,i]for j in range(f.size[0]
)])for i in range(f.size[1])],c/
sum(c)).astype(uint8),"L").show()
