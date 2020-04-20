import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

#test image
image_name=' (enter your image path) '

im_data = img.imread(image_name)
print(im_data)
print(np.shape(im_data))

#image RGB data
red_data = im_data[:,:,0]
green_data = im_data[:,:,1]
blue_data = im_data[:,:,2]

#swap to BGR
image1 = np.array([blue_data, green_data, red_data])
image1 = np.swapaxes(image1, 0, 1)
image1 = np.swapaxes(image1, 1, 2)
print(np.shape(image1))

#swap to GRB
image2 = np.array([green_data, red_data, blue_data])
image2 = np.swapaxes(image2, 0, 1)
image2 = np.swapaxes(image2, 1, 2)
print(np.shape(image2))

#assigning colour map as jet
cmap = 'jet'

plt.figure(figsize=(15,10))

#image in RGB (original img)
plt.subplot(231)
plt.imshow(im_data, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Image in RGB')

#image in BGR
plt.subplot(232)
plt.imshow(image1, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Image in BGR')

#image in GRB
plt.subplot(233)
plt.imshow(image2, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Image in GRB')

#shows red channel with cmap
plt.subplot(234)
plt.imshow(red_data, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Red Channel')
plt.colorbar()

#shows green channel with cmap
plt.subplot(236)
plt.imshow(green_data, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Green Channel')
plt.colorbar()

#shows blue channel with cmap
plt.subplot(235)
plt.imshow(blue_data, cmap=cmap, interpolation='nearest')
plt.axis('off')
plt.title('Blue Channel')
plt.colorbar()

#histogram for RGB data
plt.figure(figsize=(15,10))
plt.subplot(131)
plt.hist(red_data.ravel(), bins=100, fc='red', ec='k')
plt.subplot(132)
plt.hist(green_data.ravel(), bins=100, fc='green', ec='k')
plt.subplot(133)
plt.hist(blue_data.ravel(), bins=100, fc='blue', ec='k')
plt.show()
