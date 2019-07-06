import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imread,imresize,imshow
img=imread('image.jpg')

img.shape #this tells you the shape of your image and it is represented by array(length,height,depth=3)

#here 3 means 3 channels(RGB)

'''This image I have used is of shape (2592, 4608, 3)'''

img.dtype #dtype for image mostly 'uint8'

new_img=img*(0.1,0.5,1) #Here, I am adjusting the R,G,B channels

new_img=imresize(new_img,(300,300)) #resizing it into a (300,300,3) image

'''Now, plot using matplotlib'''
plt.imshow(np.uint8(new_img)) 
plt.show()
